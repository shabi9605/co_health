from django import forms
from django.db.models import fields
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    username=forms.CharField(help_text=None,label='Username')
    password1=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Confirm Password')
    class Meta:
        model=User
        fields=('username','password1','password2','email')
        labels=('password1','password','password2','confirm password')

class StaffRegisterForm(forms.ModelForm):
   
    class Meta:
        model=StaffRegister
        fields=('staff_name','designation','phone','state','district','city','pincode','user_type')


    
class HospitalRegisterForm(forms.ModelForm):
   
    class Meta:
        model=Hospital
        fields=('hospital_name','area','district','city','pincode','phone','license','type')


class DashboardForm(forms.ModelForm):
    class Meta:
        model=Dashboard
        fields=('ward_no','no_of_positive','no_of_women','no_of_men','no_of_children','TPR','WPR','home_quarantine','total_death')



class DoctorForm(forms.ModelForm):
    date_of_join=forms.DateField(label='date of join eg: 2021-12-08')
    class Meta:
        model=Doctor
        fields=('name','type','qualification','date_of_join','experience')