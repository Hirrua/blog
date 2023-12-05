from django.shortcuts import render
from .models import Post, Comentario

#função listar -> livre sem login
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def detalhes_post(request, id):
    posts = Post.objects.get(id=id)
    comments = Comentario.objects.all()
    return render(request, 'blog/detalhes_posts.html', {'posts': posts, 'comments': comments})
