from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.utils import timezone
from django.urls import path
from .models import Post
from . import views

#função criar
#função editar
#função deletar
#função comentar

#funão listar -> livre sem login
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required()
def criar_post():
    pass

@login_required()
def editar_post():
    pass

@login_required()
def deletar_post():
    pass
    