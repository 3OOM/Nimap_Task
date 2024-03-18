from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Client
from .serializers import ClientSerializer

@api_view(['GET'])
def list_clients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True, context={'request':request})
    return Response(serializer.data)

@api_view(['POST'])
def create_client(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(created_by=request.user.username)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def retrieve_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    serializer = ClientSerializer(client)
    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
def update_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    serializer = ClientSerializer(client, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save(created_by=request.user.username)
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client.delete()
    return Response(status=204)