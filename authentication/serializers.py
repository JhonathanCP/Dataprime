from rest_framework import serializers
from authentication.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'role', 'clasificaciones')

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email', 'role', 'clasificaciones')
        extra_kwargs = {'password': {'write_only': True}, 'role': {'default': 'admin'}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user