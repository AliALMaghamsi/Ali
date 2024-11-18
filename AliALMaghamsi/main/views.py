from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .forms import ContactForm
from .models import Contact
from projects.models import Project
# Create your views here.


def home_view(request:HttpRequest):

    main_projects=Project.objects.filter()[:2]

    return render(request,"main/index.html",context={"main_projects":main_projects})


def contact_view(request:HttpRequest):
    contact_form=ContactForm()
    if request.method =="POST":
        contact_form=ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect("main:home_view")
    return render(request,'main/contact.html')


def error_view(request:HttpRequest):
    return render(request,"main/error.html")