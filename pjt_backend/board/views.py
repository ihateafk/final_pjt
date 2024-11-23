from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Board, Comment
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializers import ArticleListSerizlizer, ArticleSerializer

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def board_list(request) :
    
    if request.method == 'GET' :
        articles = Board.objects.all()
        serializers = ArticleListSerizlizer(articles, many=True)
        return Response(serializers.data)
    elif request.method == 'POST' :
        serializers = ArticleSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True) :
            serializers.save(user=request.user)
            return Response(serializers.data)