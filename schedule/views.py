from django.shortcuts import render

from django.views import generic

from django.urls import reverse_lazy

from .forms import ScheduleRegisterForm, ContactForm

from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

from .models import ScheduleRegister

from django.contrib import messages

from django.core.mail import EmailMessage

class Index(generic.ListView):
    
    template_name = 'index.html'
    
    queryset = ScheduleRegister.objects.order_by('-date')

class Index2(generic.ListView):

    template_name = 'index.html'

    queryset = ScheduleRegister.objects.order_by('date')

@method_decorator(login_required, name='dispatch')
class CreateSchedule(generic.CreateView):
    form_class = ScheduleRegisterForm
    
    template_name = 'schedule_register.html'
    
    success_url = reverse_lazy('schedule:done')
        
    def form_valid(self, form):
        postdata = form.save(commit=False)
        
        postdata.user = self.request.user
        
        postdata.save()
        
        return super().form_valid(form)

class Done(generic.TemplateView):
    
    template_name = 'success_register.html'

class Detail(generic.DetailView):

    template_name = 'detail.html'

    model = ScheduleRegister

class Delete(generic.DeleteView):

    template_name = 'delete.html'

    model = ScheduleRegister

    success_url = reverse_lazy('schedule:index')

    def delete(self, request, *args, **kwargs):

        return super().delete(request, *args, **kwargs)

class Contact(generic.FormView):
    
    template_name = 'contact.html'

    form_class = ContactForm

    success_url = reverse_lazy('schedule:contact')

    def form_valid(self, form):

        name = form.cleaned_data['name']

        email = form.cleaned_data['email']

        message = form.cleaned_data['message']

        title = form.cleaned_data['title']

        subject = 'お問い合わせ: {}'.format(title)

        message = \
            '送信者名:{0}\nメールアドレス:{1}\nタイトル:{2}\nメッセージ:\n{3}'\
                .format(name, email, title, message)
        
        from_email = 'admin@example.com'

        to_list = ['admin@example.com']

        message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list,
                               )
        message.send()
        messages.success(
            self.request,
            'お問い合わせを受け付けました')
        
        return super().form_valid(form)

