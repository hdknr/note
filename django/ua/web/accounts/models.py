# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from ua import agent_type
import hashlib


class UserAgent(models.Model):
    agent = models.CharField(
        _(u'User Agent'),
        max_length=30, default="PC")
    key = models.CharField(
        _(u'User Agent Header MD5 Hash'),
        max_length=40, unique=True, db_index=True,)
    header = models.CharField(
        _(u'User Agent Header'),  max_length=512, )
    users = models.ManyToManyField(
        User, default=None, null=True, blank=True)

    @classmethod
    def get_ua(cls, ua_header, user=None):
        ua, created = cls.objects.get_or_create(
            key=hashlib.md5(ua_header).hexdigest())

        if created:
            ua.agent = agent_type(ua_header)
            ua.header = ua_header
            ua.save()

        if user:
            ua.users.add(user)

        return ua

    def __unicode__(self):
        return "%s(%s)" % (self.agent, getattr(self, 'id', ''))

    class Meta:
        verbose_name = _(u'User Agent')
        verbose_name_plural = _(u'User Agents')
        ordering = ['agent', 'header', ]
