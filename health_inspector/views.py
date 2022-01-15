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
from department.models import *

# Create your views here.

def vaccine_drive_form(request):
    if request.method=="POST":
        vaccine_form=VaccineDriveForm(request.POST)
        if vaccine_form.is_valid():
            cp=VaccineDrive(user=request.user,vacc_type=vaccine_form.cleaned_data['vacc_type'],vacc_location=vaccine_form.cleaned_data['vacc_location'],available_date=vaccine_form.cleaned_data['available_date'],time=vaccine_form.cleaned_data['time'],ward=vaccine_form.cleaned_data['ward'],max_vaccno=vaccine_form.cleaned_data['max_vaccno'],dr_incharge=vaccine_form.cleaned_data['dr_incharge'],nurse_asst=vaccine_form.cleaned_data['nurse_asst'])
            cp.save()
            return render(request,'add_vaccine_drive.html',{'msg':'successfully added vaccine drive'})
        else:
            return HttpResponse("Invalid form")
    vaccine_form=VaccineDriveForm()
    return render(request,'add_vaccine_drive.html',{'form':vaccine_form})


def view_vaccine_drive(request):
    vaccine_drive=VaccineDrive.objects.all().order_by('-date')
    return render(request,'vaccine_drive.html',{'vaccine_drive':vaccine_drive})



def update_vaccine_drive(request,drive_id):
    vaccine_drive=VaccineDrive.objects.get(id=drive_id)
    print(vaccine_drive)
    update_vaccine_form=VaccineDriveForm(instance=vaccine_drive)
    if request.method=="POST":
        update_vaccine_form=VaccineDriveForm(request.POST,request.FILES,instance=vaccine_drive)
        update_vaccine_form.save()
        return redirect('view_vaccine_drive')
    return render(request,'add_vaccine_drive.html',{'form':update_vaccine_form})


def delete_vaccine_drive(request,drive_id):
    vaccine_drive=VaccineDrive.objects.get(id=drive_id)
    vaccine_drive.delete()
    return redirect('view_vaccine_drive')

