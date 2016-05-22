## タスクをrevoke

- [revoke: Revoking tasks](http://docs.celeryproject.org/en/latest/userguide/workers.html#revoke-revoking-tasks)

~~~python
from celery.result import AsyncResult
r = AsyncResult('6d696bda-f2e8-4985-bc57-d237edf7f3c5')
r.revoke(terminate=True)1
~~~

## revoke リスト

~~~python
from celery.task.control import *
inspect().revoked()

{'celery@jessie.local': [
  '60c02542-9fd9-4f6f-8f15-1dd7e5688749',
  '60c02542-9fd9-4f6f-8f15-1dd7e5688749',
  '6d696bda-f2e8-4985-bc57-d237edf7f3c5']}
~~~

### statedb

- [settings.CELERYD_STATE_DB](http://docs.celeryproject.org/en/latest/configuration.html#celeryd-state-db)
- [worker --statedb {{ path }}](http://docs.celeryproject.org/en/latest/reference/celery.bin.worker.html#cmdoption-celery-worker-S)
