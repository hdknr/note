## TEST_DATABASE_COLLATION

~~~
/home/vagrant/.pyenv/versions/wordpress/lib/python2.7/site-packages/django/db/utils.py:238: RemovedInDjango19Warning: In Django 1.9 the TEST_DATABASE_COLLATION 
connection setting will be moved to a DATABASE_COLLATION entry in the TEST setting
  self.prepare_test_settings(alias)
~~~

##  RemovedInDjango19Warning: Model class django.contrib.contenttypes.models.ContentType doesn't declare an explicit app_label and either isn't in an application in INSTALLED_APPS or else was imported before its application was loaded. This will no longer be supported in Django 1.9.


## RemovedInDjango19Warning: django.db.models.get_models is deprecated.

## RemovedInDjango19Warning: The app_mod argument of get_models is deprecated.

## RemovedInDjango19Warning: The utilities in django.db.models.loading are deprecated in favor of the new application loading system.

## RemovedInDjango19Warning: The utilities in django.db.models.loading are deprecated in favor of the new application loading system.

## RemovedInDjango19Warning: django.db.models.get_app is deprecated.

~~~
RemovedInDjango19Warning: The utilities in django.db.models
.loading are deprecated in favor of the new application loading system.
~~~

- モデル一覧(これまで)

~~~
>>> from django.apps import apps
>>> apps.get_app('bulletins')
<string>:1: RemovedInDjango19Warning: get_app_config(app_label).models_module supersedes get_app(app_label).

<module 'bulletins.models' from '/home/vagrant/projects/myproj/web/bulletins/models.pyc'>
>>> apps.get_models(_)
[<class 'bulletins.models.Subject'>, <class 'bulletins.models.Post'>]
~~~

- モデル一覧(これから)

~~~
>>> apps.get_app_config('bulletins').models
OrderedDict([('subject', <class 'bulletins.models.Subject'>), ('post', <class 'bulletins.models.Post'>)])
~~~