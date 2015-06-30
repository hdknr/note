
## extra_info () でタスクリスト

- apps/worker.py

~~~
EXTRA_INFO_FMT = """                                                                
[tasks]                                                                             
{tasks}                                                                             
"""  
~~~

~~~
class Worker(WorkController):                                                    
	...
    def extra_info(self):                                                           
        if self.loglevel <= logging.INFO:                                           
            include_builtins = self.loglevel <= logging.DEBUG                       
            tasklist = self.tasklist(include_builtins=include_builtins)             
            return EXTRA_INFO_FMT.format(tasks=tasklist)                            

~~~

## tasklist()

~~~
    def tasklist(
    	self, include_builtins=True, 
    	sep='\n', int_='celery.'
    ):         
        return sep.join(                                                         
            '  . {0}'.format(task) 
            for task in sorted(self.app.tasks)            
            if (not task.startswith(int_) 
                if not include_builtins else task)     
        ) 
~~~
        
- self.app       

~~~
<class 'celery.app.base.Celery'>
~~~

- self.app.tasks

~~~
 {'dotnet.tasks.add': <@task: dotnet.tasks.add of app:0x7f26efa431d0>, 'celery.chain': <@task: celery.chain of app:0x7f26efa431d0>, 'ce
lery.chord': <@task: celery.chord of app:0x7f26efa431d0>, 'emailsmtp.tasks.save_inbound': <@task: emailsmtp.tasks.save_inbound of app:0x7f26efa431d0 (v2 compatible)>, 'celery.chord_
unlock': <@task: celery.chord_unlock of app:0x7f26efa431d0>, 'celery.chunks': <@task: celery.chunks of app:0x7f26efa431d0>, 'emailsmtp.tasks.send_messages': <@task: emailsmtp.tasks.
send_messages of app:0x7f26efa431d0 (v2 compatible)>, 'emailsmtp.tasks.send_raw_message': <@task: emailsmtp.tasks.send_raw_message of app:0x7f26efa431d0 (v2 compatible)>, 'celery.gr
oup': <@task: celery.group of app:0x7f26efa431d0>, 'celery.backend_cleanup': <@task: celery.backend_cleanup of app:0x7f26efa431d0>, 'celery.map': <@task: celery.map of app:0x7f26efa
431d0>, 'emailsmtp.tasks.hello': <@task: emailsmtp.tasks.hello of app:0x7f26efa431d0>, 'celery.starmap': <@task: celery.starmap of app:0x7f26efa431d0>, 'accounts.tasks.add': <@task:
 accounts.tasks.add of app:0x7f26efa431d0>, 'emailsmtp.tasks.process_inbound': <@task: emailsmtp.tasks.process_inbound of app:0x7f26efa431d0 (v2 compatible)>}
~~~  

## この tasks が shellの内容と一致しない

~~~
>>> from django.apps import apps
>>> c = apps.get_app_config('app').celery
~~~

~~~
>>> c.tasks
{'celery.chain': <@task: celery.chain of app:0x7f69a2731390>, 'celery.chord': <@task: celery.chord of app:0x7f69a2731390>, 'celery.chunks': <@task: celery.chunks of app:0x7f69a2731390>, 'celery.chord_unlock': <@task: celery.chord_unlock of app:0x7f69a2731390>, 'celery.group': <@task: celery.group of app:0x7f69a2731390>, 'celery.backend_cleanup': <@task: celery.backend_cleanup of app:0x7f69a2731390>, 'celery.map': <@task: celery.map of app:0x7f69a2731390>, 'celery.starmap': <@task: celery.starmap of app:0x7f69a2731390>}
~~~

- ワーカーはなんかやってる？

## コールスタック

- extra_info()
- on_start()

- [Extensions and Bootsteps](http://docs.celeryproject.org/en/latest/userguide/extending.html)

### celery.bootsteps

- [celery.bootsteps](https://celery.readthedocs.org/en/latest/reference/celery.bootsteps.html)

### celery.worker

- [celery.worker](http://docs.celeryproject.org/en/latest/reference/celery.worker.html)

## autodiscover_tasks(apps, force=True) でいけるっぽい

~~~
>>> from app.apps import celery_app
>>> a = celery_app()
~~~

~~~
>>> from django.conf import settings
~~~
~~~
>>> a.autodiscover_tasks(settings.INSTALLED_APPS,force=True)
>>> a.tasks
{'dotnet.tasks.add': <@task: dotnet.tasks.add of app:0x7f54af128f90>, 'celery.chain': <@task: celery.chain of app:0x7f54af128f90>, 'celery.chord': <@task: celery.chord of app:0x7f54af128f90>, 'celery.chunks': <@task: celery.chunks of app:0x7f54af128f90>, 'celery.chord_unlock': <@task: celery.chord_unlock of app:0x7f54af128f90>, 'emailsmtp.tasks.save_inbound': <@task: emailsmtp.tasks.save_inbound of app:0x7f54af128f90 (v2 compatible)>, 'emailsmtp.tasks.send_messages': <@task: emailsmtp.tasks.send_messages of app:0x7f54af128f90 (v2 compatible)>, 'emailsmtp.tasks.send_raw_message': <@task: emailsmtp.tasks.send_raw_message of app:0x7f54af128f90 (v2 compatible)>, 'celery.group': <@task: celery.group of app:0x7f54af128f90>, 'celery.backend_cleanup': <@task: celery.backend_cleanup of app:0x7f54af128f90>, 'celery.map': <@task: celery.map of app:0x7f54af128f90>, 'emailsmtp.tasks.hello': <@task: emailsmtp.tasks.hello of app:0x7f54af128f90>, 'celery.starmap': <@task: celery.starmap of app:0x7f54af128f90>, 'accounts.tasks.add': <@task: accounts.tasks.add of app:0x7f54af128f90>, 'emailsmtp.tasks.process_inbound': <@task: emailsmtp.tasks.process_inbound of app:0x7f54af128f90 (v2 compatible)>}
~~~

## だれか調べてる

> I just found that the strange thing is when I specify "force=True" in autodiscover_tasks(), then it works fine. 

> By checking celery codes, it seems this parameter will cause self._autodiscover_tasks() called immediately, by default it just postpond until some signal received, so I assume this parameter is optimized for using with django only to implement lazy module loading, but still I have no idea why it failed in signal handler. – 

- [celery autodiscover_tasks not working for ValueError: Empty module name](https://stackoverflow.com/questions/29493344/celery-autodiscover-tasks-not-working-for-valueerror-empty-module-name)

### celery/app/base.py

~~~
class Celery(object):                                                            
	...
    def autodiscover_tasks(
    	self, packages, related_name='tasks', 
    	force=False
    ):   
        if force:                                                                   
            return self._autodiscover_tasks(
            	packages, related_name)   
            	              
        signals.import_modules.connect(
        	promise(                                     
            	self._autodiscover_tasks, 
            	(packages, related_name),                     
        	), 
        	weak=False, sender=self)  
~~~        