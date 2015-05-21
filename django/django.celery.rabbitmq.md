Celery: @shared_task

- キュー、エクスジェンジ、キーなどを変えたり複数定義したりするとき

## RabbitMQにユーザーと仮想ホスト作成

~~~ 
$ sudo rabbitmqctl add_vhost lafoglia
$ sudo rabbitmqctl add_user lafoglia lafoglia
$ sudo rabbitmqctl set_permissions -p lafoglia lafoglia ".*" ".*" ".*"
~~~


## app/settings.py

- kombuでCELERY_QUEUESを定義
- めんどくさいのでJOBQでuser, vhost, passwordなどを同じにしてみた

~~~py
JOBQ = 'lafoglia'

CELERY_RESULT_BACKEND = 'amqp'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
BROKER_URL = 'amqp://{0}:{1}@localhost:5672/{2}'.format(JOBQ, JOBQ, JOBQ)
from kombu import Exchange, Queue
CELERY_DEFAULT_QUEUE = JOBQ
CELERY_QUEUES = (Queue(JOBQ, Exchange(JOBQ), routing_key=JOBQ),)
~~~

## app/celery.py

- サンプル通り

~~~py
from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

from django.conf import settings

app = Celery('app')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
~~~

## acounts/tasks.py

- サンプル通り

~~~py
from celery import shared_task

@shared_task
def add(x, y):
    ret = x + y
    return ret
~~~

## ワーカー

- settings.py のキューでCeleryのワーカーが動いている
- ので、このCeleryにたいしてジョブを投げる必要があります

~~~
$ celery -A app worker -l info -E -B
~~~
~~~
 -------------- celery@jessie.local v3.1.18 (Cipater)
---- **** ----- 
--- * ***  * -- Linux-3.16.0-4-amd64-x86_64-with-debian-8.0
-- * - **** --- 
- ** ---------- [config]
- ** ---------- .> app:         app:0x7f027c104050
- ** ---------- .> transport:   amqp://lafoglia:**@localhost:5672/lafoglia
- ** ---------- .> results:     amqp
- *** --- * --- .> concurrency: 1 (prefork)
-- ******* ---- 
--- ***** ----- [queues]
 -------------- .> lafoglia         exchange=lafoglia(direct) key=lafoglia
                

[tasks]
  . accounts.tasks.add
~~~

## タスク実行 : app をロードすること

- app(Celeryインスタンス)にキューのパラメータが保持されているので、appが違うと別のキューに対してタスクを投げようとしてしまう。

~~~py
>>> from accounts.tasks import *
>>> add.delay(1, 3).get()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/vagrant/.anyenv/envs/pyenv/versions/wordpress/lib/python2.7/site-packages/celery/result.py", line 169, in get
    no_ack=no_ack,
  File "/home/vagrant/.anyenv/envs/pyenv/versions/wordpress/lib/python2.7/site-packages/celery/backends/base.py", line 601, in _is_disabled
    'No result backend configured.  '
NotImplementedError: No result backend configured.  Please see the documentation for more information.
~~~

~~~py
>>> from app.celery import app
>>> add.delay(1, 3).get()
4
~~~

## current_app とは？

~~~py
>>> from celery import current_app
>>> current_app.main
'default'
>>> from app.celery import app
>>> current_app.main
'app'
~~~
~~~py
>>> from celery import Celery
>>> app = Celery('hoge')
>>> current_app.main
'hoge'
~~~

## celery.local.Proxy

~~~
>>> type(current_app)
<class 'celery.local.Proxy'>
~~~

- つまり、current_appは参照されるたびに現在のCeleryインスタンスを返す代理オブジェクト

~~~py
class Proxy(object):                                                             

    def __init__(self, local,                                                    
                 args=None, kwargs=None, 
                 name=None, __doc__=None):     
        
        # 元のオブジェクト保存 
        object.__setattr__(self, '_Proxy__local', local)  
        ...
        
    def _get_current_object(self):                                                
        
        # 代理元の実際のオブジェクト                                                                   
        loc = object.__getattribute__(self, '_Proxy__local')   
        
        # celery.utils.threads.Localのサブクラス                  
        if not hasattr(loc, '__release_local__'):                                
            return loc(*self.__args, **self.__kwargs)   
                                     
        try:                                                                     
            return getattr(loc, self.__name__)                                   
        except AttributeError:                                                   
            raise RuntimeError(
            	'no object bound to {0.__name__}'.format(self))   


~~~

##  celery.app.base.Celery

- コンストラクタで自分を現在のアプリとして設定します

~~~py
class Celery(object): 
	...
	def __init__(self, ....):
		...	               
        if self.set_as_current:                                                  
            self.set_current()                                                   
		...

    def set_current(self):                                                       
        _set_current_app(self)    	
~~~

## celery._state._set_current_app

- TLS(Thread Loacal Storage) にシングルトンで現在のアプリを保持

~~~py
def _set_current_app(app):                                                          
    _tls.current_app = app                                                          
~~~                              
                              
~~~py
class _TLS(threading.local):                                                                   
    current_app = None  
                                                             
_tls = _TLS() 
~~~


## celery._state._get_current_app

- TLSから current_appを返す
- NoneだったらデフォルトCeleryを作ってカレントに設定してから返す

~~~py
def _get_current_app():                                                          
    if default_app is None:                                                      
        from celery.app import Celery  
        # デフォルト作成                                          
        set_default_app(Celery(                                                  
            'default',                                                           
            loader=os.environ.get('CELERY_LOADER') or 'default',                 
            fixups=[],                                                           
            set_as_current=False, accept_magic_kwargs=True,                      
        ))     
                                                                          
    return _tls.current_app or default_app                                       
~~~

- これは基本的には get_current_app() です


## celery._state.current_app

- get_current_app() のプロキシーです

~~~py
current_app = Proxy(get_current_app) 
~~~
