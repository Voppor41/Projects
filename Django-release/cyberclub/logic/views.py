from allauth.socialaccount.providers.dummy.views import authenticate
from django.shortcuts import render
from .serializers import *
from rest_framework import status, generics, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from.models import Users


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

def dota_page(request):
    return render(request, "html-templates/dota_page.html", menu())

def cs2_page(request):
    return render(request, "html-templates/cs2_page.html", menu())

def register_page(request):
    return render(request, 'html-templates/register.html')

def login_page(request):
    return render(request, 'html-templates/login.html')

class RegisterView(generics.CreateAPIView):
    queryset = Users.objects.all()
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

class LoginView(views.APIView):
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        print("Received data:", request.data)
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request=request, username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Login successful",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }, status=status.HTTP_200_OK)

        return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)