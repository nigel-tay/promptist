from promptist.views import *
from django.contrib import admin
from django.urls import path

app_name = "promptist"

urlpatterns = [
    path('', promptist_index, name="promptist_index_page")
]
