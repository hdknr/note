Django 1.7:リリースノート:スキーママイグレーション関連

- https://docs.djangoproject.com/en/1.7/releases/1.7/#schema-migrations

# データベース初期化 #

startproject:

    (v17)hdknr@wzy:~/ve/v17/src/sample$ mkdir -p web; django-admin.py startproject app web ;cd web
    

migrate & createsuperuser :

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, contenttypes, auth, sessions
    Running migrations:
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying sessions.0001_initial... OK

    
    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py createsuperuser
    Username (leave blank to use 'hdknr'): admin
    Email address: admin@admin.admin
    Password: 
    Password (again): 
    Superuser created successfully.


syncdbも一応使える:

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ rm db.sqlite3 ; python manage.py syncdb
    Operations to perform:
      Apply all migrations: admin, contenttypes, auth, sessions
    Running migrations:
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying sessions.0001_initial... OK
    
    You have installed Django's auth system, and don't have any superusers defined.
    Would you like to create one now? (yes/no): yes
    Username (leave blank to use 'hdknr'): admin
    Email address: admin@admin.admin
    Password: 
    Password (again): 
    Superuser created successfully.
    

# モデルマイグレーション #

makemigrations:

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py makemigrations 
    No changes detected

アプリ追加

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py startapp todos
    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ tree todos/
    todos/
    ├── __init__.py
    ├── admin.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
    
    1 directory, 6 files

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ echo "INSTALLED_APPS += ('todos',)" >> app/settings.py

モデルクラス無いので追加:

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py makemigrations
    No changes detected

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ cat todos/models.py

    from django.db import models
    from django.contrib.auth.models import User
    
    
    class Todo(models.Model):
        user = models.ForeignKey(User)
        title = models.CharField(max_length=50)
        description = models.TextField()
        due_at = models.DateTimeField(
            null=True, blank=True, default=None)
        created_at = models.DateTimeField(auto_now_add=True, )
        updated_at = models.DateTimeField(auto_now=True, )


makemigrations:

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py makemigrations todos

    Migrations for 'todos':
      0001_initial.py:
        - Create model Todo

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ tree todos/

    todos/
    ├── __init__.py
    ├── __init__.pyc
    ├── admin.py
    ├── admin.pyc
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    │   └── __init__.pyc
    ├── models.py
    ├── models.pyc
    ├── tests.py
    └── views.py
    
    1 directory, 11 files
        
migrate:

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py migrate todos
    Operations to perform:
      Apply all migrations: todos
    Running migrations:
      Applying todos.0001_initial... OK        


    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ echo ".schema todos_todo" | python manage.py dbshell

    CREATE TABLE "todos_todo" (
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
        "title" varchar(50) NOT NULL, 
        "description" text NOT NULL, 
        "due_at" datetime NULL, 
        "created_at" datetime NOT NULL, 
        "updated_at" datetime NOT NULL, 
        "user_id" integer NOT NULL REFERENCES "auth_user" ("id"));

    CREATE INDEX todos_todo_e8701ad4 ON "todos_todo" ("user_id");
    
## django_migrations #

マイグレーションテーブル:

    $ echo ".schema django_migrations" | python manage.py dbshell

    CREATE TABLE "django_migrations" (
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
        "app" varchar(255) NOT NULL, 
        "name" varchar(255) NOT NULL, 
        "applied" datetime NOT NULL);

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ echo "select * from django_migrations;" | python manage.py dbshell

    1|contenttypes|0001_initial|2014-09-03 02:10:35.695671
    2|auth|0001_initial|2014-09-03 02:10:35.744375
    3|admin|0001_initial|2014-09-03 02:10:35.788881
    4|sessions|0001_initial|2014-09-03 02:10:35.808466
    5|todos|0001_initial|2014-09-03 02:10:35.855269
    6|todos|0002_todo_closed|2014-09-03 02:11:12.687727

モジュール:

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ tree $VIRTUAL_ENV/lib/python2.7/site-packages/django/db/migrations/ -I "*.pyc"
    /home/hdknr/ve/v17/lib/python2.7/site-packages/django/db/migrations/
    ├── __init__.py
    ├── autodetector.py
    ├── executor.py
    ├── graph.py
    ├── loader.py
    ├── migration.py
    ├── operations
    │   ├── __init__.py
    │   ├── base.py
    │   ├── fields.py
    │   ├── models.py
    │   └── special.py
    ├── optimizer.py
    ├── questioner.py
    ├── recorder.py
    ├── state.py
    └── writer.py
    
    1 directory, 16 files

