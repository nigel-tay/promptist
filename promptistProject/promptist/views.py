from django.shortcuts import render, redirect
from django.http.response import JsonResponse
import requests
import re
import json

from promptist.models import *
from accounts.models import *

def promptist_landing(request):
    return render(request, "promptist/landing.html")


def promptist_generator(request):

    # r = requests.get('https://random-word-form.herokuapp.com/random/noun').json()
    # res = requests.get('https://random-word-form.herokuapp.com/random/adjective/').json()
    # noun = r[0]
    # adjective = res[0]
    # vowel = re.search('^[aeiou]', adjective)

    # context = {'noun' : noun, 'adjective' : adjective, 'vowel' : vowel}

    return render(request, "promptist/generator.html") #, context)


def promptist_gallery(request):

    pictures = Picture.objects.all()
    context = {'pictures' : pictures}

    return render(request, "promptist/gallery.html", context)


def upload_picture(request, userid):
    if request.method == "POST":
        try:
            user = User.objects.get(pk=userid)
        except:
            return redirect("promptist:promptist_landing", userid)

        if request.user.is_authenticated:
            data = json.loads(request.body)
            user.picture.create(
                prompt = data['data'],
                image = data['image']
            )
        else:
            return JsonResponse({"message" : "Please log in"}, status=401)

    return JsonResponse({"message" : "Image uploaded Successfully"}, status=200)


def promptist_profile(request, userid):
    if request.method == "GET":
        user = User.objects.get(pk=userid)
        pictures = Picture.objects.filter(user=userid)
        context = {'pictures' : pictures}

    return render(request, "promptist/profile.html", context)