from django import forms
from django.db.models import fields
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class VaccineDriveForm(forms.ModelForm):
    available_date=forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model=VaccineDrive
        fields=('vacc_type','vacc_location','available_date','time','ward','max_vaccno','dr_incharge','nurse_asst')