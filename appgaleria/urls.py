from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhotoViewSet, CommentViewSet
from .views import LikeViewSet
from .views import UserCreate

router = DefaultRouter()
router.register(r'photos', PhotoViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreate.as_view(), name='account-create'),

]
