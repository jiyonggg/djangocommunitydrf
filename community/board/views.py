from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Post, Comment
from .serializers import *

# Create your views here.

@api_view(['GET', 'POST'])
def all_post(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = AllPostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PostEditSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detail_post(request, pk):
    if request.method == 'GET':
        try:
            post = Post.objects.get(pk=pk)
            serializer = DetailPostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostEditSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def all_comment(request, pk):
    if request.method == 'GET':
        comments = Comment.objects.filter(post__exact=pk)
        serializer = CommentViewSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        try:
            write_serializer = CommentWriteSerializer(data=request.data)
            target = Post.objects.get(pk=pk)
            if write_serializer.is_valid():
                comment = write_serializer.save(post=target)
                view_serializer = CommentViewSerializer(comment)
                return Response(view_serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.status.HTTP_400_BAD_REQUEST)