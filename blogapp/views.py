from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from .models import Posts
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='signin')
def index(request):
    data =Posts.objects.all()
    
    print(data)
    return render(request,"index.html",{"data":data})

def signup(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        if User.objects.filter(username=name).exists():
            messages.info(request,"user name exists")
            return redirect("signup")
        user=User.objects.create_user(username=name,email=email,password=password)
        user.save()

        return redirect("signin")

    return render(request,"signup.html")

def signin(request):

    if request.method=="POST":
        name=request.POST.get("name")
        password=request.POST.get("password")
        user=auth.authenticate(username=name,password=password)
        print(user)

        if user is not None:
            print("user is authnetiacate")
            auth.login(request,user)
            return redirect("index")
        

    return render(request,"signin.html")

@login_required(login_url='signin')
def post(request):
    if request.method=="POST":
        title=request.POST.get("title")
        content=request.POST.get('content')
        date_time=request.POST.get('date_posted')
        new_post = Posts(title=title, content=content, author=request.user)
        new_post.save()

        return redirect('index')

        
    return render(request,"post.html")

@login_required(login_url='signin')
def myposts(request):
    data=Posts.objects.filter(author=request.user)

    return render(request,"myposts.html",{"data":data})

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect("signin")
    


