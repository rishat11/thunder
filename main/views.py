from rest_framework import viewsets
from rest_framework.response import Response

from .models import UserPhoto
from .models import UserProfile
from .serializers import UserPhotoSerializer, UserProfileSerializer


class UserPhotoView(viewsets.ModelViewSet):
    serializer_class = UserPhotoSerializer
    queryset = UserPhoto.objects.all()


class UserProfileView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer

    def list(self, request, *args, **kwargs):
        return Response(self.get_serializer(UserProfile.objects.prefetch_related('photos').first()).data)
