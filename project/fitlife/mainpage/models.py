from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userInfo(models.Model):
  age = models.IntegerField()
  birthday = models.DateField()
  height = models.FloatField()
  weight = models.FloatField()
  user = models.ForeignKey(User, on_delete = models.CASCADE)