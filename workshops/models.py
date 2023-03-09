from django.db import models
from django.contrib.auth.models import User


class Workshop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField(blank=False)
    link = models.URLField('Workshop URL', max_length=400, blank=False)
    price = models.IntegerField(null=False, blank=False)
    location = models.CharField(max_length=50)
    time = models.TimeField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.title} {self.date}'
