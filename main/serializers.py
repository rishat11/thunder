from rest_framework import serializers

from main.models import UserProfile, UserPhoto


class UserPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UserPhoto


class UserProfileSerializer(serializers.ModelSerializer):
    photo = UserPhotoSerializer(source='photos')

    class Meta:
        exclude = ('location',)
        model = UserProfile
