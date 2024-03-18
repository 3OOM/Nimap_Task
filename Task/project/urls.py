from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_projects, name='list-projects'),
    path('create/', views.create_project, name='create-project'),
    path('<int:project_id>/', views.retrieve_project, name='retrieve-project'),
    path('<int:project_id>/update/', views.update_project, name='update-project'),
    path('<int:project_id>/delete/', views.delete_project, name='delete-project'),
]