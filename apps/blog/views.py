from django.shortcuts import redirect, render
from .models import Post
from .forms import ComentarioForm

#função listar -> livre sem login
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def detalhes_post(request, id):
    post = Post.objects.get(id=id)
    comentarios = post.comentarios.all()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.nome = request.user.username
            comentario.save()
            return redirect('detalhes', id=post.id)

    else:
        form = ComentarioForm()

    return render(request, 'blog/detalhes_posts.html', {'post': post, 'comentarios': comentarios, 'form': form})
