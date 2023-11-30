from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render

from django.views import generic

from .forms import CustomUserCreationForm

from django.urls import reverse_lazy

class SignUp(generic.CreateView):
    
    template_name = 'signup.html'
    
    form_class = CustomUserCreationForm
    
    success_url = reverse_lazy('accounts:signup_success')
    
    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)

class SignUpSuccess(generic.TemplateView):
    
    template_name ='signup_success.html'    