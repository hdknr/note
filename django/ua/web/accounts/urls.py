# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    '',
    url(r'login/$', 'django.contrib.auth.views.login'),
    url(r'profile/$', views.profile),
)