shellから:

    >>> from django.db.migrations.recorder import *
    >>> for i in MigrationRecorder.Migration.objects.values():
    ...     print i
    ... 
    {'applied': datetime.datetime(2014, 9, 3, 2, 10, 35, 695671, tzinfo=<UTC>), 'app': u'contenttypes', u'id': 1, 'name': u'0001_initial'}
    {'applied': datetime.datetime(2014, 9, 3, 2, 10, 35, 744375, tzinfo=<UTC>), 'app': u'auth', u'id': 2, 'name': u'0001_initial'}
    {'applied': datetime.datetime(2014, 9, 3, 2, 10, 35, 788881, tzinfo=<UTC>), 'app': u'admin', u'id': 3, 'name': u'0001_initial'}
    {'applied': datetime.datetime(2014, 9, 3, 2, 10, 35, 808466, tzinfo=<UTC>), 'app': u'sessions', u'id': 4, 'name': u'0001_initial'}
    {'applied': datetime.datetime(2014, 9, 3, 2, 10, 35, 855269, tzinfo=<UTC>), 'app': u'todos', u'id': 5, 'name': u'0001_initial'}
    {'applied': datetime.datetime(2014, 9, 3, 2, 11, 12, 687727, tzinfo=<UTC>), 'app': u'todos', u'id': 6, 'name': u'0002_todo_closed'}


# pre_migrate/ post_migrate #

todos/models.py 修正:

    
    from django.dispatch import receiver
    from django.db.models.signals import (
        pre_migrate, post_migrate,
    )
    
    
    def trace(msg, sender, app_config, *args, **kwargs):
        assert sender == app_config
        assert args == ()
        if app_config and app_config.name == "todos":
            print msg 
            for k, v in kwargs.items():
                print "***", k, type(v), v
    
    
    @receiver(pre_migrate)
    def pre_migrate_handler(
        sender=None, app_config=None, *args, **kwargs
    ):
        trace(
            ">>> pre_migrate signal",
            sender, app_config, *args, **kwargs)
    
    
    @receiver(post_migrate)
    def post_migrate_handler(
        sender=None, app_config=None, *args, **kwargs
    ):
        trace(
            ">>> post_migrate signal",
            sender, app_config, *args, **kwargs)
    
    
    class Todo(models.Model):
        closed = models.BooleanField(default=False)
        ....    

makemigrations & migrate:

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py makemigrations todos

    Migrations for 'todos':
      0002_todo_closed.py:
        - Add field closed to todo
    
    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py migrate todos

    Operations to perform:
      Apply all migrations: todos
    Running migrations:
      Applying todos.0002_todo_closed... OK
    >>> post_migrate signal
    *** using <type 'str'> default
    *** verbosity <type 'int'> 1
    *** signal <class 'django.dispatch.dispatcher.Signal'> <django.dispatch.dispatcher.Signal object at 0x25ba110>
    *** interactive <type 'bool'> True

# Database router の allow_migrateメソッド #

allow_syncdb -> allow_migrateの変更。

既存のXOOPSのデータベースを読むようにrouteを設定:

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ more app/database.py

    _EXCLUSIVE = lambda obj: \
        {"xoops": "xoops"}.get(obj._meta.app_label, 'default')
    
    
    class SitesRouter(object):
    
        def db_for_read(self, model, **hints):
            return _EXCLUSIVE(model)
    
        def db_for_write(self, model, **hints):
            return _EXCLUSIVE(model)
    
        def allow_relation(self, obj1, obj2, **hints):
            d1, d2 = _EXCLUSIVE(obj1), _EXCLUSIVE(obj2)
    
            return None if d1 != d2 else d1
    
        def allow_migrate(self, db, model):
            ''' allow_syncdb -> allow_migrate '''
            return _EXCLUSIVE(model)

app/settings.py:

    INSTALLED_APPS += ('todos', 'xoops',)
    #
    DATABASES['xoops'] = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['XOOPS_DBNAME'],
        'USER': os.environ['XOOPS_DBUSER'],
        'PASSWORD': os.environ['XOOPS_DBPASSWORD'],
        'TEST_CHARSET': 'utf8',
        'TEST_DATABASE_COLLATION': 'utf8_general_ci',
    }
    DATABASE_ROUTERS = ['app.database.SitesRouter']
   

migrateしてみる:

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py migrate

    Operations to perform:
      Synchronize unmigrated apps: xoops
      Apply all migrations: admin, contenttypes, todos, auth, sessions
    Synchronizing apps without migrations:

    >>> pre_migrate signal
    *** using <type 'str'> default
    *** verbosity <type 'int'> 1
    *** signal <class 'django.dispatch.dispatcher.Signal'> <django.dispatch.dispatcher.Signal object at 0x27a4190>
    *** interactive <type 'bool'> True

      Creating tables...
      Installing custom SQL...
      Installing indexes...
    Running migrations:
      No migrations to apply.

    >>> post_migrate signal
    *** using <type 'str'> default
    *** verbosity <type 'int'> 1
    *** signal <class 'django.dispatch.dispatcher.Signal'> <django.dispatch.dispatcher.Signal object at 0x27a41d0>
    *** interactive <type 'bool'> True
     

