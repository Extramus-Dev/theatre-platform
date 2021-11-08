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

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ViewerSerializer(serializers.Serializer):
    user = UserSerializer()

    class Meta:
        model = ViewerProfile
        fields = ['user']

    def create(self, validated_data):
        user_data = validated_data['user']

        return ViewerProfile.objects.create_viewer(
            User.objects.create_user(
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                date_birth=user_data['date_birth'],
                password=user_data['password']
            )
        )


class ContentCreatorSerializer(serializers.Serializer):
    user = UserSerializer()

    class Meta:
        model = ContentCreatorProfile
        fields = ['user']

    def create(self, validated_data):
        user_data = validated_data['user']

        return ContentCreatorProfile.objects.create_viewer(
            User.objects.create_user(
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                date_birth=user_data['date_birth'],
                password=user_data['password']
            )
        )
