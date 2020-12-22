# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='about')
    greeting = models.TextField()
    description = models.TextField()

    def __str__(self):
        return '{}\'s profile'.format(str(self.user))
    
class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    class SkillArea(models.TextChoices):
        LANGUAGE = 'LG', 'language'
        SOFTWARE = 'SO','software'
    area = models.CharField(max_length=2, choices=SkillArea.choices, default=SkillArea.LANGUAGE)
    
    skill = models.CharField(max_length=255)
    proficency = models.IntegerField()
    
    def __str__(self):
        return '{}: {} in {}'.format(self.skill, self.proficency, self.area)

class Link(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    medium = models.CharField(max_length=255)
    address = models.URLField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.medium, self.address)

