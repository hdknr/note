# 管理プロセス

- https://12factor.net/admin-processes
- `Run admin/management tasks as one-off processes`

管理タスクのコマンド化:

~~~bash 
$ python manage.py migrate
~~~

Docker:

- docker run --rm ..

K8s:

- Job
- CronJob