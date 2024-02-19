from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.generics import CreateAPIView

from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.serializers import PostCreateSerializer

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    lookup_field = 'slug'


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)