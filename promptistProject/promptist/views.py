from promptist.forms import PictureForm
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
# from bootstrap_modal_forms.generic import BSModalCreateView
import requests
import re
import json

from promptist.models import *
from accounts.models import *

#landing page
def promptist_landing(request):
    return render(request, "promptist/landing.html")

#Generator page
def promptist_generator(request):

    context={}

    if request.method == "POST":
        r = requests.get('https://random-word-form.herokuapp.com/random/noun').json()
        res = requests.get('https://random-word-form.herokuapp.com/random/adjective/a').json()
        noun = r[0]
        adjective = res[0]
        vowel = re.search('^[aeiou]', adjective)

        context = {'noun' : noun, 'adjective' : adjective, 'vowel' : vowel}

    return render(request, "promptist/generator.html", context) #

#Gallery page
@login_required
def promptist_gallery(request):

    pictures = Picture.objects.all()
    context = {'pictures' : pictures}

    return render(request, "promptist/gallery.html", context)

#Profile page
@login_required
def promptist_profile(request): #, userid):
    print(request.user)
    # template_name = 'promptist/profile.html'
    # form_class = PictureForm
    # success_message = 'Image uploaded Successfully'
    # success_url = reverse_lazy('promptist_profile_page')

    form = PictureForm()
    if request.method == "POST":
        form =PictureForm(request.POST, request.FILES)
        if form.is_valid():
            pictures = form.save(commit=False)
            pictures.user = request.user
            pictures.save()
        # user = User.objects.get(pk=userid)
        # pictures = Picture.objects.filter(user=userid)
    pictures = Picture.objects.filter(user=request.user)

    context = {'pictures' : pictures, 'form' : form}

    return render(request, "promptist/profile.html", context)

@login_required
def delete(request, imageid):
    if request.method == "POST":
        image_to_delete=Picture.objects.get(pk=imageid)
        image_to_delete.delete()
    
    return redirect("promptist:promptist_profile_page")

@login_required
def search_profile(request):
    form = PictureForm()

    if request.method == "POST":
        
        pictures = Picture.objects.filter(user=request.user)
        form =PictureForm(request.POST, request.FILES)
        if form.is_valid():
            pictures = form.save(commit=False)
            pictures.user = request.user
            pictures.save()
        
        searched = request.POST.get('searched', False)
        pictures = Picture.objects.filter(prompt__contains=searched, user=request.user)
        
        context = {'searched' : searched, 'pictures' : pictures, 'form' : form}
        return render(request, "promptist/profile_search.html", context)
