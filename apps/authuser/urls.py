from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('sair/', views.sair, name='sair'),
    path('registrar/', views.registrar, name='registrar')
]