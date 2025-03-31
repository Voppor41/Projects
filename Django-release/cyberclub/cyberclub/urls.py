from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from logic.views import *


urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),

    # Главные страницы
    path('', main_page, name='main_page'),
    path('club_page/', club_page, name='club_page'),
    path('team_page/', team_page, name='team_page'),
    path('dota_page/', cs2_page, name='dota_page'),
    path('cs2_page/', cs2_page, name='cs2_page'),
    path('register/', register_page, name='register_page'),  # HTML-страница регистрации
    path('login/', login_page, name='login_page'),

    # API маршруты
    path('api/register/', RegisterView.as_view(), name='register_api'),  # Маршрут для API регистрации
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

