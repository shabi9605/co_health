from os import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('add_covid_info',views.add_covid_info,name='add_covid_info'),
    path('view_covid_info',views.view_covid_info,name='view_covid_info'),
    path('view_all_covid_info',views.view_all_covid_info,name='view_all_covid_info'),

    path('lab_register',views.lab_register,name='lab_register'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)