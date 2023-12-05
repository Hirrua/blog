from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='imagens/')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title
    
class Comentario(models.Model):

    post = models.ForeignKey(Post, related_name="comentarios",on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    comentario = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.nome