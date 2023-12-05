from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as django_login
from django.shortcuts import render, redirect

def registrar(request):
    if request.method == 'GET':
        return render(request, "authuser/register.html")
    else:
        usuario = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=usuario).first()
        
        if user:
            return HttpResponse("Usuário já cadastrado!!")
        
        user = User.objects.create_user(username=usuario, password=senha)
        user.save()

        user = authenticate(request, username=usuario, password=senha)
        django_login(request, user)

        return redirect('home')


#função login
def login(request):
    if request.method == 'GET':
        return render(request, "authuser/login.html")
    else: 
        usuario = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario, password=senha)

        if user:
            django_login(request, user)
            if request.user.is_superuser:
                next_path = request.GET.get('next', 'painel')
                return redirect(next_path)
            else:
                next_path = request.GET.get('next', 'home')
                return redirect(next_path)
        else:
            return HttpResponse("Credenciais inválidas!!")

@login_required(login_url='/login/')
def sair(request):
    logout(request)
    return redirect('home')