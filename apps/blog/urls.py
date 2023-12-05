from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detalhes/<int:id>/', views.detalhes_post, name='detalhes')
]