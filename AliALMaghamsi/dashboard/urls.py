from django.urls import path
from . import views


app_name='dashboard'

urlpatterns=[
    path("dashboard/<str:username>/<str:password>/",views.dashboard_view,name="dashboard_view"),
    path("dashboarderror/",views.dashboard_error_view,name="dashboard_error_view")
     
]