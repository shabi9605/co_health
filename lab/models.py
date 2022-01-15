from datetime import time
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

class LabRegister(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    license_no=models.IntegerField()
    proof=models.FileField(upload_to='lab_proof',null=True,blank=True)
    working_days=models.CharField(max_length=100)
    working_time=models.CharField(max_length=20)
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.user.username)



class CovidInfo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    lab=models.ForeignKey(LabRegister,on_delete=models.CASCADE,null=True,blank=True)
    patient_name=models.CharField(max_length=50)
    patient_status=models.BooleanField(default=False)
    patient_location=models.CharField(max_length=50)
    patient_phc=models.CharField(max_length=50)
    patient_ward=models.CharField(max_length=20)
    panchayath=models.CharField(max_length=50)
    phone=PhoneNumberField()
    email=models.CharField(max_length=50)
    age=models.IntegerField()
    male='male'
    female='female'
    genders=[
        (male,'male'),
        (female,'female')
    ]
    gender=models.CharField(max_length=20,choices=genders,default=male)
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.patient_name)
