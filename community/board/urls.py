from django.urls import path
from .views import *

app_name = 'board'

urlpatterns = [
    path('', all_post, name='getallpost'),
    path('post/create/', all_post, name='writepost'),
    path('post/detail/<int:pk>/', detail_post, name='getapost'),
    path('post/update/<int:pk>/', detail_post, name='updatepost'),
    path('post/delete/<int:pk>/', detail_post, name='deletepost'),
    path('comment/create/<int:pk>/', all_comment, name='writecomment'),
    path('comment/list/<int:pk>/', all_comment, name='getcomments'),
]