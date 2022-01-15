from datetime import time
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

class UserRegister(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pincode=models.IntegerField()
    ward=models.IntegerField(null=True,blank=True)
    house_no=models.IntegerField(null=True,blank=True)
    
    status=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user.username)


class Organs(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)



class Complaint(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    complaint=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)


class OrganDonation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    donor=models.ForeignKey(UserRegister,on_delete=models.CASCADE,null=True,blank=True)
    
    blood_group=models.CharField(max_length=50,null=True,blank=True)
    male='male'
    female='female'
    genders=[
        (male,'male'),
        (female,'female')
    ]
    gender=models.CharField(max_length=20,choices=genders,default=male,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    contact_person=PhoneNumberField(null=True,blank=True)
    organs=models.ForeignKey(Organs,on_delete=models.CASCADE,null=True,blank=True)
    weight=models.IntegerField()
    height=models.IntegerField()
    h_status=models.CharField(max_length=20)
    phone=PhoneNumberField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)



class VaccineInfo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50)
    vaccine_type=models.CharField(max_length=50)
    ward=models.IntegerField()
    
    contact_no=PhoneNumberField()
    covid_status=models.BooleanField(default=False)
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)




