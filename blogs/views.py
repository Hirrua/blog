from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login as login_required
from django.shortcuts import render
from django.urls import path
from . import views

def cadastro(request):
        return HttpResponse('Teste')

def post_list(request):
    return render(request, 'blog/post_list.html', {})