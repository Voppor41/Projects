from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField()
    age = models.IntegerField(blank=True)
    email = models.EmailField(unique=True, default="default@example.com")

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

class Players(models.Model):
    lastname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    fathername = models.CharField(max_length=20)
    nickname = models.CharField(max_length=100)
    statistic = models.TextField(blank=True)

class Match(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=10)
