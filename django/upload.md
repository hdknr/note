# FileField クラス


## ファイル名の生成

- [generate_filename method](https://github.com/django/django/blob/master/django/db/models/fields/files.py#L328)

~~~
   def generate_filename(self, instance, filename):                                
       return os.path.join(
            self.get_directory_name(),
            self.get_filename(filename))
~~~

### ディレクトリ名

- [get_directory_name](https://github.com/django/django/blob/master/django/db/models/fields/files.py#L322)
- upload_to は callable もしくは空の文字列(デフォルト)

~~~
    def get_directory_name(self):
        return os.path.normpath(
             force_text(datetime.datetime.now().strftime(
                 force_str(self.upload_to))))
~~~

- デフォルトは空もじ列なので

~~~
>>> import datetime
>>> datetime.datetime.now().strftime('')
''
~~~

### ファイル名

- [get_filename](https://github.com/django/django/blob/master/django/db/models/fields/files.py#L325)

~~~
    def get_filename(self, filename):
        return os.path.normpath(
            self.storage.get_valid_name(
                os.path.basename(filename)))
~~~
	
## upload_to の指定

- [__init__](https://github.com/django/django/blob/master/django/db/models/fields/files.py#L241)

~~~
    def __init__(self, 
    		verbose_name=None, 
    		name=None, upload_to='', storage=None, **kwargs):
    	 ...
        self.upload_to = upload_to
        if callable(upload_to):
            self.generate_filename = upload_to
        ...            
~~~        	
