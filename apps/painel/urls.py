from django.urls import include, path
from . import views

urlpatterns = [
    path('criar_post/', views.criar_post, name='criar_post'),
]