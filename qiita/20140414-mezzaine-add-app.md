

(v16)hdknr@wzy:~/ve/v16/src/sites/simple$ python manage.py startapp quiz

(v16)hdknr@wzy:~/ve/v16/src/sites/simple$ mkdir -p quiz/templates/quiz
(v16)hdknr@wzy:~/ve/v16/src/sites/simple$ vi quiz/templates/quiz/default.html

(v16)hdknr@wzy:~/ve/v16/src/sites/simple$ more quiz/templates/quiz/default.html 

{% extends 'base.html' %}

{% block title %}Quiz Default{% endblock %}

{% block main %}
<p>
Welcome to Quiz application.
</p>
{% endblock %}

(v16)hdknr@wzy:~/ve/v16/src/sites/simple$ more quiz/views.py
# -*- coding: utf-8 -*-
from django import template
from django.shortcuts import render_to_response


def default(request):
    return render_to_response(
        'quiz/default.html',
        {}, context_instance=template.RequestContext(request),)
        

(v16)hdknr@wzy:~/ve/v16/src/sites/simple$ more quiz/urls.py
from django.conf.urls import patterns, url
from views import default

urlpatterns = patterns(
    '',
    url(r'', default, name="quize_default1"),
)


追加
(v16)hdknr@wzy:~/ve/v16/src/sites/simple$ more urls.py

urlpatterns += patterns(
    '',
    url('quiz', include('%s.urls' % 'quiz')),
    
    
(v16)hdknr@wzy:~/ve/v16/src/sites/simple$ more settings.py

INSTALLED_APPS += (
    'quiz',
)
    



        