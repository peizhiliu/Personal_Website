# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Profile, Skill, Link

def index(request):
    user = User.objects.filter(first_name='Peizhi', last_name='Liu')[0]
    profile = Profile.objects.filter(user=user)[0]
    skills = []
    for area, _ in Skill.SkillArea.choices:
        skills.append([(getattr(skill, 'skill'), getattr(skill, 'proficency')) for skill in sorted(Skill.objects.filter(area=area), key=lambda skill: -skill.proficency)])
    context = {
        'picture': getattr(profile, 'picture'),
        'greeting': getattr(profile, 'greeting'),
        'about': getattr(profile, 'description'),
        'skills': skills,
        'email': ('Email', user.email),
        'links': [(getattr(link, 'medium'), getattr(link, 'address')) for link in sorted(Link.objects.filter(profile=profile), key=lambda link: link.medium)],
    }
    return render(request, 'about/index.html', context=context)
