# local_settings

- settings.py のパラメータをオーバーライドさせる
- 同じディレクトリに local_settings.py を置いて, settings.py と同様に設定する

~~~
try:
    import local_settings
    globals().update(
        dict((k, v) for k, v in local_settings.__dict__.items()
        if not k.startswith('_'))
    )   
except:
    pass
~~~

もしくは

~~~
try:
	from local_settings import *
except:
	pass
~~~	    

# リンク

- [Django settings](https://docs.djangoproject.com/en/1.7/topics/settings/)

