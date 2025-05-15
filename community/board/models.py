from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField()
    body = models.TextField()
    created_at = models.DateField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateField()
    comment = models.CharField()