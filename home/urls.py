from django.test import TestCase

# Create your tests here.
from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name="home"),
    path('login',views.login, name="login"),
    path('register',views.register, name="register"),



]


