# models.py

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class UserProfile(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True,null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USER_TYPES = (
        ('friend', 'Friend'),
        ('spouse', 'Spouse'),
        ('other', 'Other'),
    )
    user_type = models.CharField(choices=USER_TYPES, max_length=10, default='other')

    objects = UserProfileManager()
    EMAIL_FIELD = 'email'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    
class Photo(models.Model):
    userUpload = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload/')
    approved = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'photo']

class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class UploadedExcel(models.Model):
    file = models.FileField(upload_to='uploaded_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)