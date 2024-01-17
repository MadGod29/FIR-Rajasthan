# imageapp/views.py
from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import UploadedImage
from django.http import FileResponse
from django.conf import settings
import os



def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = ImageUploadForm()

    return render(request, 'imageapp/upload_image.html', {'form': form})

# def upload_success(request):
#     images = UploadedImage.objects.all()
#     return render(request, 'imageapp/upload_success.html', {'images': images})

def upload_success(request):
    images = UploadedImage.objects.all()
    image_urls = [image.image.url for image in images]
    return render(request, 'imageapp/upload_success.html', {'image_urls': image_urls})
#

def view_image(request, image_filename):
    image_path = os.path.join(settings.MEDIA_ROOT, 'images', image_filename)
    return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')
