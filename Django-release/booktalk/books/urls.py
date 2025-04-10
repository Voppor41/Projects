from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    path('', BookListCreateView.as_view, name='book-list'),
    path('<int:pk>/', BookDetailView.as_view, name='book-detail'),
]