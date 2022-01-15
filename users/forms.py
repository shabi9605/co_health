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

class UserRegisterForm(forms.ModelForm):
   
    class Meta:
        model=UserRegister
        fields=('name','state','ward','house_no','district','city','pincode')



class ComplaintForm(forms.ModelForm):
    complaint=forms.Textarea()
    class Meta:
        model=Complaint
        fields=('complaint',)


class OrganDonationForm(forms.ModelForm):
    class Meta:
        model=OrganDonation
        fields=('phone','weight','height','h_status','blood_group','gender','age','contact_person','organs')



class AddVaccineInfo(forms.ModelForm):
    covid_status=forms.BooleanField(help_text=None,label='Have you ever covid +ve',required=False)
    class Meta:
        model=VaccineInfo
        fields=('name','vaccine_type','ward','contact_no','covid_status')