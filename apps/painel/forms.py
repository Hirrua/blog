from django import forms
from apps.blog.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author','title', 'description', 'image']