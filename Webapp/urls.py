from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import upload_image, gallery_view

urlpatterns = [
    path('upload/', upload_image, name='upload'),
    path('gallery/', gallery_view, name='gallery'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
