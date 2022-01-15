from django import forms
from django.db.models import fields
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CovidInfoForm(forms.ModelForm):
    class Meta:
        model=CovidInfo
        fields=('patient_name','patient_location','patient_phc','patient_ward','age','panchayath','gender','phone','email','patient_status')




class UserForm(UserCreationForm):
    username=forms.CharField(help_text=None,label='Username')
    password1=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Confirm Password')
    class Meta:
        model=User
        fields=('username','password1','password2','email')
        labels=('password1','password','password2','confirm password')

class LabRegisterForm(forms.ModelForm):
   
    class Meta:
        model=LabRegister
        fields=('name','location','state','district','license_no','proof','working_days','working_time')