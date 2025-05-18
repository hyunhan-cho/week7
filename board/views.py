from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .serializers import (
    PostListSerializer,
    PostResponseSerializer,
    PostDetailSerializer,
    CommentRequestSerializer,
    CommentResponseSerializer,
)

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.order_by('-created_at')
        serializer = PostResponseSerializer(posts, many=True)  
        return Response(serializer.data)

    serializer = PostListSerializer(data=request.data)  
    if serializer.is_valid():
        post = serializer.save()
        resp = PostResponseSerializer(post)  
        return Response(resp.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'GET':
        serializer = PostDetailSerializer(post) 
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostListSerializer(post, data=request.data)  
        if serializer.is_valid():
            post = serializer.save()
            resp = PostDetailSerializer(post)  
            return Response(resp.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)  
    serializer = CommentRequestSerializer(data=request.data)  
    if serializer.is_valid():
        new_comment = serializer.save(post=post)
        response_serializer = CommentResponseSerializer(new_comment)  
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_comments(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.order_by('-created_at')
    serializer = CommentResponseSerializer(comments, many=True)  
    return Response(serializer.data)