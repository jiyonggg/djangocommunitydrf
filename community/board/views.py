from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Post, Comment
from .serializers import *

# Create your views here.

@api_view(['GET'])
def get_all_post(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = AllPostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def write_post(request):
    if request.method == 'POST':
        serializer = PostEditSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_a_post(request, pk):
    if request.method == 'GET':
        try:
            post = Post.objects.get(pk=pk)
            serializer = DetailPostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_post(request, pk):
    if request.method == 'PUT':
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostEditSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_post(request, pk):
    if request.method == 'DELETE':
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def write_comment(request, pk):
    if request.method == 'POST':
        try:
            serializer = CommentSerializer(data=request.data)
            target = Post.objects.get(pk=pk)
            if serializer.is_valid():
                serializer.save(post=target)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_comments(request, pk):
    if request.method == 'GET':
        comments = Comment.objects.filter(post__exact=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)