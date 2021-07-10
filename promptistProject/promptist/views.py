from django.shortcuts import render
import requests
import re

def promptist_index(request):

    r = requests.get('https://random-word-form.herokuapp.com/random/noun').json()
    res = requests.get('https://random-word-form.herokuapp.com/random/adjective/').json()
    noun = r[0]
    adjective = res[0]
    vowel = re.search('^[aeiou]', adjective)
    context = {'noun' : noun, 'adjective' : adjective, 'vowel' : vowel}


    return render(request, "promptist/index.html", context)