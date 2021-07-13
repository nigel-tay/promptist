from promptist.forms import PictureForm
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
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
        res = requests.get('https://random-word-form.herokuapp.com/random/adjective/').json()
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