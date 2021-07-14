from django.urls import path

from accounts.views import *

app_name = "accounts"

urlpatterns = [
    path('register/', register_view, name="register_view_page"),
    path('login/', login_view, name="login_view_page"),
    path('logout/', logout_view, name="logout"),
]