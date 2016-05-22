from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse

import models


@login_required
def profile(request):
    ua = models.UserAgent.get_ua(
        request.META.get('HTTP_USER_AGENT', 'N/A'),
        request.user)

    return TemplateResponse(
        request,
        'registration/profile.html',
        dict(request=request, ua=ua, ))
