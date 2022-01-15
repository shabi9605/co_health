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
from lab.models import *

# Create your views here.

def index(request):
    return render(request,'index.html')


def user_register(request):
    reg=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserRegisterForm(data=request.POST)
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
         profile_form=UserRegisterForm()
    return render(request,'user_register.html',{'register':reg,'user_form':user_form,'profile_form':profile_form}) 



def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        try:
            lab=LabRegister.objects.get(user=user)
        except:
            pass
        try:
            public=UserRegister.objects.get(user=user)
        except:
            pass
        try:
            staff=StaffRegister.objects.get(user=user)
        except:
            pass
        try:
            hospital=Hospital.objects.get(user=user)
        except:
            pass
        if user:
            if user.is_active:
                try:
                    if lab:
                        active=LabRegister.objects.all().filter(user_id=user.id,status=True)
                        if active:
                            login(request,user)
                            return HttpResponseRedirect(reverse('dashboard'))
                        else:
                            return HttpResponse("Waiting for approval")
                except:
                    pass

                try:
                    if staff:
                        active=StaffRegister.objects.all().filter(user_id=user.id,status=True)
                        if active:
                            login(request,user)
                            return HttpResponseRedirect(reverse('dashboard'))
                        else:
                            return HttpResponse("Waiting for approval")
                except:
                    pass

                try:
                    if hospital:
                        active=Hospital.objects.all().filter(user_id=user.id,status=True)
                        if active:
                            login(request,user)
                            return HttpResponseRedirect(reverse('dashboard'))
                        else:
                            return HttpResponse("Waiting for approval")
                except:
                    pass

                try:
                    if public:
                        
                        login(request,user)
                        return HttpResponseRedirect(reverse('dashboard'))
                    else:
                        return HttpResponse("Waiting for approval")
                except:
                    pass

                try:
                    if user.is_superuser:
                        
                        login(request,user)
                        return HttpResponseRedirect(reverse('dashboard'))
                    else:
                        return HttpResponse("Waiting for approval")
                except:
                    pass
               
            else:
                return HttpResponse("Not active")
        else:
            return HttpResponse("Invalid username or password")
    else:
        
        return render(request,'login.html')




def dashboard(request):
    dashboard=Dashboard.objects.all().order_by('-date')
    return render(request,'dashboard.html',{'dashboard':dashboard})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')



def add_complaint(request):
    if request.method=="POST":
        complaint_form=ComplaintForm(request.POST)
        if complaint_form.is_valid():
            cp=Complaint(user=request.user,complaint=complaint_form.cleaned_data['complaint'])
            cp.save()
            return render(request,'complaint.html',{'msg':'successfully added complaint'})
        else:
            return HttpResponse("Invalid form")
    complaint_form=ComplaintForm()
    return render(request,'complaint.html',{'form':complaint_form})


def my_complaint(request):
    my_complaints=Complaint.objects.filter(user=request.user)
    return render(request,'view_complaints.html',{'my_complaints':my_complaints})



def organ_donation_form(request):
    if request.method=="POST":
        organ_dnation_form=OrganDonationForm(request.POST)
        if organ_dnation_form.is_valid():
            donor=UserRegister.objects.get(user=request.user)
            cp=OrganDonation(user=request.user,donor=donor,phone=organ_dnation_form.cleaned_data['phone'],weight=organ_dnation_form.cleaned_data['weight'],height=organ_dnation_form.cleaned_data['height'],h_status=organ_dnation_form.cleaned_data['h_status'],
            blood_group=organ_dnation_form.cleaned_data['blood_group'],gender=organ_dnation_form.cleaned_data['gender'],
            age=organ_dnation_form.cleaned_data['age'],contact_person=organ_dnation_form.cleaned_data['contact_person'],
            organs=organ_dnation_form.cleaned_data['organs'])
            
            cp.save()
            return render(request,'organ_donation_form.html',{'msg':'successfully added donation'})
        else:
            return HttpResponse("Invalid form")
    organ_dnation_form=OrganDonationForm()
    return render(request,'organ_donation_form.html',{'form':organ_dnation_form})


def view_my_donation(request):
    my_donation=OrganDonation.objects.filter(user=request.user)
    return render(request,'my_donation.html',{'my_donation':my_donation})


def view_all_donation(request):
    all_donation=OrganDonation.objects.all().order_by('-date')
    return render(request,'my_donation.html',{'my_donation':all_donation})


def cancel_donation(request,id):
    donation=OrganDonation.objects.get(id=id)
    donation.delete()
    return redirect('view_my_donation')


def add_vaccine_info(request):
    if request.method=="POST":
        vaccine_form=AddVaccineInfo(request.POST)
        if vaccine_form.is_valid():
            
            cp=VaccineInfo(user=request.user,name=vaccine_form.cleaned_data['name'],vaccine_type=vaccine_form.cleaned_data['vaccine_type'],ward=vaccine_form.cleaned_data['ward'],contact_no=vaccine_form.cleaned_data['contact_no'],covid_status=vaccine_form.cleaned_data['covid_status'])
            cp.save()
            return render(request,'vaccine_form.html',{'msg':'successfully added vaccine details'})
        else:
            return HttpResponse("Invalid form")
    vaccine_form=AddVaccineInfo()
    return render(request,'vaccine_form.html',{'form':vaccine_form})



def view_my_vaccine_info(request):
    my_vaccine=VaccineInfo.objects.filter(user=request.user).order_by('-date')
    return render(request,'my_vaccine_info.html',{'vaccine':my_vaccine})


def view_all_vaccine_info(request):
    all_vaccine=VaccineInfo.objects.all().order_by('-date')
    return render(request,'my_vaccine_info.html',{'vaccine':all_vaccine})
