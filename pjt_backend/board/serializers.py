from rest_framework import serializers
from .models import Board, Comment
from accounts.serializers import CustomUserDetailSerializer
from accounts.models import User

# boards/serializers.py
class ArticleListSerizlizer(serializers.ModelSerializer):
    user = CustomUserDetailSerializer()
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)  # 추가

    class Meta:
        model = Board
        fields = ('id', 'title', 'content', 'created_at', 'user', 'comment_count')  # comment_count 추가

class ArticleSerializer(serializers.ModelSerializer):
    user = CustomUserDetailSerializer(read_only=True)
    comment_set = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Board
        fields = ('id', 'title', 'content', 'created_at', 'user', 'comment_set', 'comment_count')

    def get_comment_set(self, obj):
        comments = Comment.objects.filter(board=obj)
        return CommentListSerializer(comments, many=True).data

    def get_comment_count(self, obj):
        return Comment.objects.filter(board=obj).count()

class CommentListSerializer(serializers.ModelSerializer) :
    class UserNameSerializer(serializers.ModelSerializer) :
        class Meta :
            model = User
            fields = ('name',)
    
    user = UserNameSerializer(read_only=True)

    class Meta :
        model = Comment
        fields = ('comment', 'user',)


class CommentSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Comment
        fields = '__all__'
        read_only_fields = ('board', 'user',)