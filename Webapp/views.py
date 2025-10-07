from django.shortcuts import render, redirect
from .models import Gallery

def upload_image(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')

        if title and image:
            Gallery.objects.create(title=title, image=image)
            return redirect('gallery')  
    return render(request, 'upload.html')


def gallery_view(request):
    images = Gallery.objects.all()
    return render(request, 'gallery.html', {'images': images})
