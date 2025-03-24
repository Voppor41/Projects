from django.shortcuts import render
from .serializers import *
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

# Create your views here.

def menu():
    context = {
        "main": "Главная",
        "club": "О клубе",
        "team": "Команда",
        "blog": "Блог",
    }
    return context

def menu_page(request):
    return render(request, "html-templates/menu.html", menu())

def main_page(request):
    return render(request, "html-templates/main_page.html", menu())

def club_page(request):
    return render(request, "html-templates/club_page.html", menu())

def team_page(request):
    return render(request, "html-templates/team_page.html", menu())

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
