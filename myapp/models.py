from django.db import models
from datetime import datetime

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.BigIntegerField()
    subject=models.CharField(max_length=20)