from rest_framework import viewsets, permissions
from .models import Photo, Comment, Like,UserProfile,UploadedExcel
from .serializers import PhotoSerializer,LikeSerializer, CommentSerializer, RegisterSerializer,CustomTokenObtainPairSerializer,UploadedExcelSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import generics
from django.contrib.auth.models import User

from .permissions import IsCoupleOrReadOnly

class UserCreate(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny, )
    
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()  # pegando todas as fotos, para que o casal possa ver as não aprovadas também
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user_profile = self.request.user
        serializer.save(userUpload=user_profile)

    def perform_update(self, serializer):
        user_profile = self.request.user
        if 'approved' in serializer.validated_data:
            if user_profile.user_type not in ['friend', 'spouse']:
                raise serializer.ValidationError("Você não tem permissão para aprovar fotos.")
        serializer.save(userUpload=user_profile)

    def get_queryset(self):
        user_profile = self.request.user

        if user_profile.is_superuser or user_profile.user_type in ['friend', 'spouse']:
            return Photo.objects.all()
    
  
        return Photo.objects.filter(approved=True)
    
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
   
  

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
  


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UploadedExcelViewSet(viewsets.ModelViewSet):
    queryset = UploadedExcel.objects.all()
    serializer_class = UploadedExcelSerializer