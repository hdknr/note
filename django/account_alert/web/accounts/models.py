from django.db import models
from django.contrib.auth.models import User


class AccountAlert(models.Model):
    user = models.ForeignKey(User)
    url = models.CharField(max_length=200, db_index=True)
    text = models.TextField(null=True, default=None, blank=True)
    force = models.BooleanField(default=False)
    due_on = models.DateTimeField(null=True, blank=True, default=None)
    executed_at = models.DateTimeField(null=True, blank=True, default=None)

    class Meta:
        ordering = ['-due_on']
