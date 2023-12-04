from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required 
from django.utils import timezone
from django.urls import path
from .models import Post
from . import views

#funão listar -> livre sem login
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def detlhes_post(request, id):
    posts = Post.objects.get(id=id)
    return render(request, 'blog/detalhes_posts.html', {'posts': posts})
