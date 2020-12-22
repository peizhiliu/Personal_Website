# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from github import Github
from markdown2 import Markdown
from bs4 import BeautifulSoup
import pytz
import os
import wget
#from urllib.request import urlretrieve
from urllib.parse import urlparse

from django.conf import settings
from django.core.files import File

from .models import Technology, Image, Project

# call this function to update the projects from GitHub
def update_projects(user):
    git = Github(settings.GIT_TOKEN)
    repos = git.get_user().get_repos()
    for repo in repos:
        try:
            check_update(user, repo)
        except: pass

# helper function to check whether repo needs updating
def check_update(user, repo):
    url = repo.html_url
    projects = Project.objects.filter(pk=url)
    # project is already in database
    if projects.exists():
        project = projects[0]
        # project has nothing to update
        if repo.updated_at.astimezone(pytz.UTC) == project.lastupdate:
            return
        # project has something to update
        else:
            update(user, repo, project)
    # project not in database
    else:
        update(user, repo)

# this prepares the fields to be updated
def update(user, repo, project=None):
    base = 'https://raw.githubusercontent.com/'
    login = repo.owner.login
    repo_name = repo.name
    branch = 'master'


    readme = repo.get_readme().decoded_content
    readme = readme.decode('utf-8')

    url = repo.html_url
    title = parse_md(readme, header='Title')
    description = parse_md(readme, header='Description')
    technologies = Technology.objects.filter(pk__in=list(repo.get_languages().keys()))
    lastupdate = repo.updated_at
    #image_urls = [repo.get_contents(url).download_url for url in parse_img(readme)]
    image_urls = [os.path.join(base, login, repo_name, branch, url) for url in parse_img(readme)]
    image_paths = [wget.download(url, os.path.join('tmp', os.path.basename(urlparse(url).path))) for url in image_urls]
    images = [File(open(path, 'rb')) for path in image_paths]

    if project:
        write_project(project, title, description, technologies, lastupdate, images)
    else:
        project = Project(user=user, url=url)
        project.save()
        write_project(project, title, description, technologies, lastupdate, images)

# update project fields
def write_project(project, title, description, technologies, lastupdate, images):
    project.title = title
    project.description = description
    project.lastupdate = lastupdate
    
    project.technology.clear()
    for tech in technologies:
        project.technology.add(tech.pk)

    project.save()

    Image.objects.filter(project=project).delete()
    for i, image in enumerate(images):
        img = Image(project=project, featured=(not bool(i)))
        img.image.save(os.path.basename(image.name), image, save=True)
        img.save()

# assumes title is preceded by '# ' and the headers are 
# preceded by '## '
def parse_md(readme, header):
    splitted = [s.strip() for s in readme.splitlines()]
    if header == 'Title':
        title = splitted[0].split('# ')[1]
        return title
    start = splitted.index('## ' + header)
    end = start
    for i in range(start + 1, len(splitted)):
        end = i
        if '##' in splitted[i]:
            return ' '.join(splitted[start + 1: end])
    return ' '.join(splitted[start + 1: end + 1])

# get all image urls in the readme file on github
def parse_img(readme):
    md = Markdown()
    html = md.convert(readme)
    soup = BeautifulSoup(html, 'html.parser')
    return [img.get('src') for img in soup.find_all('img')]

