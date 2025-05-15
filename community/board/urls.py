from django.urls import path
from .views import *

app_name = 'board'

urlpatterns = [
    path('', get_all_post, name='getallpost'),
    path('post/create/', write_post, name='writepost'),
    path('post/detail/<int:pk>/', get_a_post, name='getapost'),
    path('post/update/<int:pk>/', update_post, name='updatepost'),
    path('post/delete/<int:pk>/', delete_post, name='deletepost'),
    path('comment/create/<int:pk>/', write_comment, name='writecomment'),
    path('comment/list/<int:pk>/', get_comments, name='getcomments'),
]