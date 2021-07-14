from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import AuthenticationForm

from accounts.forms import *

def register_view(request):
    register = RegisterNewUserForm()
    if request.method == "POST":
        register = RegisterNewUserForm(request.POST)
        if register.is_valid():
            user = register.save()
            login(request, user)
            
            return redirect("promptist:promptist_landing_page")
    
    context = {"register" : register}
    return render(request, "accounts/register.html", context)


def login_view(request):
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("promptist:promptist_profile_page")

    context = {"login_form" : login_form}
    return render(request, "accounts/login.html", context)

def logout_view(request):
    # logout(request)
    # return redirect("login_view")
    logout(request)
    # response = redirect('login_view')
    # response.delete_cookie('user_location')
    return redirect("promptist:promptist_profile_page") #response
