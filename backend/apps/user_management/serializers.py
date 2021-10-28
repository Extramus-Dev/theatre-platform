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
        email = user_data['email']
        fn = user_data['first_name']
        ln = user_data['last_name']
        date_birth = user_data['date_birth']
        pw = user_data['password']

        return ViewerProfile.objects.create_viewer(
            User.objects.create_user(
                email=email,
                first_name=fn,
                last_name=ln,
                date_birth=date_birth,
                password=pw
            )
        )


class ContentCreatorSerializer(serializers.Serializer):
    user = UserSerializer()

    class Meta:
        model = ContentCreatorProfile
        fields = ['user']
