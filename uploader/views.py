from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import UploadedImage
from django.http import JsonResponse

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            return redirect('upload_success', image_id=uploaded_image.id) 
    else:
        form = ImageUploadForm()
    
    return render(request, 'uploader/upload.html', {'form': form})

def success(request, image_id):
    image = UploadedImage.objects.get(id=image_id)
    return render(request, 'uploader/success.html', {'image': image})

def api_upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            return JsonResponse({'url': uploaded_image.image.url}, status=201)
        return JsonResponse(form.errors, status=400)

def view_image(request, image_id):
    image = UploadedImage.objects.get(id=image_id)
    return render(request, 'uploader/view_image.html', {'image': image})
