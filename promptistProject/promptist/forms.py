from django import forms
from promptist.models import *

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        exclude = ['user']

    
