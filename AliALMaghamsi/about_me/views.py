from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.


def about_me_view(request:HttpRequest):
    return render(request,"about_me/about.html")

def resume_view(request:HttpRequest):
    return render(request,"about_me/resume.html")
