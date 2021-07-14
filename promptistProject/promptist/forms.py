from django import forms
# from bootstrap_modal_forms.forms import BSModalModelForm
from promptist.models import *

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        exclude = ['user']

# class PictureForm(BSModalModelForm):
#     class Meta:
#         model = Picture
#         fields = '__all__'
#         exclude = ['user']

