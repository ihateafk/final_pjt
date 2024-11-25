from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .models import Chat
from .serializers import UserProfileSerializer, ChatItemSerializer, ChatStoreSerializer


# Create your views here.
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def profile(request):
    if request.method == 'GET':
        serializer = UserProfileSerializer(instance=request.user)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = UserProfileSerializer(instance=request.user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    if request.method == 'DELETE':
        request.user.delete()
        return Response({ 'process': True }, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    return Response({
        'pk': request.user.pk,
        'username': request.user.username,
        'email': request.user.email,
    })


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def chatHistory(request):
    if request.method == 'GET':
        chatdata = request.user.chathistory.all().order_by('pk')
        serializer = ChatItemSerializer(instance=chatdata, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print(request)
        serializer = ChatStoreSerializer(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
