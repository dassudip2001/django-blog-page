from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
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
      posts=Post.objects.all()
      return render(request, 'dashboard.html',{
        'posts':posts
    })
    else:
        return render(request, 'register.html')
# create new Post
def post(request):
    if request.user.is_authenticated:
    #    if request.method == 'POST':
    #       title=request.POST.get('title')
    #       photo=request.POST.get('photo')
    #       Body=request.POST.get('Body')
    #       post=Post(title=title,photo=photo, Body=Body, 
    #       date=datetime.today())
    #       post.save()
    #       messages.success(request, 'Post Created Successfully!')
          return render(request, 'dashboard.html')
    else:
        return render(request, 'register.html')
    
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
            messages.success(request, 'Your message has been sent!')
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
            messages.success(request, 'Login successfully!')
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
    messages.success(request, 'Logout successfully!')
    return redirect('/')


    #add post
def create_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
          title=request.POST.get('title')
          photo=request.POST.get('photo')
          Body=request.POST.get('Body')
          post=Post(title=title,photo=photo, Body=Body, 
          date=datetime.today())
          post.save()
          messages.success(request, 'Post Created Successfully!')
          

          return redirect('/')
    else:
        return render(request, 'register.html')   


    #update post
def update_post(request,id):
    if request.user.is_authenticated:
        return render(request, 'post_page/update_post.html',) 
    else:
        return redirect('login')  


def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi=Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard')    
        # return redirect('/')
    else:
        return redirect('login')                