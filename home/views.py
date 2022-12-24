from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):

    posts=Post.objects.all()

    return render(request, 'home.html',{
        'posts':posts
    })


# login form
def login(request):
    return render(request, 'login.html')

# login form
def register(request):
    return render(request, 'register.html')
