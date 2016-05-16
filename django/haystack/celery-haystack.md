celery-haystack: バックグラウンドでインデクシング

# インストール

~~~bash
$ sudo apt-get install redis-server redis-tools -y

$ echo "info" | redis-cli  | grep port
tcp_port:6379
~~~

~~~bash
$ pip install celery[redis]
$ pip install celery-haystack -U
~~~

# app/celery

~~~py
from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')
app.conf.update(
    BROKER_URL='redis://localhost:6379/0',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
~~~

# app/settings.py

~~~py
INSTALLED_APPS += [
    'celery_haystack',
]
HAYSTACK_SIGNAL_PROCESSOR = 'celery_haystack.signals.CelerySignalProcessor'
~~~

# blog : celery タスクの起動


- [Redis broker not working. Celery 3.1.13 #2240](https://github.com/celery/celery/issues/2240)
- どれかのアプリで app.celery.app をロードする

- \__init__.py

~~~py
default_app_config = 'blog.apps.BlogConfig'
~~~

- apps.py

~~~py
from __future__ import unicode_literals
from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        from app.celery import app as celery_app   # NOQA
~~~

# タスクの実行

~~~bash
$ ls manage.py
manage.py

$ celery  --workdir=$PWD --app=app.celery  worker -l debug
[2016-05-16 12:58:41,048: DEBUG/MainProcess] | Worker: Preparing bootsteps.
[2016-05-16 12:58:41,054: DEBUG/MainProcess] | Worker: Building graph...
[2016-05-16 12:58:41,055: DEBUG/MainProcess] | Worker: New boot order: {StateDB, Timer, Hub, Queues (intra), Pool, Autoreloader, Beat, Autoscaler, Consumer}
[2016-05-16 12:58:41,064: DEBUG/MainProcess] | Consumer: Preparing bootsteps.
[2016-05-16 12:58:41,066: DEBUG/MainProcess] | Consumer: Building graph...
[2016-05-16 12:58:41,077: DEBUG/MainProcess] | Consumer: New boot order: {Connection, Events, Mingle, Tasks, Control, Agent, Heart, Gossip, event loop}

 -------------- celery@jessie.local v3.1.23 (Cipater)
---- **** -----
--- * ***  * -- Linux-3.16.0-4-amd64-x86_64-with-debian-8.4
-- * - **** ---
- ** ---------- [config]
- ** ---------- .> app:         app:0x7fd2d298c650
- ** ---------- .> transport:   redis://localhost:6379/0
- ** ---------- .> results:     disabled://
- *** --- * --- .> concurrency: 1 (prefork)
-- ******* ----
--- ***** ----- [queues]
 -------------- .> celery           exchange=celery(direct) key=celery


[tasks]
  . blog.tasks.add
  . celery.backend_cleanup
  . celery.chain
  . celery.chord
  . celery.chord_unlock
  . celery.chunks
  . celery.group
  . celery.map
  . celery.starmap
  . celery_haystack.tasks.CeleryHaystackSignalHandler
  . celery_haystack.tasks.CeleryHaystackUpdateIndex

  [2016-05-16 12:58:41,094: DEBUG/MainProcess] | Worker: Starting Hub
  [2016-05-16 12:58:41,096: DEBUG/MainProcess] ^-- substep ok
  [2016-05-16 12:58:41,097: DEBUG/MainProcess] | Worker: Starting Pool
  [2016-05-16 12:58:41,130: DEBUG/MainProcess] ^-- substep ok
  [2016-05-16 12:58:41,134: DEBUG/MainProcess] | Worker: Starting Consumer
  [2016-05-16 12:58:41,134: DEBUG/MainProcess] | Consumer: Starting Connection
  [2016-05-16 12:58:41,149: INFO/MainProcess] Connected to redis://localhost:6379/0
  [2016-05-16 12:58:41,152: DEBUG/MainProcess] ^-- substep ok
  [2016-05-16 12:58:41,153: DEBUG/MainProcess] | Consumer: Starting Events
  [2016-05-16 12:58:41,163: DEBUG/MainProcess] ^-- substep ok
  [2016-05-16 12:58:41,164: DEBUG/MainProcess] | Consumer: Starting Mingle
  [2016-05-16 12:58:41,165: INFO/MainProcess] mingle: searching for neighbors
  [2016-05-16 12:58:42,171: INFO/MainProcess] mingle: all alone
  [2016-05-16 12:58:42,172: DEBUG/MainProcess] ^-- substep ok
  [2016-05-16 12:58:42,173: DEBUG/MainProcess] | Consumer: Starting Tasks
  [2016-05-16 12:58:42,176: DEBUG/MainProcess] ^-- substep ok
  [2016-05-16 12:58:42,177: DEBUG/MainProcess] | Consumer: Starting Control
  [2016-05-16 12:58:42,179: DEBUG/MainProcess] ^-- substep ok
  [2016-05-16 12:58:42,180: DEBUG/MainProcess] | Consumer: Starting Heart
  [2016-05-16 12:58:42,182: DEBUG/MainProcess] ^-- substep ok
  [2016-05-16 12:58:42,183: DEBUG/MainProcess] | Consumer: Starting Gossip
  [2016-05-16 12:58:42,186: DEBUG/MainProcess] ^-- substep ok
  [2016-05-16 12:58:42,187: DEBUG/MainProcess] | Consumer: Starting event loop
  /home/vagrant/.anyenv/envs/pyenv/versions/oilliocp/lib/python2.7/site-packages/celery/fixups/django.py:265: UserWarning: Using settings.DEBUG leads to a memory leak, never use this setting
  in production environments!
    warnings.warn('Using settings.DEBUG leads to a memory leak, never '

  [2016-05-16 12:58:42,188: WARNING/MainProcess] /home/vagrant/.anyenv/envs/pyenv/versions/oilliocp/lib/python2.7/site-packages/celery/fixups/django.py:265: UserWarning: Using settings.DEBUG
  leads to a memory leak, never use this setting in production environments!
    warnings.warn('Using settings.DEBUG leads to a memory leak, never '

  [2016-05-16 12:58:42,191: WARNING/MainProcess] celery@jessie.local ready.
  [2016-05-16 12:58:42,193: DEBUG/MainProcess] | Worker: Hub.register Pool...
  [2016-05-16 12:58:42,194: DEBUG/MainProcess] basic.qos: prefetch_count->4

~~~


# 管理画面で保存

~~~bash


[2016-05-16 13:00:31,729: INFO/MainProcess] Received task: celery_haystack.tasks.CeleryHaystackSignalHandler[61a595fb-bda3-4381-9b6b-60d904c4cfbc]
[2016-05-16 13:00:31,730: DEBUG/MainProcess] TaskPool: Apply <function _fast_trace_task at 0x7f32137e40c8> (args:(u'celery_haystack.tasks.CeleryHaystackSignalHandler', u'61a595fb-bda3-4381-
9b6b-60d904c4cfbc', [u'update', u'blog.note.1'], {}, {u'utc': True, u'is_eager': False, u'chord': None, u'group': None, u'args': [u'update', u'blog.note.1'], u'retries': 0, u'delivery_info'
: {u'priority': 0, u'redelivered': None, u'routing_key': u'celery', u'exchange': u'celery'}, u'expires': None, u'hostname': 'celery@jessie.local', u'task': u'celery_haystack.tasks.CeleryHay
stackSignalHandler', u'callbacks': None, u'correlation_id': u'61a595fb-bda3-4381-9b6b-60d904c4cfbc', u'errbacks': None, u'timelimit': [None, None], u'taskset': None, u'kwargs': {}, u'eta':
None, u'reply_to': u'25070a2c-468a-3ebe-9ef9-46b6c01acd90', u'id': u'61a595fb-bda3-4381-9b6b-60d904c4cfbc', u'headers': {}}) kwargs:{})
[2016-05-16 13:00:31,737: DEBUG/MainProcess] Task accepted: celery_haystack.tasks.CeleryHaystackSignalHandler[61a595fb-bda3-4381-9b6b-60d904c4cfbc] pid:31164
[2016-05-16 13:00:31,815: DEBUG/Worker-1] Converted retries value: False -> Retry(total=False, connect=None, read=None, redirect=0)
[2016-05-16 13:00:31,818: INFO/Worker-1] Starting new HTTP connection (1): 127.0.0.1
[2016-05-16 13:00:31,823: DEBUG/Worker-1] "GET /haystack/_mapping HTTP/1.1" 200 407
[2016-05-16 13:00:31,826: INFO/Worker-1] GET http://127.0.0.1:9200/haystack/_mapping [status:200 request:0.010s]
[2016-05-16 13:00:31,827: DEBUG/Worker-1] > None
[2016-05-16 13:00:31,830: DEBUG/Worker-1] < {"haystack":{"mappings":{"modelresult":{"properties":{"author":{"type":"string","analyzer":"snowball"},"django_ct":{"type":"string","index":"not_
analyzed","include_in_all":false},"django_id":{"type":"string","index":"not_analyzed","include_in_all":false},"id":{"type":"string"},"pub_date":{"type":"date","format":"strict_date_optional
_time||epoch_millis"},"text":{"type":"string","analyzer":"snowball"}}}}}}
[2016-05-16 13:00:31,832: WARNING/Worker-1] No handlers could be found for logger "elasticsearch.trace"
[2016-05-16 13:00:31,835: DEBUG/Worker-1] Converted retries value: False -> Retry(total=False, connect=None, read=None, redirect=0)
[2016-05-16 13:00:31,839: DEBUG/Worker-1] "PUT /haystack HTTP/1.1" 400 211
[2016-05-16 13:00:31,840: INFO/Worker-1] PUT http://127.0.0.1:9200/haystack [status:400 request:0.006s]
[2016-05-16 13:00:31,841: DEBUG/Worker-1] > {"settings": {"analysis": {"filter": {"haystack_edgengram": {"max_gram": 15, "type": "edgeNGram", "min_gram": 2}, "haystack_ngram": {"max_gram":
15, "type": "nGram", "min_gram": 3}}, "tokenizer": {"haystack_ngram_tokenizer": {"max_gram": 15, "type": "nGram", "min_gram": 3}, "haystack_edgengram_tokenizer": {"max_gram": 15, "type": "e
dgeNGram", "side": "front", "min_gram": 2}}, "analyzer": {"edgengram_analyzer": {"filter": ["haystack_edgengram", "lowercase"], "type": "custom", "tokenizer": "standard"}, "ngram_analyzer":
 {"filter": ["haystack_ngram", "lowercase"], "type": "custom", "tokenizer": "standard"}}}}}
[2016-05-16 13:00:31,843: DEBUG/Worker-1] < {"error":{"root_cause":[{"type":"index_already_exists_exception","reason":"already exists","index":"haystack"}],"type":"index_already_exists_exce
ption","reason":"already exists","index":"haystack"},"status":400}
[2016-05-16 13:00:31,845: DEBUG/Worker-1] Converted retries value: False -> Retry(total=False, connect=None, read=None, redirect=0)
[2016-05-16 13:00:31,860: DEBUG/Worker-1] "PUT /haystack/_mapping/modelresult HTTP/1.1" 200 21
[2016-05-16 13:00:31,862: INFO/Worker-1] PUT http://127.0.0.1:9200/haystack/_mapping/modelresult [status:200 request:0.017s]
[2016-05-16 13:00:31,864: DEBUG/Worker-1] > {"modelresult": {"properties": {"django_ct": {"include_in_all": false, "index": "not_analyzed", "type": "string"}, "text": {"type": "string", "an
alyzer": "snowball"}, "django_id": {"include_in_all": false, "index": "not_analyzed", "type": "string"}, "pub_date": {"type": "date"}, "author": {"type": "string", "analyzer": "snowball"}}}
}
[2016-05-16 13:00:31,865: DEBUG/Worker-1] < {"acknowledged":true}
[2016-05-16 13:00:31,885: DEBUG/Worker-1] Converted retries value: False -> Retry(total=False, connect=None, read=None, redirect=0)
[2016-05-16 13:00:31,907: DEBUG/Worker-1] "POST /haystack/modelresult/_bulk HTTP/1.1" 200 184
[2016-05-16 13:00:31,908: INFO/Worker-1] POST http://127.0.0.1:9200/haystack/modelresult/_bulk [status:200 request:0.023s]
[2016-05-16 13:00:31,908: DEBUG/Worker-1] > {"index": {"_id": "blog.note.1"}}
{"django_ct": "blog.note", "django_id": "1", "author": "vagrant", "text": "平清盛の死因はインフルエンザか 謎の高熱に苦しんだ描写\nデフォルト 管理者\n「討死」や「謀殺」、「自決」によって英雄
の最期はドラマチックに語り継がれるが、「病」に苦しみ、「病」と闘い、「病」に斃れた歴史上の人物の悩みはあまり知られていない。平清盛（1118～1181年。享年63）の死因は何だったのか？\r\n\r\n　115
9年の平治の乱で源義朝を破り、武士として初めて太政大臣となった平清盛。平家の棟梁として独裁政権を樹立したが、源頼朝ら反平家の源氏が蜂起した1181年、謎の熱病に侵された。\r\n\r\n『平家物語』の第
六巻「入道死去」には、清盛が1週間にわたり高熱に苦しむ様子が「悶絶躄地して、つひにあつち死にぞし給ける」と描写されており、身体を冷やす水がたちまち水蒸気になったとも。2月という季節柄、インフ
ルエンザに罹患した可能性が指摘されている。\r\n\r\n※病名などについては『戦国武将の死亡診断書』（酒井シヅ監修／エクスナレッジ刊）などを参考に記したが、病名や死因については諸説ある。生年・没年
については『コンサイス日本人名事典』（第4版／三省堂）などを参考にした。享年は満年齢を基本としたが、出生・死亡日が不祥のものは数え年で表記したケースもある。\n", "pub_date": "2016-05-10T07:54
:49+00:00", "id": "blog.note.1"}

[2016-05-16 13:00:31,908: DEBUG/Worker-1] < {"took":20,"errors":false,"items":[{"index":{"_index":"haystack","_type":"modelresult","_id":"blog.note.1","_version":2,"_shards":{"total":2,"suc
cessful":1,"failed":0},"status":200}}]}
[2016-05-16 13:00:31,908: DEBUG/Worker-1] Converted retries value: False -> Retry(total=False, connect=None, read=None, redirect=0)
[2016-05-16 13:00:31,971: DEBUG/Worker-1] "POST /haystack/_refresh HTTP/1.1" 200 50
[2016-05-16 13:00:31,973: INFO/Worker-1] POST http://127.0.0.1:9200/haystack/_refresh [status:200 request:0.065s]
[2016-05-16 13:00:31,981: DEBUG/Worker-1] > None
[2016-05-16 13:00:31,989: DEBUG/Worker-1] < {"_shards":{"total":10,"successful":5,"failed":0}}
[2016-05-16 13:00:31,997: DEBUG/Worker-1] celery_haystack.tasks.CeleryHaystackSignalHandler[61a595fb-bda3-4381-9b6b-60d904c4cfbc]: Updated 'blog.note.1' (with blog.search_indexes.NoteIndex)
[2016-05-16 13:00:32,035: INFO/MainProcess] Task celery_haystack.tasks.CeleryHaystackSignalHandler[61a595fb-bda3-4381-9b6b-60d904c4cfbc] succeeded in 0.30063409009s: None

~~~
