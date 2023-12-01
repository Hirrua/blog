from django.contrib.auth.decorators import login_required
from apps.blog.models import Post
from django.shortcuts import redirect
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
            form = form.save(commit=False)
            form.save()
            return redirect('post_list')
            #return render(request, 'painel.html')
    else:
        form = PostForm()
    return render(request, 'painel/post_forms.html', {"form": form})
        

@login_required()
def editar_post():
    pass

@login_required()
def deletar_post():
    pass
    