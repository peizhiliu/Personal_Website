# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Tag, Post, Comment


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date', 'update')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'date')

admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
