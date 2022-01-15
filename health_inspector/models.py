from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

# Create your models here.

class VaccineDrive(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    vacc_type=models.CharField(max_length=50)
    vacc_location=models.CharField(max_length=50)
    available_date=models.DateField()
    time=models.CharField(max_length=20)
    ward=models.IntegerField()
    max_vaccno=models.IntegerField()
    dr_incharge=models.CharField(max_length=50)
    nurse_asst=models.CharField(max_length=50)
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.user.username)

