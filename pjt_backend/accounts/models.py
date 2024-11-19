from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here..
class Job(models.Model):
    job_name = models.CharField(max_length=100)

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    birthday = models.DateField()
    address = models.TextField()
    servay_yn = models.BooleanField(default=False)
    job_id = models.ForeignKey(Job, on_delete=models.SET_DEFAULT, default=0)
