from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now, verbose_name="Create date")
