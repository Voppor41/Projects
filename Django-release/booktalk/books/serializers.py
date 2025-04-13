from rest_framework import serializers
from .models import Book
#from reviews.serializer import ReviewSerializer

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = '__all__'

"""class BookDetaileSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'description', 'cover', 'reviews']

"""