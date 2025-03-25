from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from logic.views import RegisterView, club_page, team_page, main_page
from frontend.views import register_page

urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),

    # Главные страницы
    path('', main_page, name='main_page'),
    path('club_page/', club_page, name='club_page'),
    path('team_page/', team_page, name='team_page'),

    # Фронтенд страницы
    path('register/', register_page, name='register_page'),  # HTML-страница регистрации
    path('frontend/', include('frontend.urls')),  # Подключаем маршруты фронтенда (если нужно)

    # API маршруты
    path('api/register/', RegisterView.as_view(), name='register_api'),  # Маршрут для API регистрации
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

