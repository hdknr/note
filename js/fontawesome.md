## fontawesome animation

- [Font Awesome Animation](https://l-lin.github.io/font-awesome-animation/) ([github](https://github.com/l-lin/font-awesome-animation))
- [sample](https://l-lin.github.io/font-awesome-animation/demo/partials/usage.html)

### djanog-bower

~~~
BOWER_INSTALLED_APPS = (                                                            
    'fontawesome',                                                                  
    'font-awesome-animation',                                                       
)  
~~~
~~~
$ python manage.py bower install
$ python manage.py collectstatic
~~~

~~~
<link href="{{ STATIC_URL }}fontawesome/css/font-awesome.css" rel="stylesheet">
<link href="{{ STATIC_URL }}font-awesome-animation/dist/font-awesome-animation.min.css" rel="stylesheet">
~~~
