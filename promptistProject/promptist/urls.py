from promptist.views import *
from django.contrib import admin
from django.urls import path

app_name = "promptist"

urlpatterns = [
    path('', promptist_landing, name="promptist_landing_page"),
    path('generator/', promptist_generator, name="promptist_generator_page"),
    path('gallery/', promptist_gallery, name="promptist_gallery_page"),
    path('profile/', promptist_profile, name="promptist_profile_page"),
    path('delete/<uuid:imageid>', delete, name="delete"),
    path('profile/search/', search_profile, name="search_profile"),
]
