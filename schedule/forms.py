from django.forms import ModelForm, DateInput, Form, CharField, EmailField, Textarea

from .models import ScheduleRegister

class DateInput(DateInput):
    
    input_type = 'date'
    
class ScheduleRegisterForm(ModelForm):  
    class Meta:
        
        model = ScheduleRegister
        
        fields = ['date', 'event', 'place']
        
        widgets = {
            'date': DateInput(),
            }


class ContactForm(Form):
    name = CharField(label='お名前')
    email = EmailField(label='メールアドレス')
    title = CharField(label='件名')
    message = CharField(label='メッセージ', widget=Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'お名前'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレス'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = '件名'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージ'
        self.fields['message'].widget.attrs['class'] = 'form-control'

    
