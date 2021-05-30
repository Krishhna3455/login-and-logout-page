from django.contrib import admin
from django.urls import path
from Techinfo import views

urlpatterns = [
    path("", views.index, name='home'),
    path("contact", views.contact, name='contact'),
    path("services", views.services, name='services'),
    path("blog", views.blog, name='blog'),
]
