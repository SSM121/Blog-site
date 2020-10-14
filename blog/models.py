from django.db import models


class Post(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_author = models.CharField(max_length=100)
    blog_content = models.TextField()
    blog_date = models.DateTimeField('date published')

class Comment(models.Model):
    blog = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=100)
    comment_email = models.EmailField()
    comment_content = models.TextField()
    comment_date = models.DateTimeField('date published')
