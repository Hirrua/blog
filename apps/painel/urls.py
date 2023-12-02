from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.painel, name='painel'),
    path('criar_post/', views.criar_post, name='criar_post'),
    path('editar_post/<int:id>/', views.editar_post, name='editar_post'),   
    path('deletar_post/<int:id>/', views.deletar_post, name='deletar_post')
]