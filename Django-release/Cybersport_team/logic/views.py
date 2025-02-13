from http.client import responses
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import *
from django.shortcuts import render
from .forms import RegisterForm, LoginForm

def menu_context():
    return {
        'main': 'Главная',
        'team': 'Команда',
        'club': 'О клубе',
        'blog': 'Блог'
    }

def main_page(request):
    context = {
        'main': 'Главная',
        'team': 'Команда',
        'club': 'О клубе',
        'blog': 'Блог',
        'shop': 'Магазин'
    }
    return render(request, 'html-templates/main_page.html', context)

def team_page(request):
    context = {
        'cs2': 'CS2',
        'dota': 'DOTA 2',
        'main': 'Главная',
        'team': 'Команда',
        'club': 'О клубе',
        'blog': 'Блог',
    }
    return render(request, 'html-templates/team_page.html', context)

def club_page(request):
    context = {
        'main': 'Главная',
        'team': 'Команда',
        'club': 'О клубе',
        'blog': 'Блог',
    }
    return render(request, 'html-templates/club_page.html', context)


def blog_page(request):
    context = {
        'main': 'Главная',
        'team': 'Команда',
        'club': 'О клубе',
        'blog': 'Блог',
    }
    return render(request, 'html-templates/blog.html', context)

def dota_page(request):
    context = {
        'main': 'Главная',
        'team': 'Команда',
        'club': 'О клубе',
        'blog': 'Блог',
    }
    return render(request, 'html-templates/dota_page.html', context)

def cs2_page(request):
    context = {
        'main': 'Главная',
        'team': 'Команда',
        'club': 'О клубе',
        'blog': 'Блог',
    }
    return render(request, 'html-templates/cs2_page.html', context)





