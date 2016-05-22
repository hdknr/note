from django.contrib import admin
from django.db.models import get_app, get_models


for model in get_models(get_app(__name__.split('.')[-2:][0])):
    admin_class = type(
        "%sAdmin" % model.__name__,
        (admin.ModelAdmin,),
        dict(list_display=tuple([f.name for f in model._meta.fields]),)
    )

    admin.site.register(model, admin_class)
