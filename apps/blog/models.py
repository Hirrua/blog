from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Post(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='imagens/')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title