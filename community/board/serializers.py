from rest_framework import serializers

from .models import Post, Comment

class AllPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body']

class PostEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'created_at']

class CommentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment']

class CommentViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'created_at', 'comment']

class DetailPostSerializer(serializers.ModelSerializer):
    comments = CommentViewSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'created_at', 'comments']