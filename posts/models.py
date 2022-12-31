from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Model related to owner, User instance.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../pin_default_iicvjx', blank=True
    )
    created_on = models.DateTimeField(auto_now=True)
    last_edit = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'
