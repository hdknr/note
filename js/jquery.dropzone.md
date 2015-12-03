## dropzone.js

- [dropzone](http://www.dropzonejs.com/)

- [dropzone.js の基本的な使い方](http://d.hatena.ne.jp/pospome/20130913/1379050713)
- [DROPZONEJS + DJANGO: HOW TO BUILD A FILE UPLOAD FORM](https://amatellanes.wordpress.com/2013/11/05/dropzonejs-django-how-to-build-a-file-upload-form/)
- [Batch Image Upload with Drag & Drop in the Django Admin](http://www.mechanicalgirl.com/post/batch-image-upload-drag-and-drop-django-admin/)
- [Dropzone + Django](https://alexanderae.com/dropzonejs-django.html)
- [Dropzone in Django - Stackoverflow](https://stackoverflow.com/questions/26143550/dropzone-in-django
- [sigurdga/django-dropzone-upload](https://github.com/sigurdga/django-dropzone-upload)

## requirements.txt

~~~
Django
bambu-bootstrap
beautifulsoup4
django-bootstrap3
django-bower
~~~

~~~bash
$ pip install -r requirements.txt
~~~

## app/settings.py

~~~py
from django.conf import global_settings

MEDIA_ROOT = os.path.join(BASE_DIR, 'medias/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# django-bower と bambu_bootstrapを追加する
INSTALLED_APPS += (
    'bootstrap3',       # django-bootstrap3
    'djangobower',      # django-bower
    'bambu_bootstrap',  # bambu
)
# django-bower でスタティクファイルを扱う
STATICFILES_FINDERS = global_settings.STATICFILES_FINDERS + (
    'djangobower.finders.BowerFinder',
)

# インストール先
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components/')

# bowerでインストールするnode.js パケージ
BOWER_INSTALLED_APPS = (
    'bootstrap',
    'fontawesome',
    'jquery-ui',
    'lightbox2',
    'dropzone',         # これです
)
~~~



## bower install

~~~bash
$ python ../manage.py bower install

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
$ python ../manage.py collectstatic

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


## accounts サンプルアプリケーション

- app/urls.py

~~~py
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
]
~~~

- app/settings.py

~~~py
INSTALLED_APPS += (
    'accounts',
)
~~~

~~~bash
$ tree accounts/ -I *.pyc

accounts/
├── __init__.py
├── admin.py
├── forms.py
├── migrations
│   ├── 0001_initial.py
│   └── __init__.py
├── models.py
├── templates
│   └── accounts
│       └── profile
│           └── upload_picture.html
├── tests.py
├── urls.py
└── views.py
~~~

- accounts/models.py

~~~py
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    photo = models.ImageField(_("Photo"), upload_to='profile_photo')

~~~

- accounts/admin.py

~~~
from django.contrib import admin
form .models import Profile

admin.site.register(Profile)
~~~

- accounts/forms.py

~~~py
from django import forms
from . import models


class ProfileForm(forms.ModelForm):

    class Meta:
        model = models.Profile
        fields = ('photo',)
~~~

- accounts/urls.py

~~~py
from django.conf.urls import url

urlpatterns = [
    url(r'^profile/picture$',
        'accounts.views.profile_upload_picture',
        name='accounts_profile_upload_picture'),
]
~~~

- accounts/views.py

~~~py
from django.shortcuts import render_to_response as render
from django.template import RequestContext as ctx

from .forms import ProfileForm


def profile_upload_picture(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profiile = form.save()
        else:
            print form.errors
    else:
        form = ProfileForm()

    return render("accounts/profile/upload_picture.html",
                  locals(), ctx(request))
~~~

- accounts/templates/accounts/profile/upload_picture.html

~~~html
{% load static %}

<html>
    <head>
        <link rel="stylesheet" href="{% static 'dropzone/dist/dropzone.css' %}">
    </head>

    <body>
        <form action="{% url 'accounts_profile_upload_picture' %}" method='POST'
         class="dropzone"                 // dropzone!!!
         id="myDropzone"              
         enctype="multipart/form-data">
            {% csrf_token %}

            <div class="fallback">
                <input name="photo" type="file" multiple />
            </div>
        </form>

        <script src="{% static 'dropzone/dist/dropzone.js' %}"></script>
        <script type="text/javascript">
            Dropzone.options.myDropzone = {
                paramName: "photo",     // POST
                autoProcessQueue : true,
                parallelUploads: 1,

                init: function() {
                    this.on("success", function(file, responseText) {
                        console.log(responseText);
                    });
                }
            };
        </script>
    </body>
</html>
~~~
