from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class StaffRegister(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    staff_name=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pincode=models.IntegerField()
    phone=PhoneNumberField()
    designation=models.CharField(max_length=50)
    health_inspector='health_inspector'
    asha_worker='asha_worker'
    councilor='councilor'
    user_types=[
        (health_inspector,'health_inspector'),
        (asha_worker,'asha_worker'),
        (councilor,'councilor')
    ]
    user_type=models.CharField(max_length=50,choices=user_types,default=health_inspector)
    status=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user.username)


class Dashboard(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    ward_no=models.IntegerField()
    no_of_positive=models.IntegerField()
    no_of_women=models.IntegerField()
    no_of_men=models.IntegerField()
    no_of_children=models.IntegerField()
    TPR=models.FloatField()
    WPR=models.FloatField()
    home_quarantine=models.CharField(max_length=30)
    total_death=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)




class Hospital(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    hospital_name=models.CharField(max_length=50)
    area=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pincode=models.IntegerField()
    phone=PhoneNumberField()
    license=models.CharField(max_length=50)
    hospital='hospital'
    phc='phc'
    types=[
        (hospital,'hospital'),
        (phc,'phc')

    ]
    type=models.CharField(max_length=50,choices=types,default=hospital)
    status=models.BooleanField(default=False)
    def __str__(self):
        return str(self.user.username)



class Doctor(models.Model):
    name=models.CharField(max_length=50)
    hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE,null=True,blank=True)
    doctor='doctor'
    nurse='nurse'
    types=[
        (doctor,'doctor'),
        (nurse,'nurse')
    ]
    type=models.CharField(max_length=50,choices=types,default=doctor)
    qualification=models.CharField(max_length=50)
    date_of_join=models.DateField()
    experience=models.IntegerField()
    def __str__(self):
        return str(self.name)
