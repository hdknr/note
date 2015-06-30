## いろいろ

### easy.cmdopts と easy.consume_argsは同時に使えないっぽい

- cusume_argに取られてしまう

~~~python

@easy.task
@easy.consume_args
@easy.cmdopts([
    ('username=', 'u', 'Username to use when logging in to the servers'),
])
def runserver(args, options):
    ''' Run Django Web Application '''
    print ">>>", args, options
	....
~~~


~~~bash

$ paver runserver ikki   --username=user 
---> pavement.runserver

>>> ['ikki', '--username=user'] Namespace(args=['ikki', '--username=user'], dry_run=None, pavement_file='pavement.py')

~~~

