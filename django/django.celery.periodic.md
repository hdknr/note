- [https://celery.readthedocs.org/en/latest/userguide/periodic-tasks.html](https://celery.readthedocs.org/en/latest/userguide/periodic-tasks.html)
	
	
## タイムゾーン

- `settings.USE_TZ` , `settings.TIME_ZONE` を見てくれます

## Beat

- `-B` でビートオプション
- `-s` でステートデータベースの指定

~~~
$ celery -A app.apps.celery worker -l info -B -s  celery.beat.schedule
~~~


## 定期タスクをコードで

~~~
from celery.schedules import crontab
from celery.task import periodic_task

@periodic_task(
	run_every=crontab(
		hour=7, minute=30, day_of_week="mon"))
def every_monday_morning():
    print("This is run every Monday morning at 7:30")
~~~    
