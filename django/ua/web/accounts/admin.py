from django.contrib import admin
from django.db.models import get_app, get_models
from django.db.models.manager import Manager
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin


import models


class UserAgentAdmin(admin.ModelAdmin):
    add_exclude = ('users',)
    edit_exclude = ('users',)
    list_display = tuple(
        [f.name for f in models.UserAgent._meta.fields
         if f.name not in ['key']]
    ) + ('users_count',)
    list_filter = ('agent', )
    readonly_fields = ('ua_users', )

    def add_view(self, *args, **kwargs):
        self.exclude = getattr(self, 'add_exclude', ())
        return super(UserAgentAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.exclude = getattr(self, 'edit_exclude', ())
        return super(UserAgentAdmin, self).change_view(*args, **kwargs)

    def users_count(self, obj):
        if not obj.users.exists():
            return '0'

        uri = reverse("admin:%s_changelist" % obj.users.model._meta.db_table)
        query = "?useragent__id__exact=%d" % (obj.id)
        return mark_safe(
            u"<a href='%s'>%d Users</a>" % (uri + query, obj.users.count()))

    users_count.allow_tags = True

    def ua_users(self, instance):
        try:
            return ",".join([
                mark_safe('<a href="%s">%s</a>   ' % (
                    reverse("admin:%s_change" % u._meta.db_table, args=[u.id]),
                    u.__unicode__()))
                for u in instance.users.all()])
        except:
            return "errors"

    ua_users.short_description = "UserAgent Users"
    ua_users.allow_tags = True


for model in get_models(get_app(__name__.split('.')[-2:][0])):
    name = "%sAdmin" % model.__name__

    admin_class = globals().get(name, None)
    if admin_class is None:
        params = dict(
            list_display=tuple([f.name for f in model._meta.fields]),)
        admin_class = type(
            "%sAdmin" % model.__name__,
            (admin.ModelAdmin,),
            params,
        )

    admin.site.register(model, admin_class)


def link_to_relation(self, obj, field=""):
    fobj = obj and getattr(obj, field, None)

    if fobj is None:
        return "No Link"

    if issubclass(fobj.__class__, Manager):
        fobj = fobj.all()
    else:
        fobj = [fobj, ]

    return mark_safe("<br/>".join([
        '<a href="%s">%s</a>' % (
            reverse("admin:%s_change" % ln._meta.db_table, args=[ln.id]),
            ln.__unicode__()
        ) for ln in fobj]))

useragent_link = lambda self, obj: link_to_relation(self, obj, "useragent_set")
useragent_link.short_description = u"User Agent"
useragent_link.allow_tags = True

UserAdmin.list_display = tuple(
    set(UserAdmin.list_display + ('useragent_link', )))
UserAdmin.useragent_link = useragent_link

UserAdmin.list_filter = UserAdmin.list_filter + ('useragent__agent',)
