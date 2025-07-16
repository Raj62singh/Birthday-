from django import forms  # Note: "forms" not "form"
from .models import Photo

class PhotoForm(forms.ModelForm):  # Use "forms" here
    class Meta:
        model = Photo
        fields = ['image']  # Only show the image field in the form