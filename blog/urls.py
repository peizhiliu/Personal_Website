from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('tag/<str:name>', views.index, name='tag'),
    path('post/<int:pk>/<slug:slug>', views.post, name='post'),
    path('post/<int:pk>', views.post),
    path('edit/<int:pk>/<slug:slug>', views.edit, name='edit'),
    path('edit/<int:pk>', views.edit),
    path('edit', views.edit, name='create')
]