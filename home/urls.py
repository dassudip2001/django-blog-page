from django.test import TestCase

# Create your tests here.
from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name="index"),
    path('post',views.post, name="home page"),

    path('login/',views.LoginPage,name='login'),
    path('register',views.register, name="register"),
    path('logout/',views.LogoutPage,name='logout'),

]


