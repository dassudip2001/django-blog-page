from django.shortcuts import render,HttpResponse,redirect
from .models import Post
from django.contrib.auth.models import User
from .models import Contact
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    posts=Post.objects.all()

    return render(request, 'post.html',{
        'posts':posts
    })

# contact us
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today() )
        contact.save()
        messages.success(request, 'Your message has been sent!')
        
    return render(request, 'contact/contact.html')
# about us
def about_us(request):
    return render(request, 'about.html') 
# dashboard

def dashboard_page(request):
    if request.user.is_authenticated:
      return render(request, 'dashboard.html')
    else:
        return render(request, 'register.html')

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
            return HttpResponse("Your password and conform password are not Same!!")
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
            return redirect('/')
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