from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import uuid

class EmailOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=now)
    is_verified = models.BooleanField(default=False)
