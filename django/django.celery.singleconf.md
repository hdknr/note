Celery: 設定等を１つのファイルで済ます
- settings.py と celery.py と apps.pyとかにまたがるのがいやなので１つにしたい。apps.py に全部入りを作ってみる。

## settings.py のアプリをINSTALLED_APPSに追加
- appディレクトリ

~~~
$ tree -P "*.py" app

app
├── __init__.py
├── local_settings.py
├── settings.py
├── urls.py
└── wsgi.py

~~~

- settings.py を変更

~~~py
INSTALLED_APPS += ('app', )
~~~

## app/apps.py で Celeryの初期化

- 各種インポート

~~~py
import django                                                                       
from django.apps import AppConfig as DjangoAppConfig, apps                          
from django.utils.translation import (                                              
    ugettext_lazy as _,                                                             
)                                                                                   
from django.conf import settings                                                    
from celery import Celery                                                           
from kombu import Exchange, Queue                                                   
                                                                                    
import types                                                                        
import os                                                                           
import sys                                                                          
~~~

- Celeryの設定パラメータをdictで作成

~~~py                                                                                    
JOBQ = 'lafoglia'                                                                   
_conf = dict(                                                                       
    CELERY_RESULT_BACKEND='amqp',                                                   
    CELERY_ACCEPT_CONTENT=['json'],                                                 
    CELERY_TASK_SERIALIZER='json',                                                  
    CELERY_RESULT_SERIALIZER='json',                                                
    BROKER_URL='amqp://{0}:{1}@localhost:5672/{2}'.format(JOBQ, JOBQ, JOBQ),        
    CELERY_DEFAULT_QUEUE=JOBQ,                                                      
    CELERY_QUEUES=(Queue(JOBQ, Exchange(JOBQ), routing_key=JOBQ),),                 
)   
~~~

- AppConfig を作り、 ready()で Celeryを作成する
- _confをパラメータで読ませる

~~~py
class AppConfig(DjangoAppConfig):                                                   
    name = 'app'                                                                    
    verbose_name = _("Apps")                                                        
                                                                                    
    def ready(self):                                                                
        self.celery = Celery('app')                                                                 
        self.celery.config_from_object(_conf)                                       
        self.celery.autodiscover_tasks(
        	lambda: settings.INSTALLED_APPS) 
~~~

- built-inモジュールを定義
- Celeryが指定したモジュールから"app"をさがすので、プロパティを定義
- app()のなかでdjangoを起動
- AppConfigのceleryを返す

~~~py

class Loader(types.ModuleType):                                                  
    @property                                                                    
    def app(self):                                                               
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
                  
        # bin/celery でsys.pathが変わるっぽい                                          
        sys.path.insert(                                                         
            0,                                                                   
            os.path.dirname(
            	os.path.dirname(os.path.abspath(__file__))))      
        #     	   
        django.setup()                                                           
        return apps.get_app_config('app').celery                                 
~~~      

- 最後に、 モジュールをインスタンス化しておく

~~~py
celery = Loader('celery_loader')                                                 
~~~  

- `app/__init__.py` で default_app_configを指定する

~~~py
default_app_config = 'app.apps.AppConfig'

~~~


## app.apps.celeryでCeleryのワーカーを起動する

- _confで指定したキュー情報で起動

~~~
$ celery -A app.apps.celery worker -l info
 
 -------------- celery@jessie.local v3.1.18 (Cipater)
---- **** ----- 
--- * ***  * -- Linux-3.16.0-4-amd64-x86_64-with-debian-8.0
-- * - **** --- 
- ** ---------- [config]
- ** ---------- .> app:         app:0x7f868f35b1d0
- ** ---------- .> transport:   amqp://lafoglia:**@localhost:5672/lafoglia
- ** ---------- .> results:     amqp
- *** --- * --- .> concurrency: 1 (prefork)
-- ******* ---- 
--- ***** ----- [queues]
 -------------- .> lafoglia         exchange=lafoglia(direct) key=lafoglia
                

[tasks]
  . accounts.tasks.add
.....
~~~

- accounts.tasks.add

~~~py
>>> from accounts.tasks import *
>>> add.delay(1, 2).get()
3
~~~
