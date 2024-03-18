from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_clients, name='list-clients'),
    path('create/', views.create_client, name='create-client'),
    path('<int:client_id>/', views.retrieve_client, name='retrieve-client'),
    path('<int:client_id>/update/', views.update_client, name='update-client'),
    path('<int:client_id>/delete/', views.delete_client, name='delete-client'),
]