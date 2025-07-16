from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo

def celebration(request):
    return render(request, 'index.html')  # Homepage

def gallery(request):
    photos = Photo.objects.all()  # Get all uploaded photos
    return render(request, 'gallery.html', {'photos': photos})

def quotes(request):
    return render(request, 'quotes.html')  # Love quotes page

def upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the photo
            return redirect('gallery')  # Go to gallery after upload
    else:
        form = PhotoForm()
    return render(request, 'upload.html', {'form': form})