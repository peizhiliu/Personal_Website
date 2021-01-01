# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.defaults import HttpResponseNotFound

from .forms import PostForm
from .models import Post

def index(request):
    return render(request, 'blog/index.html')

def post(request, pk, slug=None):
    
    return render(request, 'blog/index.html')

@login_required
def edit(request, pk=None, slug=None):
    if pk == None:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('blog')
        else:
            form = PostForm()
        return render(request, 'blog/edit.html', {'form':form})
        
    else:
        posts = Post.objects.filter(pk=pk)  
        if (posts.exists() and slug == None) or (posts.exists() and slug == posts[0].slug):
            post = Post.objects.get(pk=pk)
            if request.method == 'POST':
                form = PostForm(request.POST, instance=post)
                if form.is_valid():
                    form.save()
                    return redirect('blog')
            else:
                form = PostForm(instance=post)
            return render(request, 'blog/edit.html', {'form':form})
        else:
            return HttpResponseNotFound("<h1>404 Page Not Found</h1>")