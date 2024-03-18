from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Project
from .serializers import ProjectSerializer

@api_view(['GET'])
def list_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True,context={'request':request})
    return Response(serializer.data)

@api_view(['POST'])
def create_project(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user.username)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def retrieve_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    serializer = ProjectSerializer(project)
    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
def update_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    serializer = ProjectSerializer(project, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save(created_by=request.user.username)
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    return Response(status=204)