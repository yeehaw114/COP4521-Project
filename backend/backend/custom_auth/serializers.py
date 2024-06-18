from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth import get_user_model
from backend.user.models import User, Role
from backend.user.serializers import UserSerializer


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, max_length=128)
    role = serializers.ChoiceField(choices=Role.ROLE_CHOICES, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']

    def create(self, validated_data):
        role_name = validated_data.pop('role')
        try:
            role = Role.objects.get(name=role_name)
        except ObjectDoesNotExist:
            raise serializers.ValidationError(f"Role {role_name} does not exist")
        try:
            user = User.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user = User.objects.create_user(**validated_data)
            user.roles.add(role)
        return user

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data['access'] = str(refresh.access_token)
        data['refresh'] = str(refresh)
        data['user'] = UserSerializer(self.user).data

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data