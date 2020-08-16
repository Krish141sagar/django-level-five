from django import forms
from django.contrib.auth.models import User
from . import models

class Teacher_Form(forms.ModelForm):

    class Meta:
        model=models.Teacher
        #fields=('Name','Mobile','Email')
        fields='__all__'

class  Userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username','email','password')
class Portfoiloform(forms.ModelForm):
    class Meta:
        model=models.PortfoiloModel
        fields=("portfoilo","Image_link")
