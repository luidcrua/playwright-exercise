"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path

from challenge_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
]
