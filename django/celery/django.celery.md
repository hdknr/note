## revoke

~~~
[2015-09-01 17:28:34,747: WARNING/MainProcess] celery@jessie.local ready.
[2015-09-01 17:28:35,723: INFO/MainProcess] Received task: emailsmtp.tasks.send_mail[47332760-7456-4987-808c-fb0db8c1789d] eta:[2015-09-02 02:05:00+09:00]
~~~

~~~
$ celery -A app.apps.celery inspect scheduled
-> celery@jessie.local: OK

    {'priority': 6, 'eta': '2015-09-02T02:05:00+09:00', 
     'request': {
     	'args': '[1, None]', 
     	'time_start': None, 'name': 
     	'emailsmtp.tasks.send_mail', 
		'delivery_info': {
			'priority': None, 
			'redelivered': True, 
			'routing_key': 'sandbox', 
			'exchange': 'sandbox'}, 
		'hostname': 'celery@jessie.local', 
		'acknowledged': False, 
		'kwargs': '{}', 
		'id': '47332760-7456-4987-808c-fb0db8c1789d', 
		'worker_pid': None
		}
	 }
~~~
   
~~~python
>>> from app.apps import celery
>>> celery.app.control.revoke('47332760-7456-4987-808c-fb0db8c1789d')
~~~

~~~
[2015-09-01 17:29:16,027: INFO/MainProcess] Tasks flagged as revoked: 47332760-7456-4987-808c-fb0db8c1789d
~~~

~~~bash
$ celery -A app.apps.celery inspect revoked
-> celery@jessie.local: OK
    * 47332760-7456-4987-808c-fb0db8c1789d
~~~

ここで、ワーカーを落として、立ち上げるとタスクが復活してしまう。

