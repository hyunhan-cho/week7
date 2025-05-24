from django.utils import timezone
from rest_framework import serializers
from .models import Post, Comment

# 게시글 생성/수정 요청용
class PostListSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Post
        fields = ['id','title', 'body']  
    
    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    
# 게시글 응답용 Serializer ㅎㅎㅎㅎ
class PostResponseSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()  

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'created_at']

    def get_created_at(self, obj):
        return timezone.localtime(obj.created_at).strftime('%Y-%m-%d')  

# 댓글 응답용 Serializer 
class CommentResponseSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'comment', 'created_at']

    def get_created_at(self, obj):
        return timezone.localtime(obj.created_at).strftime('%Y-%m-%d')

# 게시글 상세조회
class PostDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    comments = CommentResponseSerializer(many=True, read_only=True)  # 댓글 응답 Serializer 사용

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'created_at', 'comments']

    def get_created_at(self, obj):
        return timezone.localtime(obj.created_at).strftime('%Y-%m-%d')

# 댓글 작성 요청용
class CommentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment']

