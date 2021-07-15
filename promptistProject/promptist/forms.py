from django import forms
from promptist.models import *

class PictureForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = True
    class Meta:
        model = Picture
        exclude = ['user']


