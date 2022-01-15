from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . models import *
from . forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver 
import random
from datetime import datetime,timedelta
from numpy import random

# Create your views here.


def lab_register(request):
    reg=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=LabRegisterForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()

            reg=True
            return redirect('user_login')
        else:
            HttpResponse("invalid form")
    else:
         user_form=UserForm()
         profile_form=LabRegisterForm()
    return render(request,'lab_register.html',{'register':reg,'user_form':user_form,'profile_form':profile_form})



def add_covid_info(request):
    if request.method=="POST":
        covid_info_form=CovidInfoForm(request.POST)
        if covid_info_form.is_valid():
            lab=LabRegister.objects.get(user=request.user)
            cp=CovidInfo(user=request.user,lab=lab,patient_name=covid_info_form.cleaned_data['patient_name'],patient_status=covid_info_form.cleaned_data['patient_status'],patient_location=covid_info_form.cleaned_data['patient_location'],patient_phc=covid_info_form.cleaned_data['patient_phc'],patient_ward=covid_info_form.cleaned_data['patient_ward'],panchayath=covid_info_form.cleaned_data['panchayath'],phone=covid_info_form.cleaned_data['phone'],email=covid_info_form.cleaned_data['email'],age=covid_info_form.cleaned_data['age'])
            cp.save()
            return render(request,'add_covid_info.html',{'msg':'successfully added covid info'})
        else:
            return HttpResponse("Invalid form")
    covid_info_form=CovidInfoForm()
    return render(request,'add_covid_info.html',{'form':covid_info_form})



def view_covid_info(request):
    covid_info=CovidInfo.objects.filter(user=request.user).order_by('-date')
    return render(request,'view_covid_info.html',{'covid_info':covid_info})


def view_all_covid_info(request):
    all_covid=CovidInfo.objects.filter(patient_status=True).order_by('-date')
    return render(request,'view_covid_info.html',{'covid_info':all_covid})


