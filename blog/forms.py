from django import forms
from .models import Tag, Post, Comment
from django.utils.translation import ugettext as _

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tags', 'public']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']
        labels = {
            'author': 'Name',
            'body': 'Comment'
        }
    