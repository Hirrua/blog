from django.contrib.auth.decorators import login_required
from django.urls import reverse
from apps.blog.models import Post
from django.shortcuts import redirect
from apps.blog.models import Post
from .forms import PostForm
from django.shortcuts import render

@login_required(login_url='/login/')
def painel(request):
    if request.user.is_superuser:

        posts = Post.objects.filter(author=request.user)
        return render(request, 'painel/painel.html', {'posts': posts})
    else: 
        return redirect('home')  

@login_required(login_url='/login/')
def criar_post(request):

    if request.user.is_superuser:

        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)

            if form.is_valid():
                form.save(commit=False)
                form.save()
                return redirect('painel')
        else:
            form = PostForm()
        return render(request, 'painel/post_forms.html', {"form": form})
    else:
        return redirect('home')
        
@login_required(login_url='/login/')
def editar_post(request, id):   
    if request.user.is_superuser:

        post = Post.objects.get(id=id)
        form = PostForm(request.POST or None, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('painel')
        
        return render(request, 'painel/post_forms.html',  {"form": form})
    
    else:
        return redirect('home')

@login_required(login_url='/login/')
def deletar_post(request, id):
    if request.user.is_superuser:

        post = Post.objects.get(id=id)
        post.delete()
        return redirect('painel')
    else:
        return redirect('home')
