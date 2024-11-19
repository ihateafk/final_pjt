from django.db import models
from accounts.models import User

# Create your models here.

# 게시판 모델
class Board(models.Model) :
    title = models.TextField() # 제목
    content = models.TextField() # 내용
    created_at = models.DateField(auto_now_add=True) # 생성 날짜
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 유저 아이디

# 댓글 모델 
class Comment(models.Model) :
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)