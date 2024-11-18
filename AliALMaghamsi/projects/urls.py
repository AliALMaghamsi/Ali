from django.urls import path
from . import views


app_name='projects'

urlpatterns=[
    path('all/',views.all_projects_view,name='all_projects_view'),
    path('new/',views.new_project_view,name='new_project_view'),
    path('detail/<int:project_id>/',views.project_detail_view,name='project_detail_view'),
    path('update/<int:project_id>/',views.update_project_view,name='update_project_view'),
    path('delete/<int:project_id>/',views.delete_project_view,name='delete_project_view'),
]