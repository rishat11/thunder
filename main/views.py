from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import UserPhoto
from .models import UserProfile
from .models import Like
from .serializers import UserPhotoSerializer, UserProfileSerializer, LikeSerializer


class UserPhotoView(viewsets.ModelViewSet):
    serializer_class = UserPhotoSerializer
    queryset = UserPhoto.objects.all()


class UserProfileView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer

    def list(self, request, *args, **kwargs):
        return Response(self.get_serializer(
            UserProfile.objects.prefetch_related('userphoto_set').first()).data)


class LikeView(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        data = request.data
        Like.objects.get_or_create(
            liked_user_id=data.get('user'),
            current_user_id=request.user.userprofile.id,
            like=data.get('like'),
        )

        return Response()
