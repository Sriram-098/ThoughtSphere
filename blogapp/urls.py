from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.signup,name="signup"),
    path("index",views.index,name="index"),
    path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("post",views.post,name="post"),
    path("myposts",views.myposts,name="myposts"),
    path("logout",views.logout,name="logout")
    
]