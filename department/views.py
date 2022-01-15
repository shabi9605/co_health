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

def staff_register(request):
    reg=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=StaffRegisterForm(data=request.POST)
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
         profile_form=StaffRegisterForm()
    return render(request,'staff_register.html',{'register':reg,'user_form':user_form,'profile_form':profile_form}) 



def hospital_register(request):
    reg=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=HospitalRegisterForm(data=request.POST)
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
         profile_form=HospitalRegisterForm()
    return render(request,'hospital_register.html',{'register':reg,'user_form':user_form,'profile_form':profile_form})



def add_dashboard(request):
    if request.method=="POST":
        dashboard_form=DashboardForm(request.POST)
        if dashboard_form.is_valid():
            
            cp=Dashboard(user=request.user,ward_no=dashboard_form.cleaned_data['ward_no'],no_of_positive=dashboard_form.cleaned_data['no_of_positive'],no_of_women=dashboard_form.cleaned_data['no_of_women'],no_of_men=dashboard_form.cleaned_data['no_of_men'],no_of_children=dashboard_form.cleaned_data['no_of_children'],TPR=dashboard_form.cleaned_data['TPR'],WPR=dashboard_form.cleaned_data['WPR'],home_quarantine=dashboard_form.cleaned_data['home_quarantine'],total_death=dashboard_form.cleaned_data['total_death'])
            cp.save()
            return render(request,'dashboard_form.html',{'msg':'successfully added dashboard details'})
        else:
            return HttpResponse("Invalid form")
    dashboard_form=DashboardForm()
    return render(request,'dashboard_form.html',{'form':dashboard_form})




def add_doctor(request):
    hospital=Hospital.objects.get(user=request.user)
    if request.method=="POST":
        dashboard_form=DoctorForm(request.POST)
        if dashboard_form.is_valid():
            
            cp=Doctor(name=dashboard_form.cleaned_data['name'],hospital=hospital,type=dashboard_form.cleaned_data['type'],
            qualification=dashboard_form.cleaned_data['qualification'],date_of_join=dashboard_form.cleaned_data['date_of_join'],
            experience=dashboard_form.cleaned_data['experience'])
            cp.save()
            return render(request,'doctor_form.html',{'msg':'successfully added dashboard details'})
        else:
            return HttpResponse("Invalid form")
    dashboard_form=DoctorForm()
    return render(request,'doctor_form.html',{'form':dashboard_form})


def view_my_dashboard(request):
    dashboard=Dashboard.objects.filter(user=request.user).order_by('-date')
    return render(request,'my_dashboard.html',{'dashboard':dashboard})


def dashboard_delete(request,dashboard_id):
    dashboard=Dashboard.objects.get(id=dashboard_id)
    dashboard.delete()
    return redirect('view_my_dashboard')



def view_our_staffs(request):
    doc_nur=Doctor.objects.filter(hospital=request.user.hospital)
    return render(request,'view_our_staffs.html',{'doc_nur':doc_nur})