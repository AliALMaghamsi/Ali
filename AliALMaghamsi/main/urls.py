from django.urls import path
from . import views


app_name='main'

urlpatterns=[
    path('',views.home_view,name='home_view'),
    path('contact/',views.contact_view,name="contact_view"),
    path('error/',views.error_view,name="error_view"),
    
]