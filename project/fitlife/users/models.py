from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, default = None)
    password = models.CharField(max_length=50)
