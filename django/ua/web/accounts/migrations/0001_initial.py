# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAgent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agent', models.CharField(default=b'PC', max_length=30, verbose_name='User Agent')),
                ('key', models.CharField(unique=True, max_length=40, verbose_name='User Agent Header MD5 Hash', db_index=True)),
                ('header', models.CharField(max_length=512, verbose_name='User Agent Header')),
                ('users', models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
                'ordering': ['agent', 'header'],
                'verbose_name': 'User Agent',
                'verbose_name_plural': 'User Agents',
            },
            bases=(models.Model,),
        ),
    ]
