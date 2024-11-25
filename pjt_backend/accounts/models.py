from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here..
# class Job(models.Model):
#     job_name = models.CharField(max_length=100)

class User(AbstractUser):
    username = None
    name = models.CharField(max_length=100, default='Anonymous')
    email = models.EmailField(unique=True)
    age = models.IntegerField() 
    gender = models.CharField(max_length=10)
    birthday = models.DateField()
    address = models.TextField()
    servay_yn = models.BooleanField(default=False)
    # job_id = models.ForeignKey(Job, on_delete=models.SET_DEFAULT, default=1)
    job = models.CharField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chathistory')
    sender = models.CharField(max_length=100)
    content = models.TextField()