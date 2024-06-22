from django.urls import path
from django.contrib import admin 
from django.urls import include 
from . import views

urlpatterns = [
    path("", views.finmarkt, name="finmarkt"),
    # path('admin/', admin.site.urls), 
    path("visualize/", views.visualize, name="visualize"), 
    path("about/", views.about, name="about"),
]

