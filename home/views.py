from django.shortcuts import render,HttpResponse,redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    posts=Post.objects.all()

    return render(request, 'post.html',{
        'posts':posts
    })

# home page 

def post(request):
    return render(request, 'post.html')
# login form
def register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'register.html')

# login form
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('post')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')
    # if request.method=='POST':
    #     username=request.POST.get('username')
    #     pass1=request.POST.get('pass')
    #     user=authenticate(request,username=username,password=pass1)
    #     if user is not None:
    #         login(request,User)
    #         return redirect('home')
    #     else:
    #         return HttpResponse ("Username or Password is incorrect!!!")

    # return render (request,'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('/')