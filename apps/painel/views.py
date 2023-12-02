from django.contrib.auth.decorators import login_required
from django.urls import reverse
from apps.blog.models import Post
from django.shortcuts import get_object_or_404, redirect
from apps.blog.models import Post
from .forms import PostForm
from django.shortcuts import render

@login_required(login_url='/login/')
def painel(request):
    posts = Post.objects.all()
    #posts = Post.objects.filter(author=request.user)
    return render(request, 'painel/painel.html', {'posts': posts})

@login_required(login_url='/login/')
def criar_post(request):
    if request.method == "POST":
        #if request.user.is_superuser:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('painel')
    else:
        form = PostForm()
    return render(request, 'painel/post_forms.html', {"form": form})
        
@login_required(login_url='/login/')
def editar_post(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES, instance=post)
    if form.is_valid():
        form.save()
        return redirect('detalhes', id=post.id)
    return render(request, 'painel/post_forms.html',  {"form": form})

@login_required(login_url='/login/')
def deletar_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse('painel'))
