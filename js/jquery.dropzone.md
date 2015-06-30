## bower install
~~~
(wordpress)vagrant@10:~/projects/pia/web/pia$ python ../manage.py bower install
bower stickyjs#*            not-cached git://github.com/dawidziak/stickyjs.git#*
...
bower dropzone#*                     not-cached git://github.com/enyo/dropzone.git#*
bower dropzone#*                        resolve git://github.com/enyo/dropzone.git#*
bower elusive-iconfont#*               checkout master
bower dropzone#*                       download https://github.com/enyo/dropzone/archive/v4.0.1.tar.gz
bower stickyjs#*                       resolved git://github.com/dawidziak/stickyjs.git#93f682f415
bower elusive-iconfont#*               resolved git://github.com/aristath/elusive-iconfont.git#32ce6ffca3
bower dropzone#*                        extract archive.tar.gz
bower dropzone#*                       resolved git://github.com/enyo/dropzone.git#4.0.1
bower dropzone#~4.0.1                   install dropzone#4.0.1

dropzone#4.0.1 bower_components/dropzone

~~~

## collectstaic

~~~
(wordpress)vagrant@10:~/projects/pia/web/pia$ python ../manage.py collectstatic

You have requested to collect static files at the destination
location as specified in your settings:

    /home/vagrant/projects/pia/web/static

This will overwrite existing files!
Are you sure you want to do this?

Type 'yes' to continue, or 'no' to cancel: yes
Copying '/home/vagrant/projects/pia/web/components/bower_components/dropzone/bower.json'
Copying '/home/vagrant/projects/pia/web/components/bower_components/dropzone/dist/dropzone.js'
Copying '/home/vagrant/projects/pia/web/components/bower_components/dropzone/dist/readme.md'
Copying '/home/vagrant/projects/pia/web/components/bower_components/dropzone/dist/dropzone.css'
Copying '/home/vagrant/projects/pia/web/components/bower_components/dropzone/dist/dropzone-amd-module.js'
Copying '/home/vagrant/projects/pia/web/components/bower_components/dropzone/dist/basic.css'
Copying '/home/vagrant/projects/pia/web/components/bower_components/dropzone/dist/min/dropzone-amd-module.min.js'
Copying '/home/vagrant/projects/pia/web/components/bower_components/dropzone/dist/min/basic.min.css'
Copying '/home/vagrant/projects/pia/web/components/bower_components/dropzone/dist/min/dropzone.min.css'
Copying '/home/vagrant/projects/pia/web/components/bower_components/dropzone/dist/min/dropzone.min.js'

10 static files copied to '/home/vagrant/projects/pia/web/static', 2108 unmodified.
~~~

