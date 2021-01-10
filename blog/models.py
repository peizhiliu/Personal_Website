# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return "{}".format(self.name)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='posts')
    slug = models.SlugField(default='')
    public = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return "Post: {}, date={}, public={}".format(self.title, self.date, self.public)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', max_length=10000, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    email = models.EmailField()
    ip = models.GenericIPAddressField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, related_name='replies', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "Comment: author={}, post={}".format(self.author, self.post.title)