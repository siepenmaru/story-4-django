from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="ppw-index"),
    path('about-me/', views.about, name="ppw-about"),
    path('my-work/', views.work, name="ppw-work"),
    path('contact-me/', views.contact, name="ppw-contact"),
]
