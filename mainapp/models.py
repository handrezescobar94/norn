from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class LoginLog(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)