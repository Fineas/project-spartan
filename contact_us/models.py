from django import forms
from django.db import models
from captcha.fields import ReCaptchaField


class ContactUs(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    message = models.CharField(max_length=1000, null=True)


class CreateContact(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = ContactUs
        fields = '__all__'
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput({'required': 'required',
                                         'placeholder': 'Name'}),
            'email': forms.EmailInput({'required': 'required',
                                       'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'required': 'required',
                                                   'placeholder': 'Message'})
        }
