from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.shortcuts import render, redirect

#função login
def login(request):
    if request.method == 'GET':
        return render(request, "authuser/login.html")
    else: 
        #utilizar um form, metodo post e se email e senha estiverem OK, vai fazer um login e retornar para painel, senão volta para tela de login com erro
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            django_login(request, user)
            next_path = request.GET.get('next', 'painel')
            return redirect(next_path)
            #return HttpResponse("Logado com sucesso")
            #return render(request, 'painel/painel.html')
        else:
            return HttpResponse("ERRO")
        