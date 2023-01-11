from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.text

