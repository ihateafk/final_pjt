from rest_framework import serializers
from .models import Board, Comment
from accounts.serializers import CustomUserDetailSerializer

class ArticleListSerizlizer(serializers.ModelSerializer) :

    user = CustomUserDetailSerializer()
    class Meta :
        model = Board
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Board
        fields = '__all__'
        read_only_fields = ('user',)