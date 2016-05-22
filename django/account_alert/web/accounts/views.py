# Create your views here.
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.utils.timezone import now

from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import views as django_views
from django.contrib.auth import forms as django_forms
from django.core.urlresolvers import reverse
from django.views.decorators.cache import never_cache
# import models


@login_required
def profile(request):
    return TemplateResponse(
        request,
        'accounts/profile.html',
        dict(request=request), )


@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request):
    return django_views.login(
        request,
        template_name='accounts/login.html',
        redirect_field_name=django_views.REDIRECT_FIELD_NAME,
        authentication_form=django_forms.AuthenticationForm,
        current_app=None, extra_context=None)


def logout(request):
    return django_views.logout(
        request,
        next_page=reverse('accounts_login'),
        template_name='accounts/logged_out.html',
        redirect_field_name=django_views.REDIRECT_FIELD_NAME,
        current_app=None, extra_context=None)


@sensitive_post_parameters()
@csrf_protect
@login_required
def password_change(request):
    res = django_views.password_change(
        request,
        template_name='accounts/password_change.html',
        post_change_redirect=reverse('accounts_password_change_done'),
        password_change_form=django_forms.PasswordChangeForm,
        current_app=None,
        extra_context=None)

    try:
        if type(res) == HttpResponseRedirect:
            request.user.accountalert_set.filter(
                executed_at=None, url=reverse('accounts_password_change'),
            ).update(executed_at=now())

    except Exception, ex:
        print ex

    return res


@login_required
def password_change_done(request):
    return django_views.password_change_done(
        request,
        template_name='accounts/password_change_done.html',
        current_app=None,
        extra_context=None)


# @sensitive_post_parameters()
# @csrf_protect
# @login_required
# def alert(request):
#     alerts = request.user.accountalert_set.filter(
#         force=True,
#         url=request.path,
#         executed_at=None,
#         due_on__lt=now())
#
#     # formset でチェックが入ったAccountAlert を消す
#     #  ....
#
#     return TemplateResponse(
#         request,
#         'accounts/alert.html',
#         dict(request=request), )
