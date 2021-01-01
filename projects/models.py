# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Technology(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    color = models.CharField(max_length=10, default='ffffff')

    def __str__(self):
        return '{}: {}'.format(self.name, self.color)

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(max_length=200, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    technology = models.ManyToManyField(Technology)
    lastupdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{}\'s project: {}'.format(self.user, self.title)

class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects')
    featured = models.BooleanField(default=False)

    def __str__(self):
        return '{}. Image: {}'.format(self.project, self.image)