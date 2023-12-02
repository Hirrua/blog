from django.contrib.auth.decorators import login_required
from django.urls import reverse
from apps.blog.models import Post
from django.shortcuts import get_object_or_404, redirect
from apps.blog.models import Post
from .forms import PostForm
from django.shortcuts import render

#CRUD

@login_required()
def painel(request):
    return render(request, 'painel/painel.html')

@login_required()
def criar_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            #post = request.user
            #post.save()
            form.save()
            return redirect('post_list')
            #return render(request, 'painel.html')
    else:
        form = PostForm()
    #posts = Post.objects.filter(author=request.user)
    return render(request, 'painel/post_forms.html',  {"form": form, })
        

@login_required()
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES, instance=post)
    if form.is_valid():
        form.save()
        return redirect('detalhes', id=post.id)
    return render(request, 'painel/post_forms.html',  {"form": form, })

@login_required()
def deletar_post():
    pass
    