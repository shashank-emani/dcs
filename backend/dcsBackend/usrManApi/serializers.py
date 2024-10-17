from rest_framework import serializers
from .models import CustomUser, UserProfile

## Serializer for the UserProfile model

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address', 'date_of_birth']


 # Serializer for the CustomUser model       

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'profile']

