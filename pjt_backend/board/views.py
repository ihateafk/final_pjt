from django.shortcuts import get_object_or_404, render
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

@api_view(['GET', 'PUT', 'DELETE'])
def board_detail(request, board_id):
    article = get_object_or_404(Board, id=board_id)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    if not request.user.is_authenticated:
        return Response({'detail': '로그인이 필요한 서비스입니다.'}, status=401)
        
    if request.method in ['PUT', 'DELETE'] and article.user != request.user:
        return Response({'detail': '권한이 없습니다.'}, status=403)
    
    if request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
            
    elif request.method == 'DELETE':
        article.delete()
        return Response({'detail': '게시글이 삭제되었습니다.'}, status=204)