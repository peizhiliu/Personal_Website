# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Profile, Skill, Link

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'picture', 'greeting', 'description')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('profile', 'area', 'skill', 'proficency')

class LinkAdmin(admin.ModelAdmin):
    list_display = ('profile', 'medium', 'address')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Link, LinkAdmin)
