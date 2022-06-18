from rest_framework import serializers

from main.models import UserProfile, UserPhoto, Like


class UserPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UserPhoto


class UserProfileSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()

    def get_photos(self, obj):
        customer_account_query = UserPhoto.objects.filter(
            user_id=obj.id)
        serializer = UserPhotoSerializer(customer_account_query, many=True)

        return serializer.data

    class Meta:
        fields = [
            'user',
            'name',
            'date_of_birth',
            'gender',
            'age',
            'height',
            'photos',
        ]
        model = UserProfile


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Like
