from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post, User
from .serializers import PostSerializer, UserSerializer

# Create your views here.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
