from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

# Create your models here.
class CustomUser(AbstractUser, PermissionsMixin):
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # или ['username'] если всё же хочешь

    def __str__(self):
        return self.username