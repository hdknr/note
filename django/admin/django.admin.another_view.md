Admin UI: モデルに別のビューを定義する

- 同じAdminサイトではモデルに複数のAdminを定義できない

~~~py
from django.contrib.auth.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']

admin.site.register(User, UserAdmin)
~~~

~~~
django.contrib.admin.sites.AlreadyRegistered: The model User is already registered
~~~

# Proxyモデル

- proxy = True で既存モデルのサブクラスを用意し、それにAdminを定義

~~~py
class Superuser(User):
    class Meta:
        proxy = True


class SuperuserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']

admin.site.register(Superuser, SuperuserAdmin)
~~~

# get_queryset

- 条件を絞るなど

~~~py
class SuperuserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']

    def get_queryset(self, request):
        return super(SuperuserAdmin, self).get_queryset(request).filter(
            is_superuser=True)
~~~            
