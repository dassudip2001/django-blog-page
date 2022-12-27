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
    path('dashboard_page',views.dashboard_page,name='dashboard_page'),
    path("contact", views.contact, name='contact'), 
    path('about_us',views.about_us,name='about_us'),


    path('login/',views.LoginPage,name='login'),
    path('register',views.register, name="register"),
    path('logout/',views.LogoutPage,name='logout'),
    path('update_post/<int:id>',views.update_post,name='update_post'),
    path('delete_post/<int:id>',views.delete_post,name='delete_post'),
    path('create_post/',views.create_post,name='create_post'),



]


