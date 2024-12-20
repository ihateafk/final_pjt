from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Board, Comment
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from .serializers import ArticleListSerizlizer, ArticleSerializer, CommentListSerializer, CommentSerializer

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def board_list(request) :
    if request.method == 'GET' :
        articles = Board.objects.all().order_by('-created_at')
        serializers = ArticleListSerizlizer(articles, many=True)
        return Response(serializers.data)
    elif request.method == 'POST' :
        serializers = ArticleSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True) :
            serializers.save(user=request.user)
            return Response(serializers.data)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def board_list(request) :
#     if request.method == 'POST' :
#         serializers = ArticleSerializer(data=request.data)
#         if serializers.is_valid(raise_exception=True) :
#             serializers.save(user=request.user)
#             return Response(serializers.data)

@api_view(['GET', 'PUT', 'DELETE'])
def board_detail(request, board_id):
    article = get_object_or_404(Board, id=board_id)
    
    if request.method == 'GET':
        comments = Comment.objects.filter(board=article)
        serializer = ArticleSerializer(article, context={'comments': comments})
        response_data = serializer.data
        response_data['comment_set'] = CommentListSerializer(comments, many=True).data
        response_data['comment_count'] = comments.count()
        return Response(response_data)
    
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
    
@api_view(['GET'])
@permission_classes([AllowAny])
def comment_list(request, board_id):
    if request.method == 'GET':
        comments = Comment.objects.filter(board_id=board_id)
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, board_id) :
    board = Board.objects.get(pk=board_id)

    if request.method == 'POST' :
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save(board=board, user=request.user)
            return Response(serializer.data)
        

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, board_id, comment_id) :
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user != request.user :
        return Response({'detail' : '댓글 삭제 권한이 없습니다'})
    
    comment.delete()
    return Response({'detail' : '댓글이 삭제되었습니다'})