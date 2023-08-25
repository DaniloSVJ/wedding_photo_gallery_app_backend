from rest_framework import serializers
from rest_framework import exceptions
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainSerializer


from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Photo, Comment,Like,UserProfile,UploadedExcel
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

import pandas as pd


User = get_user_model()


def validateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

class RegisterSerializer(serializers.ModelSerializer):
    user_type = serializers.ChoiceField(choices=UserProfile.USER_TYPES)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'user_type')

    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, user_type=user_type)
        return user
    
class PhotoSerializer(serializers.ModelSerializer):
    userUpload = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Photo
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'photo', 'created_at']        



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = get_user_model().EMAIL_FIELD

    def validate(self, attrs):
        attrs[self.username_field] = attrs.pop('email')
        return super().validate(attrs)



class UploadedExcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedExcel
        fields = '__all__'

    def perform_create(self, serializer):
        instance = serializer.save()
        process_excel_file(instance.file.path)

def process_excel_file(file_path):
    df = pd.read_excel(file_path)

    for index, row in df.iterrows():
        email = row['email']
        username = row['username']
    
    
        if not email or not username:
            continue  # ou lidar com        