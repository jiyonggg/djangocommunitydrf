from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField()
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateField(auto_now_add=True)
    comment = models.CharField()