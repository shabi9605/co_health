from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('vaccine_drive_form',views.vaccine_drive_form,name='vaccine_drive_form'),
    path('view_vaccine_drive',views.view_vaccine_drive,name='view_vaccine_drive'),
    path('update_vaccine_drive/<int:drive_id>',views.update_vaccine_drive,name='update_vaccine_drive'),
    path('delete_vaccine_drive/<int:drive_id>',views.delete_vaccine_drive,name='delete_vaccine_drive'),

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)