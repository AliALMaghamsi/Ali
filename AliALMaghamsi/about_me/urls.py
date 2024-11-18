from django.urls import path
from . import views


app_name='about'

urlpatterns=[
    path("me/",views.about_me_view,name="about_me_view"),
    path("resume/",views.resume_view,name="resume_view"),
    
]