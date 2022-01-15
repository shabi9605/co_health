from re import A
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.index,name='index'),
    path('user_register',views.user_register,name='user_register'),
    path('user_login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('dashboard',views.dashboard,name='dashboard'),

    path('add_complaint',views.add_complaint,name='add_complaint'),
    path('my_complaint',views.my_complaint,name='my_complaint'),
    path('organ_donation_form',views.organ_donation_form,name='organ_donation_form'),
    path('view_my_donation',views.view_my_donation,name='view_my_donation'),
    path('view_all_donation',views.view_all_donation,name='view_all_donation'),
    path('add_vaccine_info',views.add_vaccine_info,name='add_vaccine_info'),

    path('view_my_vaccine_info',views.view_my_vaccine_info,name='view_my_vaccine_info'),
    path('view_all_vaccine_info',views.view_all_vaccine_info,name='view_all_vaccine_info'),

    path('cancel_donation/<int:id>',views.cancel_donation,name='cancel_donation'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)