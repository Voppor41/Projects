from .models import Users
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}



