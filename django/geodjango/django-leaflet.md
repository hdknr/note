# django-leaflet

- [makinacorpus/django-leaflet](https://github.com/makinacorpus/django-leaflet)

# Install

~~~bash
$ pip install django-leaflet
~~~

# Configure

- settings.py

~~~py
# leaflet
INSTALLED_APPS += (
    'leaflet',
)
~~~

- templates/announce/detail.html

~~~html
{% load leaflet_tags %}
....
{% block head_script %}{{ block.super }}
  {% leaflet_js %}
  {% leaflet_css %}
{% endblock %}
...

{% block content %}
 ...
 {% if instance.place %}
   {% leaflet_map "place %}
 {% endif %
....
{% endblock %}

~~~

- レンダー

~~~html

...
<script src="/static/leaflet/leaflet.js" type="text/javascript"></script>
<script src="/static/leaflet/leaflet.extras.js" type="text/javascript"></script>
<script type="text/javascript">
    L.Control.ResetView.TITLE = "Reset view";
    L.Control.ResetView.ICON = "url(/static/leaflet/images/reset-view.png)";
</script>
<link rel="stylesheet" href="/static/leaflet/leaflet.css" />
<!--[if lte IE 8]>
    <link rel="stylesheet" href="/static/leaflet/leaflet.ie.css" />
<![endif]-->
<style>.leaflet-container-default {min-height: 300px;}</style>
....

<div id="place" class="leaflet-container-default"></div>
<script type="text/javascript">
(function () {

    function loadmap() {
        var djoptions = {"layers":
          [["OSM",
            "//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
            "\u00a9 <a href=\"http://www.openstreetmap.org/copyright\">OpenStreetMap</a> contributors"]],
            "minimap": false,
            "scale": "metric", "center": null, "tilesextent": [],
            "attributionprefix": null, "zoom": null, "maxzoom": null,
            "minzoom": null,
            "extent": [[-90, -180], [90, 180]],
            "resetview": true, "srid": null, "overlays": [],
            "fitextent": true
          },
          options = {djoptions: djoptions, initfunc: loadmap,
                       globals: false, callback: null};

        L.Map.djangoMap('place', options);
    }
    var loadevents = ["load"];

    if (loadevents.length === 0) loadmap();
    else if (window.addEventListener)
      for (var i=0; i<loadevents.length; i++)
        window.addEventListener(loadevents[i], loadmap, false);
    else if (window.jQuery)
      jQuery(window).on(loadevents.join(' '), loadmap);

})();
</script>
....
~~~~

## geojson をレンダリングする

~~~py
In [7]: instance.location
Out[7]: <Point object at 0x7fc1f2e71d00>

In [8]: instance.location.geojson
Out[8]: '{"type": "Point", "coordinates": [139.70238358286394, 35.6591961376129]}'
~~~

~~~html
{% block bottom_script %} {{ block.super }}
<script>
$(window).on('map:init', function (e) {
  var data = {{ instance.place.location.geojson|safe }};
  // var data = {"type": "Point", "coordinates": [139.70238358286394, 35.6591961376129]};
  var detail = e.originalEvent ? e.originalEvent.detail : e.detail;
  L.geoJson(data).addTo(detail.map);
});
</script>
{% endblock %}
~~~

## ズーム

~~~javascript
// detail = <div id="place_map" class="leaflet-container-default"></div>
detail.map.setZoom(13);
~~~

## センタリング

~~~javascript
detail.map.setView(
    new L.LatLng(data.coordinates[1], data.coordinates[0]),
    18);      // 同時にズーム
~~~


## 地図のサイズ指定

~~~css  
<style>
  .leaflet-container { width:  600px; height: 400px; }
  #specialbigmap { height: 800px; }
</style>
~~~
