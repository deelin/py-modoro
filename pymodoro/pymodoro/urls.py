"""pymodoro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'tasks.views.home', name='home'),

    # User Accounts
    url(r'^create_user$', 'tasks.views.create_user', name='create_user'),
    url(r'^login$', 'django.contrib.auth.views.login', name='login', kwargs={
        'template_name': 'tasks/home.html',
    }),
    url(r'^logout$', 'django.contrib.auth.views.logout', name='logout', kwargs={
        'next_page': 'home',
    }),

    # Tasks
    url(r'^tasks/$', 'tasks.views.list_tasks', name='list'),
    url(r'^tasks/new$', 'tasks.views.create_task', name='create'),
    url(r'^tasks/(?P<task_id>[0-9]+)/$', 'tasks.views.get_task', name='get'),
    url(r'^tasks/(?P<task_id>[0-9]+)/update$', 'tasks.views.update_task', name='update'),
    url(r'^tasks/(?P<task_id>[0-9]+)/delete$', 'tasks.views.delete_task', name='delete'),

    # Timers
]
