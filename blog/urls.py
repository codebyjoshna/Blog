from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserViewSet
from django.urls import include, path

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]