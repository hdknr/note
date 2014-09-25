Django 1.7:リリースノート: Fieldサブクラス新メソッド関連

- https://docs.djangoproject.com/en/dev/releases/1.7/#new-method-on-field-subclasses

# deconstruct() #

[deconstruct(self)](https://github.com/django/django/blob/stable/1.7.x/django/db/models/fields/__init__.py#L292):

    To help power both schema migrations 
    and to enable easier addition of composite keys in future releases of Django, 
    the Field API now has a new required method: deconstruct().

4アイテムのタプルを返す:

    This method takes no arguments, and returns a tuple of four items:

    name: The field’s attribute name on its parent model, 
          or None if it is not part of a model

    path: A dotted, Python path to the class of this field, 
          including the class name.

    args: Positional arguments, as a list

    kwargs: Keyword arguments, as a dict

    These four values allow any field to be serialized into a file, 
    as well as allowing the field to be copied safely, both essential parts of these new features.

Todoモデルのフィールドのdeconstruct():
    
```py
    
    >>> from todos.models import Todo
    >>> import json
    >>> print json.dumps(dict([ (f.name, f.deconstruct()) for f in Todo._meta.fields ]),indent=2)
    {
      "title": [
        "title", 
        "django.db.models.CharField", 
        [], 
        {
          "max_length": 50
        }
      ], 
      ...... (省略)
      "user": [
        "user", 
        "django.db.models.ForeignKey", 
        [], 
        {
          "to": "auth.User"
        }
      ], 
      "id": [
        "id", 
        "django.db.models.AutoField", 
        [], 
        {
          "verbose_name": "ID", 
          "serialize": false, 
          "auto_created": true, 
          "primary_key": true
        }
      ]
    }
```


deconsturct()でモデル定義のシリアライズをカスタマイズできるので、マイグレーションとかで便利:

    This change should not affect you unless you write custom Field subclasses; 

    if you do, 
    you may need to reimplement the deconstruct() method 
    if your subclass changes the method signature of __init__ in any way. 
    
    If your field just inherits from a built-in Django field and doesn’t override __init__, 
    no changes are necessary.

試しにしビルトインフィールドのdeconstuct()をオーバーライドして親クラスのメソッド読んだり
フィールドを削除してみたりとかやれば:

    If you do need to override deconstruct(), 
    a good place to start is the built-in Django fields 
    (django/db/models/fields/__init__.py) as several fields
    , including DecimalField and DateField, 
    override it and show how to call the method 
    on the superclass and simply add or remove extra arguments.

要はフィールドクラスへの引数は全部シリアライズされないといけない。
詳細は、 [リファレンス](https://docs.djangoproject.com/en/dev/topics/migrations/#migration-serializing)を:　

    This also means that all arguments to fields must themselves be serializable; 
    to see what we consider serializable, and to find out how to make your own classes serializable, 
    read the migration serialization documentation.
    

# MigrationAutodetector #


- [MigrationAutodetector](https://github.com/django/django/blob/stable/1.7.x/django/db/migrations/autodetector.py#L16)
  の[changes()](https://github.com/django/django/blob/stable/1.7.x/django/db/migrations/autodetector.py#L34)が、モデルの差分を判断します
- モデルの差分は前後のモデルのフィールドの deconstruct() を取得して、比較して作成する
- generate_ ではじまるメソッドが差分の生成 
- 差分をまとめたものが[Migration](https://github.com/django/django/blob/stable/1.7.x/django/db/migrations/migration.py#L5)
- [makemigrations](https://github.com/django/django/blob/stable/1.7.x/django/core/management/commands/makemigrations.py)

 
新規モデルを追加:


```py

    class Log(models.Model):
        todo = models.ForeignKey(Todo)
        created_at = models.DateTimeField(auto_now_add=True, )

```
        

MigrationLoader:

```py

    >>> from django.db.migrations.loader import MigrationLoader
    >>> loader = MigrationLoader(None, ignore_no_migrations=True)
```

マイグレーション前のプロジェクトステータス(かな?):

```py

    >>> project_state = loader.project_state()
    >>> type(project_state)
    <class 'django.db.migrations.state.ProjectState'>

    >>> project_state.models
    {
     ('todos', u'todo'): <ModelState: 'todos.Todo'>, 
     ('admin', u'logentry'): <ModelState: 'admin.LogEntry'>,
     ('contenttypes', u'contenttype'): <ModelState: 'contenttypes.ContentType'>, 
     ('sessions', u'session'): <ModelState: 'sessions.Session'>, 
     ('auth', u'permission'): <ModelState: 'auth.Permission'>, 
     ('auth', u'user'): <ModelState: 'auth.User'>, 
     ('auth', u'group'): <ModelState: 'auth.Group'>, 
    }
```

マイグレーションしようとしているプロジェクトのステータス(かな?):

```py

    >>> from django.apps import apps
    >>> from django.db.migrations.state import ProjectState

    >>> ProjectState.from_apps(apps)
    <django.db.migrations.state.ProjectState object at 0x3161290>
    >>> states = _
    
    >>> states.models
    {
     (u'todos', u'log'): <ModelState: 'todos.Log'>, 
     (u'todos', u'todo'): <ModelState: 'todos.Todo'>, 
     ('admin', u'logentry'): <ModelState: 'admin.LogEntry'>, 
     ('contenttypes', u'contenttype'): <ModelState: 'contenttypes.ContentType'>, 
     ('sessions', u'session'): <ModelState: 'sessions.Session'>, 
     ('auth', u'permission'): <ModelState: 'auth.Permission'>, 
     ('auth', u'user'): <ModelState: 'auth.User'>, 
     ('auth', u'group'): <ModelState: 'auth.Group'>
    }
```


マイグレーションの対話(かな?):

```py

    >>> InteractiveMigrationQuestioner(specified_apps=app_labels, dry_run=True)
    <django.db.migrations.questioner.InteractiveMigrationQuestioner object at 0x3172ad0>
    >>> q = _
```

ディテクタ生成:

```py

    >>> MigrationAutodetector(project_state, states, q)
    <django.db.migrations.autodetector.MigrationAutodetector object at 0x3172b10>
    >>> detector = _
```

generate_ メソッド:

```py

    >>> import json
    >>> print json.dumps([i for i in dir(detector) if i.startswith('generate_')], indent=2)
    [
      "generate_added_fields", 
      "generate_altered_fields", 
      "generate_altered_index_together", 
      "generate_altered_options", 
      "generate_altered_order_with_respect_to", 
      "generate_altered_unique_together", 
      "generate_created_models", 
      "generate_created_proxies", 
      "generate_created_unmanaged", 
      "generate_deleted_models", 
      "generate_deleted_proxies", 
      "generate_deleted_unmanaged", 
      "generate_removed_fields", 
      "generate_renamed_fields", 
      "generate_renamed_models"
    ]
```


