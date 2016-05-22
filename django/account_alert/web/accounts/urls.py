from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    '',
    url(r'^login/$',
        views.login,
        name='accounts_login'),
    url(r'^logout/$',
        views.logout,
        name='accounts_logout'),
    url(r'^profile/$',
        views.profile,
        name="accounts_profile"),
    url(r'^password/change/done/$',
        views.password_change_done,
        name='accounts_password_change_done'),
    url(r'^password/change/$',
        views.password_change,
        name='accounts_password_change'),
)
