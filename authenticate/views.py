from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"authenticate/index.html")

def signup(request):
    return render(request,"authenticate/signup.html")

def signin(request):
    return render(request,"authenticate/signin.html")

def signout(request):
   pass