# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.defaults import HttpResponseNotFound
from django.core.paginator import Paginator

from .forms import PostForm, CommentForm
from .models import Post, Comment, Tag

def index(request, name=None):
    if name:
        posts = Post.objects.filter(tags__name=name)
        if not posts.exists():
            return HttpResponseNotFound("<h1>404 Page Not Found</h1>") 
    else:
        posts = Post.objects.filter(public=True)
    posts = posts.order_by("-date")
    paginator = Paginator(posts, 8)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    tags = Tag.objects.all().order_by('name')

    context = {
        'page':page,
        'tags':tags,
    }
    return render(request, 'blog/index.html', context=context)

def get_client_ip(request):
    http_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
    if http_forwarded:
        return http_forwarded.split(',')[0]
    else:
        return request.META.get('REMOTE_ADDR')

def post(request, pk, slug=None):
    posts = Post.objects.filter(pk=pk)
    if ((posts.exists() and slug == None) or (posts.exists() and slug == posts[0].slug)) and posts[0].public:
        if request.method == 'POST':
            form = CommentForm(request.POST, label_suffix='')
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = Post.objects.get(pk=pk)
                comment.ip = get_client_ip(request)
                try:
                    parent_id = int(request.POST.get('parent_pk'))
                except:
                    parent_id = None
                
                if parent_id:
                    comment.parent = Comment.objects.get(pk=parent_id)
                comment.save()
                
                return redirect('post', pk=comment.post.pk, slug=comment.post.slug)
        else:
            form = CommentForm(label_suffix='')

        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=post, parent=None).order_by('-date')
        context = {
            'post':post,
            'comments': comments,
            'form': form,
        }
        return render(request, 'blog/post.html', context=context)
    else:
        return HttpResponseNotFound("<h1>404 Page Not Found</h1>") 



@login_required
@user_passes_test(lambda u: u.groups.filter(name='admin').exists())
def edit(request, pk=None, slug=None):
    if pk == None:
        if request.method == 'POST':
            form = PostForm(request.POST, label_suffix='')
            if form.is_valid():
                post = form.save()
                return redirect('post', pk=post.pk, slug=post.slug)
        else:
            form = PostForm(label_suffix='')
        context = {
            'form':form,
            'title':'New Post'
        }
        return render(request, 'blog/edit.html', context=context)
        
    else:
        posts = Post.objects.filter(pk=pk)  
        if (posts.exists() and slug == None) or (posts.exists() and slug == posts[0].slug):
            post = Post.objects.get(pk=pk)
            if request.method == 'POST':
                form = PostForm(request.POST, instance=post, label_suffix='')
                if form.is_valid():
                    post = form.save()
                    return redirect('post', pk=post.pk, slug=post.slug)
            else:
                form = PostForm(instance=post, label_suffix='')
            title = 'Edit Post {}: {}'.format(pk, post.title)
            context = {
                'form':form,
                'title':title
            }
            return render(request, 'blog/edit.html', context=context)
        else:
            return HttpResponseNotFound("<h1>404 Page Not Found</h1>")