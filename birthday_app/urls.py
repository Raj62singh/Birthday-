from django.urls import path
from . import views

urlpatterns = [
    path('', views.celebration, name='celebration'),  # Homepage
    path('gallery/', views.gallery, name='gallery'),  # Photo gallery
    path('quotes/', views.quotes, name='quotes'),  # Love quotes
    path('upload/', views.upload, name='upload'),  # Photo upload
]