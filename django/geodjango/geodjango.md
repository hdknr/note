# GeoDjango

- [GeoDjango](https://docs.djangoproject.com/en/1.9/ref/contrib/gis/)
- [GeoDjango Model API](https://docs.djangoproject.com/en/1.9/ref/contrib/gis/model-api/#module-django.contrib.gis.db.models)
- [GeoQuerySet API Reference](https://docs.djangoproject.com/en/1.9/ref/contrib/gis/geoquerysets /)
- [GeoDjango Admin UI](https://docs.djangoproject.com/en/1.9/ref/contrib/gis/admin/#module-django.contrib.gis.admin)
- [GeoDjango Database Function](https://docs.djangoproject.com/en/1.9/ref/contrib/gis/functions/)

- [GeoDjango in a nutshell](http://www.slideshare.net/DjangoStars/geodjango-in-a-nutshell)

- [makinacorpus/django-leaflet](https://github.com/makinacorpus/django-leaflet)
- [django-location-field](https://github.com/caioariede/django-location-field)
- [django-geoposition](https://django-geoposition.readthedocs.org/en/latest/)   ([github](https://github.com/philippbosch/django-geoposition))
- [Edit Django geometries fields with Leaflet](http://blog.mathieu-leplatre.info/edit-django-geometries-fields-with-leaflet.html)
- [Adding a polygon directly in Geodjango/PostGIS](http://stackoverflow.com/questions/1504288/adding-a-polygon-directly-in-geodjango-postgis)

GoogleMap:

- [GeoDjangoの管理画面でGoogle Mapsを使う](http://qiita.com/key/items/f3206e701238f187e759)
- [lxdiyun/django_util/templates/admin/](https://github.com/lxdiyun/django_util/tree/master/templates/admin)



## Related

- [Polymaps](http://polymaps.org/) (Polymaps is a free JavaScript library for making dynamic, interactive maps in modern web browsers.)
- [Mapbox](https://www.mapbox.com/mapbox.js/api/v2.2.3/)(Build anything with Mapbox.js,
a library for fast & interactive maps.)
- [MapServer](http://mapserver.org/)
- http://featureserver.org/
- http://tilecache.org/
- http://tilestache.org/
- [PostGISでよく使うSRIDまとめ : してログ](http://landhere.info/blog/a79.html)
- [EPSG:4326](http://spatialreference.org/ref/epsg/wgs-84/)

# GeoJSON

- [GeoJSON](http://geojson.org/)
- [Wikipedia](https://ja.wikipedia.org/wiki/GeoJSON)
- [Google Map上にGeoJSONデータを表示する](http://shimz.me/blog/google-map-api/3445)

# PostGIS

[PostGIS](http://postgis.net/):
- [GEOS](https://docs.djangoproject.com/en/1.9/ref/contrib/gis/install/geolibs/#geosbuild)
- [PROJ.4](https://github.com/OSGeo/proj.4/wiki)
- [GDAL](https://docs.djangoproject.com/en/1.9/ref/contrib/gis/gdal/)

# その他

- [How to get the nearest point on a linestring to a given point?](http://gis.stackexchange.com/questions/2061/how-to-get-the-nearest-point-on-a-linestring-to-a-given-point)
- [PostGISのよく使う機能をまとめた](http://d.hatena.ne.jp/EulerDijkstra/20131008/1381190780)
- [Django Rest Framework GISで誰でも簡単RESTful Geo API](http://monomoti.hatenablog.jp/entry/2015/12/15/000000)

# サンプル

- [lxdiyun/geodjango_google](https://github.com/lxdiyun/geodjango_google)
- [cauethenorio/geodjango-gmaps-widget](https://github.com/cauethenorio/geodjango-gmaps-widget)

# Database

## sqlite

- [地図とかの空間情報をSQLiteに格納するSpatiaLiteを使用してみる](http://qiita.com/mima_ita/items/64f6c2b8bb47c4b5b391)
- [Installing Spatialite](https://docs.djangoproject.com/en/1.9/ref/contrib/gis/install/spatialite/)
- [lokkju/pyspatialite
](https://github.com/lokkju/pyspatialite/)

~~~bash
$ sudo apt-get install libspatialite-dev

Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following extra packages will be installed:
  libfreexl1 libgeos-3.4.2 libgeos-c1 libproj0 libspatialite5 proj-data
Suggested packages:
  proj-bin
The following NEW packages will be installed:
  libfreexl1 libgeos-3.4.2 libgeos-c1 libproj0 libspatialite-dev
  libspatialite5 proj-data
0 upgraded, 7 newly installed, 0 to remove and 3 not upgraded.
Need to get 4,457 kB of archives.
After this operation, 22.5 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
~~~

TODO:

- pip でビルドエラーが起きる(Ubuntu LTS 14.04)

## MySQL

- [MySQL Spatial Limitations](https://docs.djangoproject.com/en/dev/ref/contrib/gis/db-api/#mysql-spatial-limitations)

~~~py
INSTALLED_APPS += (
  'django.contrib.gis',           # GeoDjango
)
~~~

~~~bash
$ echo "CREATE TABLE geom (g GEOMETRY);" | DJ dbshell
$ echo "desc geom" | DJ dbshell

Field   Type    Null    Key     Default Extra
g       geometry        YES             NULL
~~~

~~~
AttributeError: 'DatabaseOperations' object has no attribute 'geo_db_type'
~~~


## PostgreSQL

- パッケージ(Ansible playbook task)

~~~yaml
- name: install postgresql
  sudo: true
  apt: name={{item}} state=latest
  with_items:
    - postgresql
    - libpq-dev
    - postgis
    - postgresql-9.3-postgis-scripts
~~~

- データベース(SUPERUSER権限がないとmigrateできない)

~~~yaml
- name: create PostgreSQL database
  postgresql_db:
    name: "{{ sample_db_name }}"
    encoding: "UTF-8"
    login_user: postgres
  sudo_user: postgres
  sudo: yes

- name: create user
  postgresql_user:
      db: "{{ sample_db_name}}"
      name: "{{ sample_db_user}}"
      password: "{{ sample_db_password }}"
      priv: ALL
      state: present
      role_attr_flags: CREATEDB,CREATEROLE,SUPERUSER
      login_user: postgres
  sudo_user: postgres
  sudo: yes
~~~  

- settings.py

~~~python
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
         #...
    }
}

INSTALLED_APPS += (
    'django.contrib.gis',           # GeoDjango
)
~~~

- 確認

~~~sql
geosampl=# select * from dlf_app_location;
 id |  city   |                      location                      | parent_place_id
----+---------+----------------------------------------------------+-----------------
  1 | shibuya | 0101000020E61000003716140665766140325706D506D54140 |                
(1 row)
~~~

~~~py
In [1]: from dlf_app.models import *
In [2]: shibuya = Location.objects.first()
In [3]: shibuya.location.json
Out[3]: '{"type": "Point", "coordinates": [139.699832, 35.664271]}''
In [4]: shibuya.location[0]
Out[4]: 139.699832
In [5]: shibuya.location[1]
Out[5]: 35.664271
~~~

- スキーマ

~~~sql

geosampl=# \d+ dlf_app_location;
                                                         Table "public.dlf_app_location"
     Column      |          Type          |                           Modifiers                           | Storage  | Stats target | Description
-----------------+------------------------+---------------------------------------------------------------+----------+--------------+-------------
 id              | integer                | not null default nextval('dlf_app_location_id_seq'::regclass) | plain    |              |
 city            | character varying(255) | not null                                                      | extended |              |
 location        | geometry(Point,4326)   | not null                                                      | main     |              |
 parent_place_id | integer                |                                                               | plain    |              |

Indexes:
    "dlf_app_location_pkey" PRIMARY KEY, btree (id)
    "dlf_app_location_07ba61e2" btree (parent_place_id)
    "dlf_app_location_location_id" gist (location)
Foreign-key constraints:
    "dlf_app_locatio_parent_place_id_9cbab696_fk_dlf_app_location_id" FOREIGN KEY (parent_place_id) REFERENCES dlf_app_location(id) DEFERRABLE INITIALLY DEFERRED
Referenced by:
    TABLE "dlf_app_location" CONSTRAINT "dlf_app_locatio_parent_place_id_9cbab696_fk_dlf_app_location_id" FOREIGN KEY (parent_place_id) REFERENCES dlf_app_location(id) DEFERRABLE INITIALLY DEFERRED
Has OIDs: no
~~~
