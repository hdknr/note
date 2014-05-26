phpserialize: DjangoからXoopsのセッションテーブルを読む



DjangoのプロジェクトをつくってMySQLでxoopsを読めるようにする:

xoopsアプリをつくって INSTALLED_APPS に追加する

```py

    $ python manage.py startapp xoops
    
    $ echo "INSTALLED_APPS += ('xoops',)" >> app/settings.py
```
    
inspectdb する


    $ python manage.py inspectdb > xoops/models.py
    
    
PHPにSuhoshinが使われていたらencrytをoffにする

    $ grep encrypt /etc/php5/apache2/conf.d/suhosin.ini 

    suhosin.session.encrypt = off
    suhosin.cookie.encrypt = off
    
    $ sudo /etc/init.d/apache2 restart


PHPSESSIONID でクエリしてみる

```py

    >>> from xoops.models import XoopsSession
    >>> s = XoopsSession.objects.get(sess_id='5330d6965894abba386fbd35543e5792')
    >>> s.sess_data
    u'xoopsUserId|s:1:"1";xoopsUserGroups|a:2:{i:0;s:1:"1";i:1;s:1:"2";}protector_last_ip|s:13:"153.174.42.85";'

```
    

[unserialize_session](https://gist.github.com/scragg0x/3894835) を通してdict化する

```py

    >>> sd = unserialize_session(s.sess_data)
    >>> for k, v in sd.items():
    ...    print k, "=>", v
    ... 
    xoopsUserId => 1
    protector_last_ip => 155.174.42.85
    xoopsUserGroups => {0: u'1', 1: u'2'}

```

ユーザーを探す

```py

    >>> from xoops.models import XoopsUsers
    >>> xu = XoopsUsers.objects.get(uid=sd['xoopsUserId'])
    >>> xu.uname
    u'webadmin'
```
    
    
    
