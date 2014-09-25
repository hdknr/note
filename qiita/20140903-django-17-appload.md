Django 1.7:リリースノート:AppConfigとアプリケーションローディング関連


# django.apps 

アプリケーションローディングの仕組み変わった以前は"app cache":

    App-loading refactor
    
        Historically, Django applications were tightly linked to models. 
        A singleton known as the “app cache” dealt with both installed applications and models. 
    
        The models module was used as an identifier for applications in many APIs.
    
        As the concept of Django applications matured, 
        this code showed some shortcomings. 
    

1.7では "app registry":

        It has been refactored into an “app registry” 
        where models modules no longer have a central role 
        and where it’s possible to attach configuration data to applications.

[djang.db.models.loading](https://github.com/django/django/blob/stable/1.6.x/django/db/models/loading.py)が廃止されて、
[django.apps](https://github.com/django/django/tree/stable/1.7.x/django/apps)が新設:

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ tree /home/hdknr/ve/v17/lib/python2.7/site-packages/django/apps/ -I "*.pyc"
    /home/hdknr/ve/v17/lib/python2.7/site-packages/django/apps/
    ├── __init__.py
    ├── config.py
    └── registry.py

- [1.7ドキュメント](https://docs.djangoproject.com/en/dev/ref/applications/)


# djang.apps.config.AppConfig 

[AppConfig](https://github.com/django/django/blob/stable/1.7.x/django/apps/config.py#L12):

```py

    >>> from django.apps import apps
    >>> apps.get_app_config('todos')
    <AppConfig: todos>
    >>> cf = _
    >>> cf.name, cf.verbose_name
    ('todos', 'Todos')
    >>> cf.path
    u'/home/hdknr/ve/v17/src/sample/web/todos'
    >>> cf.models
    OrderedDict([('todo', <class 'todos.models.Todo'>)])
    >>> [i for i in cf.get_models()]
    [<class 'todos.models.Todo'>]
    >>> cf.label
    'todos'
    >>> cf.models_module
    <module 'todos.models' from '/home/hdknr/ve/v17/src/sample/web/todos/models.pyc'>
    >>> cf.module
    <module 'todos' from '/home/hdknr/ve/v17/src/sample/web/todos/__init__.pyc'>
```

## AppConfig#ready()   


ready()が呼ばれるのでごにょれる：

    Improvements thus far include:
    
        Applications can run code at startup, 
        before Django does anything else, 
        with the ready() method of their configuration.

        Django imports all application configurations and models as soon as it starts, 
        through a deterministic and straightforward process. 
    
        This should make it easier to diagnose import issues such as import loops.

todos.apps を作成:

```py

    from django.apps import AppConfig
    from models import Todo
    
    
    class WebAppConfig(AppConfig):
        name = "todos"
        verbose_name = "Todos Application"
    
        def ready(self):
            print "todo application can be initialzed here."
            print "count = ", Todo.objects.count()

```


app/settings.py を修正:

```py

    INSTALLED_APPS += (
        #'todos',                   # コメント
        'todos.apps.WebAppConfig',  # AppConfigを指定
    )    

```

shellを起動するとプロンプトの前に ready()が実行されてる:

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py shell

    todo application can be initialzed here.
    count =  1

    Python 2.7.3 (default, Mar 13 2014, 11:03:55) 
    [GCC 4.7.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> 


# models.py不要 #

dashbaordアプリ追加:

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py startapp dashboard
    todo application can be initialzed here.
    count =  1


    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ cat dashboard/apps.py 

```py

    from django.apps import AppConfig
    
    
    class WebAppConfig(AppConfig):
        name = "dashboard"
        verbose_name = "Dashboard Application"
    
        def ready(self):
            print "dashboard application can be initialzed here."

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ cat app/settings.py

    INSTALLED_APPS += (
        #'todos',
        'todos.apps.WebAppConfig',
        'dashboard.apps.WebAppConfig',
    )
```

models.pyが無くてもアプリケーション初期化されてready()でなんかできる。
verboase_nameもカスタマイズ:

    It is possible to omit models.py entirely 
    if an application doesn’t have any models.

    The name of applications can be customized in the admin 
    with the verbose_name of application configurations.

確認:

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ rm dashboard/models.py

    (v17)hdknr@wzy:~/ve/v17/src/sample/web$ python manage.py shell
    todo application can be initialzed here.
    count =  1
    dashboard application can be initialzed here.
    Python 2.7.3 (default, Mar 13 2014, 11:03:55) 
    [GCC 4.7.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> apps.get_app_config('dashboard').verbose_name
    'Dashboard Application'

もちろんモデルない:

```py

    >>> from django.apps import apps
    >>> apps.get_app_config('dashboard').label
    'dashboard'
    >>> apps.get_app_config('dashboard').models
    OrderedDict()

```

## 1.6互換 ##

app/settings.py を修正:

```py

    INSTALLED_APPS += (
        'todos',                   
        #'todos.apps.WebAppConfig',  # コメント
    )    

```

todos/__init__.py:

```py

	default_app_config = "todos.apps.WebAppConfig"
```

    
# app_label #

app_label:

    Application labels are assigned correctly to models 
    even when they’re defined outside of models.py. 
     
    You don’t have to set app_label explicitly any more.
    
表示:    

```py

    >>> from django.apps import apps
    >>> apps.get_app_config('todos').label
    'todos'

```


labelがバッティングした時の為に修正できる:

    Applications can be relabeled with the label attribute of application configurations, 
    to work around label conflicts.
    
ready()でlabelを指定してみる:    

```py

    def ready(self):
        print "dashboard application can be initialzed here."
        self.label = "superdashboard"

    >>> from django.apps import apps
    >>> apps.get_app_config('dashboard').label
    'superdashboard'

```


# urls.py で autodiscover()なくてもadmin使える 


不要になりました:

    The admin automatically calls autodiscover() 
    when Django starts. 

    You can consequently remove this line from your URLconf.

