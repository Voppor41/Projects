from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField()
    age = models.IntegerField(blank=True)
    email = models.EmailField(unique=True, default="default@example.com")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
         return self.username

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Players(models.Model):
    lastname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    fathername = models.CharField(max_length=20)
    nickname = models.CharField(max_length=100)
    statistic = models.TextField(blank=True)
    photo = models.ImageField(upload_to='player_photo', null=True, blank=True)

    def __str__(self):
        return self.nickname

class Match(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    op_team = models.TextField(max_length=100, default="Unknown team")
    our_team = models.TextField(default="Polyal Suqad")
    result = models.CharField(max_length=10)

    def __str__(self):
        return self.date

