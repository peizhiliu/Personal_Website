# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Technology, Project, Image

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'image')

admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Image, ImageAdmin)

