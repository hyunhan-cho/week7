from django.urls import path
from .views import post_list, post_detail, create_comment, get_comments

urlpatterns = [
    # 게시글 관련
    path('board/list/', post_list, name='post-list'), #get
    path('board/create/', post_list, name='post-create'), # psot
    path('board/detail/<int:pk>/', post_detail, name='post-detail'), #get 상세조회하는거 
    path('board/update/<int:pk>/', post_detail, name='post-update'),
    path('board/delete/<int:pk>/', post_detail, name='post-delete'),

    # 댓글 관련
    path('board/comment/create/<int:post_id>/', create_comment, name='comment-create'),
    path('board/comment/list/<int:post_id>/', get_comments, name='comment-list'),
]