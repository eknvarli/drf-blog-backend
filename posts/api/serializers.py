from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','author','content','draft','created_at','image','slug')

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')