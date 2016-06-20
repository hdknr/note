## Reference

- [Permissions and Authorization¶](https://docs.djangoproject.com/ja/1.9/topics/auth/default/#topic-authorization)


## パーミッションとグループの動的生成


~~~py
from django.contrib.auth.models import Group                                        
from django.utils.translation import ugettext_lazy as _                             

from . import models                                                                


def configure_conference_admin():                                                   

    codename = 'club_conference_admin'                                              
    name = _('Administer Club Conference')                                          
    groupname = _('Club Conference Admin')                                          

    # 対応するグループを作成                                                        
    group, _c = Group.objects.get_or_create(name=groupname)                         

    # パーミッション作成                                                            
    for m in [models.ConferenceCalendar, models.ConferenceOrder]:                   
        ct = m.contenttype()                                                        
        perm, _x = ct.permission_set.get_or_create(codename=codename)               
        perm.name = name                                                            
        perm.save()                                                                 
        group.permissions.add(perm)               
~~~

## パーミッション

### auth_permission

~~~mysql
mysql> desc auth_permission;
+-----------------+--------------+------+-----+---------+----------------+
| Field           | Type         | Null | Key | Default | Extra          |
+-----------------+--------------+------+-----+---------+----------------+
| id              | int(11)      | NO   | PRI | NULL    | auto_increment |
| name            | varchar(255) | YES  |     | NULL    |                |
| content_type_id | int(11)      | NO   | MUL | NULL    |                |
| codename        | varchar(100) | NO   |     | NULL    |                |
+-----------------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
~~~

## グループ

### auth_group

~~~mysql
mysql> desc auth_group;
+-------+-------------+------+-----+---------+----------------+
| Field | Type        | Null | Key | Default | Extra          |
+-------+-------------+------+-----+---------+----------------+
| id    | int(11)     | NO   | PRI | NULL    | auto_increment |
| name  | varchar(80) | NO   | UNI | NULL    |                |
+-------+-------------+------+-----+---------+----------------+
2 rows in set (0.00 sec)
~~~

##　グループとパーミッション

~~~mysql
mysql> desc auth_group_permissions;
+---------------+---------+------+-----+---------+----------------+
| Field         | Type    | Null | Key | Default | Extra          |
+---------------+---------+------+-----+---------+----------------+
| id            | int(11) | NO   | PRI | NULL    | auto_increment |
| group_id      | int(11) | NO   | MUL | NULL    |                |
| permission_id | int(11) | NO   | MUL | NULL    |                |
+---------------+---------+------+-----+---------+----------------+
3 rows in set (0.00 sec)
~~~

## ユーザーとグループ

~~~py
myuser.groups = [group_list]
myuser.groups.add(group, group, ...)
myuser.groups.remove(group, group, ...)
myuser.groups.clear()
~~~

~~~mysql
mysql> desc auth_user_groups;
+----------+---------+------+-----+---------+----------------+
| Field    | Type    | Null | Key | Default | Extra          |
+----------+---------+------+-----+---------+----------------+
| id       | int(11) | NO   | PRI | NULL    | auto_increment |
| user_id  | int(11) | NO   | MUL | NULL    |                |
| group_id | int(11) | NO   | MUL | NULL    |                |
+----------+---------+------+-----+---------+----------------+
3 rows in set (0.00 sec)
~~~


## ユーザーとパーミッション

~~~py
myuser.user_permissions = [permission_list]
myuser.user_permissions.add(permission, permission, ...)
myuser.user_permissions.remove(permission, permission, ...)
myuser.user_permissions.clear()
~~~

~~~mysql
mysql> desc auth_user_user_permissions;
+---------------+---------+------+-----+---------+----------------+
| Field         | Type    | Null | Key | Default | Extra          |
+---------------+---------+------+-----+---------+----------------+
| id            | int(11) | NO   | PRI | NULL    | auto_increment |
| user_id       | int(11) | NO   | MUL | NULL    |                |
| permission_id | int(11) | NO   | MUL | NULL    |                |
+---------------+---------+------+-----+---------+----------------+
3 rows in set (0.00 sec)
~~~

## モデルとパーミッション

Model Meta options:

- [permissions](https://docs.djangoproject.com/ja/1.9/ref/models/options/#permissions)
- [default_permissions](https://docs.djangoproject.com/ja/1.9/ref/models/options/#default-permissions)

~~~py
class Task(models.Model):
    ...
    class Meta:
        permissions = (
            ("view_task", "Can see available tasks"),
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        )
~~~        

## ビューとパーミッション

~~~py
from django.contrib.auth.decorators import permission_required

@permission_required('polls.can_vote', login_url='/loginpage/')
def my_view(request):
    …
~~~

~~~py
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.has_perm('polls.can_vote'), login_url='/login/')
def my_view(request):
    ...
~~~    

## テンプレートとパーミッション


- [Permissions](https://docs.djangoproject.com/en/dev/topics/auth/default/#permissions)

### `{{ perms }}`

~~~
The currently logged-in user’s permissions are stored in the template variable {{ perms }}
~~~

-  `User.has_module_perms`

`foo` モジュールのパーミッションがあるか？

~~~html
{{ perms.foo }}
~~~

`foo.can_vote` があるか？

~~~html
{{ perms.foo.can_vote }}
~~~

~~~html
{% if perms.foo %}
    <p>You have permission to do something in the foo app.</p>
    {% if perms.foo.can_vote %}
        <p>You can vote!</p>
    {% endif %}
    {% if perms.foo.can_drive %}
        <p>You can drive!</p>
    {% endif %}
{% else %}
    <p>You don't have permission to do anything in the foo app.</p>
{% endif %}
~~~

### in

~~~html
{% if 'foo' in perms %}
    {% if 'foo.can_vote' in perms %}
        <p>In lookup works, too.</p>
    {% endif %}
{% endif %}
~~~




## django.contrib.auth.models

~~~py
In [1]: from django.contrib.auth import models

In [2]: models.
models.AbstractBaseUser             models.PermissionDenied             models.python_2_unicode_compatible
models.AbstractUser                 models.PermissionManager            models.send_mail
models.AnonymousUser                models.PermissionsMixin             models.six
models.BaseUserManager              models.User                         models.timezone
models.ContentType                  models.UserManager                  models.unicode_literals
models.EmptyManager                 models.auth                         models.update_last_login
models.Group                        models.models                       models.user_logged_in
models.GroupManager                 models.py                           models.validators
models.Permission                   models.pyc                          

~~~

~~~py
In [8]: group = models.Group.objects.filter(name__startswith='Club').first()
In [9]: group.name
Out[9]: u'Club Conference Admin'
~~~

~~~py
In [24]: for g in group.permissions.all():
    	       print g.codename, g.content_type
              ....:    
club_conference_admin Conference Calendar
club_conference_admin Conference Order
~~~

~~~py
In [13]: admin = models.User.objects.filter(username='admin').first()
In [14]: admin
Out[14]: <User: admin>
~~~

~~~py
In [16]: admin.user_permissions.all()
Out[16]: []
~~~

- 管理者はすべてのパーミッションを持っている

~~~py
In [19]: admin.has_perm('club_conference_admin')
Out[19]: True
In [20]: admin.is_superuser
Out[20]: True
~~~

- 新ユーザー

~~~py
In [12]: user = models.User.objects.create_user('user', 'user', 'user@test.com')
In [13]: user.has_perm('club.club_conference_admin')
Out[13]: False

~~~

~~~py
In [7]: user.groups.add(group)
~~~

- [User Methods](https://docs.djangoproject.com/ja/1.9/ref/contrib/auth/#methods)

~~~py
In [8]: user.get_all_permissions()
Out[8]: {u'club.club_conference_admin'}

In [8]: user.get_group_permissions()
Out[8]: {u'club.club_conference_admin'}


In [9]: user.has_module_perms('club')
Out[9]: True

In [11]: user.has_perm('club.club_conference_admin')                                                                                         
Out[11]: True

~~~


## オブジェクトごとのパーミッション

- [Django Per Object Permission for Your Own User Model](http://stackoverflow.com/questions/33227521/django-per-object-permission-for-your-own-user-model)

~~~py
class ObjectPermissionsBackend(object):

    def has_perm(self, user_obj, perm, obj=None):
        if obj:
          if perm == 'view':
              return True # anyone can view
          elif obj.author_id == user_obj.pk:
              return True
        return False
~~~

~~~py
AUTHENTICATION_BACKENDS = (
  'django.contrib.auth.backends.ModelBackend',
  'path.to.ObjectPermissionsBackend',
)
~~~

~~~py
if user.has_perm('edit', article_instance):
    # allow editing
    ...
~~~
