from rest_framework import serializers
from .models import User, ViewerProfile, ContentCreatorProfile


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=128)
    date_birth = serializers.DateField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'date_birth', 'password']


class ViewerSerializer(serializers.Serializer):
    user = UserSerializer()

    class Meta:
        model = ViewerProfile
        fields = ['user']


class ContentCreatorSerializer(serializers.Serializer):
    user = UserSerializer()

    class Meta:
        model = ContentCreatorProfile
        fields = ['user']
