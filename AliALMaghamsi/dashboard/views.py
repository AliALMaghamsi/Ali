from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.decorators import user_passes_test
from projects.models import Project
from main.models import Contact
from django.core.paginator import Paginator
# Create your views here.

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser,login_url="/admin/login/")
def dashboard_view(request:HttpRequest):
                section = request.GET.get('section') or request.POST.get('section', 'projects')

                if section == 'projects':
                    
                    if "search" in request.GET :
                        projects= Project.objects.filter(title__contains=request.GET["search"])
                    elif "order_by" in request.GET and request.GET["order_by"]=="category":
                        projects=Project.objects.filter().order_by("-category")
                    elif "order_by" in request.GET and request.GET["order_by"]=="completed_date":
                        projects=Project.objects.filter().order_by("-completed_date")
                    else:
                        projects = Project.objects.all()

                    page=request.GET.get('page')
                    paginator=Paginator(projects,2)
                    display=paginator.get_page(page)  
                      
                    
                elif section == 'messages':
                    
                    contacts=Contact.objects.all()
                    page=request.GET.get('page')
                    paginator=Paginator(contacts,3)
                    display=paginator.get_page(page) 
                else:
                    display=None
                return render(request,"dashboard/dashboard.html",context={"section":section,"display":display})
           
            
       
            
