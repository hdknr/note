# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.utils.timezone import now


class AccountAlertMiddleware(object):

    def process_request(self, request):
        if getattr(request, 'user', None) and request.user.is_authenticated():
            alerts = request.user.accountalert_set.filter(
                force=True,
                executed_at=None,
                due_on__lt=now()).exclude(url=request.path)

            if alerts.count() > 0:
                return HttpResponseRedirect(alerts[0].url)
