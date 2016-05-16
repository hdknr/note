from __future__ import unicode_literals

from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        from app.celery import app as celery_app   # NOQA