# initial_data.json #

リリースノート:

    initial_data fixtures are no longer loaded for apps with migrations; 
    if you want to load initial data for an app, we suggest you do it in a migration.


initial_data.json:
   
    [{"fields": {"description": "task1", "title": "task1", 
      "due_at": null, "created_at": "2014-09-03T03:10:37.059Z", 
      "updated_at": "2014-09-03T03:10:37.059Z", "user": 1, "closed": false}, 
      "model": "todos.todo", "pk": 1}] 

削除:

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ echo "delete from todos_todo;" | python  manage.py dbshell

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ echo "select count(*) from todos_todo;" | python manage.py dbshell
    0

todosをmigrate:

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py migrate todos
    Operations to perform:
      Apply all migrations: todos
    Running migrations:
      No migrations to apply.

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ echo "select count(*) from todos_todo;" | python manage.py dbshell
    0
    

全体:

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py migrate
    Operations to perform:
      Synchronize unmigrated apps: xoops
      Apply all migrations: admin, contenttypes, todos, auth, sessions
    Synchronizing apps without migrations:
      Creating tables...
      Installing custom SQL...
      Installing indexes...
    Installed 1 object(s) from 1 fixture(s)
    Running migrations:
      No migrations to apply.

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ echo "select count(*) from todos_todo;" | python manage.py dbshell
    1

todos/fixtures/initial_data.json:

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py dumpdata  > todos/fixtures/initial_data.json


migrateで読まない：

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, contenttypes, todos, auth, sessions
    Running migrations:
      No migrations to apply.

testsだと読まれるが、テーブルが無いのでエラー:


    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py test todos

    ....
    
    django.db.utils.OperationalError: 
    Problem installing fixture '/home/hdknr/ve/v17/src/sample/web/todos/fixtures/initial_data.json': 
    Could not load contenttypes.ContentType(pk=1): no such table: django_content_type

プロジェクトルートにあってもエラー:


    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ mv todos/fixtures/initial_data.json  .
    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py test todos

    ....
    
    django.db.utils.OperationalError: 
    Problem installing fixture '/home/hdknr/ve/v17/src/sample/web/initial_data.json': 
    Could not load contenttypes.ContentType(pk=1): no such table: django_content_type


よって, initial_data.json は使わないでloadata で明示的にロードしたほうがいいのだろうか。



# TransactionTestCase #

TODO:
    
    TransactionTestCaseをつかったことないのないのであとで調べる

リリースノート:

    Test rollback behavior is different for apps with migrations; in particular, 
    Django will no longer emulate rollbacks on non-transactional databases 
    or inside TransactionTestCase unless specifically requested.


[Rollback emulation](https://docs.djangoproject.com/en/1.7/topics/testing/overview/#test-case-serialized-rollback):

    Any initial data loaded in migrations will only be available in TestCase tests 
    and not in TransactionTestCase tests, 
    and additionally only on backends 
    where transactions are supported (the most important exception being MyISAM).

    Django can reload that data for you on a per-testcase basis 
    by setting the serialized_rollback option to True 
    in the body of the TestCase or TransactionTestCase, 
    but note that this will slow down that test suite by approximately 3x.

    Third-party apps or those developing against MyISAM will need to set this; 
    in general, however, 
    you should be developing your own projects against a transactional database 
    and be using TestCase for most tests, and thus not need this setting.

    The initial serialization is usually very quick, 
    but if you wish to exclude some apps from this process 
    (and speed up test runs slightly), 
    you may add those apps to TEST_NON_SERIALIZED_APPS.

    Apps without migrations are not affected; 
    initial_data fixtures are reloaded as usual.


# 依存 #

アプリがマイグレーションがあるアプリケーション依存するならば、
かならずマイグレーションを持つようにする事。

    It is not advised to have apps 
    without migrations depend on 
    (have a ForeignKey or ManyToManyField to) apps with migrations. 

    Read the dependencies documentation for more.

- [リファレンス](https://docs.djangoproject.com/en/1.7/topics/migrations/#unmigrated-dependencies)

# South #

southからのマイグレーション。


- [簡単](https://docs.djangoproject.com/en/1.7/topics/migrations/#upgrading-from-south) ([リファレンス](http://south.readthedocs.org/en/latest/releasenotes/1.0.html#library-migration-path))


    - Southのマイグレーションが最新であることを確認
    - 'south' をINSTALLED_APPSから削除
    - migrations配下の数字で始まるファイルを削除。__init__.pyは残す。.pycファイルは削除。
    - makemigrations を実行。 
    - migrate を実行。
