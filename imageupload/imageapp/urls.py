# imageapp/urls.py
from django.urls import path
from .views import upload_image, upload_success, view_image

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
    path('upload/success/', upload_success, name='upload_success'),
    path('image/<str:image_filename>/', view_image, name='view_image'),
]
