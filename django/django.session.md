- [How to expire Django session in 5minutes?](http://stackoverflow.com/questions/14830669/how-to-expire-django-session-in-5minutes)


## SESSION_COOKIE_AGE

- セッション保持秒数
- [Settings](https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-SESSION_COOKIE_AGE)

~~~py
In [4]: settings.SESSION_COOKIE_AGE
Out[4]: 1209600
~~~

## SESSION_EXPIRE_AT_BROWSER_CLOSE

- [django 1.8 SESSION_EXPIRE_AT_BROWSER_CLOSE not working](http://stackoverflow.com/questions/30093624/django-1-8-session-expire-at-browser-close-not-working)
- [Browser-length sessions vs. persistent sessions](https://docs.djangoproject.com/en/1.9/topics/http/sessions/#browser-length-sessions-vs-persistent-sessions)


- デフォルト = False (SESSION_COOKIE_AGE でタイムアウト)

~~~py
In [2]: from django.conf import settings
In [3]: settings.SESSION_EXPIRE_AT_BROWSER_CLOSE
Out[3]: False
~~~
