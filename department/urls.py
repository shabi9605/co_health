from os import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('staff_register',views.staff_register,name='staff_register'),
    path('add_dashboard',views.add_dashboard,name='add_dashboard'),
    path('view_my_dashboard',views.view_my_dashboard,name='view_my_dashboard'),
    path('dashboard_delete/<int:dashboard_id>',views.dashboard_delete,name='dashboard_delete'),

    path('hospital_register',views.hospital_register,name='hospital_register'),
    path('add_doctor',views.add_doctor,name='add_doctor'),

    path('view_our_staffs',views.view_our_staffs,name='view_our_staffs'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)