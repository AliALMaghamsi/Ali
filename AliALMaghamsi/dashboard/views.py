from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from projects.models import Project
from main.models import Contact
from django.core.paginator import Paginator
# Create your views here.

def dashboard_view(request:HttpRequest,username, password):
            admin_name='Ali'
            admin_pass="Ali-123"
            

            
            if username==admin_name and password==admin_pass:    
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
                return render(request,"dashboard/dashboard.html",context={"section":section,"display":display,"user":admin_name,"password":admin_pass})
            else:
                 return redirect("dashboard:dashboard_error_view")
            
       
            

def dashboard_error_view(request:HttpRequest):
    return render(request,"dashboard/dasherror.html")