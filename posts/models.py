from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Model related to owner, User instance.
    """
    category_choices = [
            ('did_you_know', 'Did you know'),
            ('tips_and_how_tos', 'Tips and how tos'),
            ('fun_posts', 'Fun posts'),
            ('recommendations', 'Recommendations'),
            ('other', 'Other')
        ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../pin_default_iicvjx', blank=True
    )
    category = models.CharField(
        max_length=50,
        choices=category_choices,
        default='none'
        )
    created_on = models.DateTimeField(auto_now=True)
    last_edit = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'
