
# セッションエンジン

~~~
>>> from django.conf import settings
>>> settings.SESSION_ENGINE
'django.contrib.sessions.backends.db'
>>> engine = __import__(settings.SESSION_ENGINE, {}, {}, [''])
>>> dir()
['__builtins__', 'engine', 'settings']
~~~

## エンジンからセッションのロード

```
>>> engine.SessionStore(u'qzoehydb7vsxp7s3ipc5b92y95ah0rhs')
<django.contrib.sessions.backends.db.SessionStore object at 0x7fefb7896590>
>>> sobj = _
```

```
>>> sobj.keys()
[u'_auth_user_hash', u'_auth_user_id', u'_auth_user_backend']

>>> sobj['_auth_user_id']
1
```

```
>>> sobj['password_expired'] = True
>>> sobj.save()
```

# セッションストア

~~~
>>> from django.contrib.sessions.models import Session
>>> ses = Session.objects.all()[0]
>>> ses.get_decoded()
{u'password_expired': True,
 u'_auth_user_hash': u'c6736a9ca733a9a3380dd9127bf9d16b0f4eab9e',
 u'_auth_user_backend': u'django.contrib.auth.backends.ModelBackend',
 u'_auth_user_id': 1}

>>> type(_)
<type 'dict'>
~~~

## セッションオブジェクトでデータを修正して保存

~~~
>>> sobj['password_expired'] = False
>>> sobj.save()
>>> Session.objects.all()[0].get_decoded()['password_expired']
False
~~~




