from django.urls import path
from .views import post_list, post_detail, create_comment, get_comments

urlpatterns = [
    # 게시글 관련 
    # 게시글 목록 조회 (GET)
    path('board/list/', post_list, name='post-list'),
    # 게시글 생성       (POST)
    path('board/create/', post_list, name='post-create'),

   #게시글 상세 조회  
    path('board/detail/<int:pk>/', post_detail, name='post-detail'),
    # 게시글 수정      (PUT)
    path('board/update/<int:pk>/', post_detail, name='post-update'),
    # 게시글 삭제      (DELETE)
    path('board/delete/<int:pk>/', post_detail, name='post-delete'),

    # 댓글 관련
    # 댓글 작성        (POST)
    path('board/comment/create/<int:post_id>/', create_comment, name='comment-create'),
    #댓글 목록 조회   (GET)
    path('board/comment/list/<int:post_id>/', get_comments,   name='comment-list'),
]
