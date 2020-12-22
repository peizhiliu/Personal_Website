# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Project, Image
from .connect_git import update_projects

def index(request):
    user = User.objects.filter(first_name='Peizhi', last_name='Liu')[0]
    update_projects(user)
    
    context_projects = []
    projects = Project.objects.filter(user=user).order_by('-lastupdate')
    '''for project in projects:
        context_project = {
            'url': project.url,
            'title': project.title,
            'description': project.description,
            'lastupdate': project.lastupdate,
            'technologies': [{'name': tech.name, 'color':tech.color} for tech in project.technology.all()],
            'images':  [image.image for image in Image.objects.filter(project=project)]
        }
        context_projects.append(context_project)'''

    context = {'projects': projects}
    return render(request, 'projects/index.html', context=context)
