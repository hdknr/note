django-floppyforms: Google Map で GeoDjangoのフィールド表示

## django-floppyforms GeoDjango

- [GeoDjango widgets](http://django-floppyforms.readthedocs.org/en/latest/geodjango.html)

~~~bash
$ pip install django-floppyforms
~~~

~~~py
INSTALLED_APPS += ('floppyforms', )
~~~

## modes.py: Venue

~~~py
from django.contrib.gis.db import models
~~~

~~~py
class Place(models.Model):
    location = models.PointField(null=True, blank=True, default=None)
    # ....

class Venue(Place):
    # ....
~~~

~~~py
In [2]: Venue.objects.get(id=4).location.geojson
Out[2]: '{"type": "Point", "coordinates": [139.6968165369083, 35.65804003941925]}'
~~~

## views.py

~~~py
def detail(request, id):
    venue = models.Venue.objects.get(id=id)

    # 表示だけどもfloppyformsのフォームをつくってレンダリングする
    form = forms.VenueForm(instance=venue)

    return TemplateResponse(
        request, 'maps/venue/detail.html',
        dict(request=request, instance=venue, form=form, venue=venue,))
~~~    

## forms.py

~~~py
import floppyforms
~~~

- Google Map をつかったPointウィジェット定義

~~~py
class GmapPointWidget(
        floppyforms.gis.BaseGMapWidget,
        floppyforms.gis.widgets.PointWidget):
    template_name = 'guides/gmap.html'    # Gooogle Mapカスタマイズ
~~~

- Venue のフォーム

~~~py
class VenueForm(floppyforms.ModelForm):
    class Meta:
        model = models.Venue
        exclude = []
        widgets = {
            'location': GmapPointWidget(attrs={
                'map_width': 1000, 'map_height': 700,
            }),
        }
~~~~        

## gmap.html

~~~html
{% extends "floppyforms/gis/openlayers.html" %}
{# http://django-floppyforms.readthedocs.org/en/latest/geodjango.html#javascript-library #}

{% block options %}
{{ block.super }}
// ここでGoogle Mapのオプションを設定する
options['base_layer'] = new OpenLayers.Layer.Google(
  "Google Streets", {numZoomLevels: 20, units: 'm'});
options['point_zoom'] = 20;
{% endblock %}
~~~

## venue/detail.html : 地図の表示

- 数行で表示されます

### headでアセット読み込み

~~~html
{% block head_style%}{{ block.super}}
<script src="{% static 'floppyforms/js/MapWidget.js' %}"></script>
{{ form.media }}      // 必須
{% endblock %}
~~~

- 以下の様にレンダリングされます

~~~html
<script src="/static/floppyforms/js/MapWidget.js"></script>
<script type="text/javascript" src="/static/floppyforms/openlayers/OpenLayers.js"></script>
<script type="text/javascript" src="/static/floppyforms/js/MapWidget.js"></script>
<script type="text/javascript" src="https://maps.google.com/maps/api/js?v=3&amp;sensor=false"></script>
~~~

### マップの表示

- 1行です

~~~html
{% block content %}
  ....
  {{ form.location }}
{% endblock %}
~~~

- レンダリング結果

~~~html
<style type="text/css">
	#id_location_map { width: 1000px; height: 700px; }
	#id_location_map .aligned label { float: inherit; }
	#id_location_span_map { position: relative; vertical-align: top; float: left; }
	#id_location { display: none; }
	.olControlEditingToolbar .olControlModifyFeatureItemActive {
		background-image: url("/static/admin/img/gis/move_vertex_on.png");
		background-repeat: no-repeat;
	}
	.olControlEditingToolbar .olControlModifyFeatureItemInactive {
		background-image: url("/static/admin/img/gis/move_vertex_off.png");
		background-repeat: no-repeat;
	}
</style>

<span id="id_location_span_map">
	<div id="id_location_map"></div>
	<a href="javascript:map_location.clearFeatures()">Delete all Features</a>

	<textarea name="location" rows="10" map_width="1000" map_height="700" cols="40" geom_type="POINT" id="id_location">POINT (15550978.4823299963027 4253669.654012895189226)</textarea>

	<script type="text/javascript">
		var map_options = {};

var options = {
			geom_type: OpenLayers.Geometry.Point,
			id: 'id_location',
			is_collection: false,
			is_linestring: false,
			is_point: true,
			is_polygon: false,
			map_id: 'id_location_map',
			map_options: map_options,
			map_srid: 3857,
			name: 'location'
		};
options['base_layer'] = new OpenLayers.Layer.Google(
  "Google Streets", {numZoomLevels: 20, units: 'm'});
options['point_zoom'] = 20;

var map_location = new MapWidget(options);
	</script>
</span>
~~~

## マーカーを追加するなど

- 生成された map_location に [OpenLayers 2 Marker](http://dev.openlayers.org/docs/files/OpenLayers/Marker-js.html) で追加します

~~~html
{% block bottom_script %} {{ block.super }}
<script>
{# http://dev.openlayers.org/docs/files/OpenLayers/Marker-js.html #}

// 座標系
var EPSG_4236 = new OpenLayers.Projection("EPSG:4326");
var EPSG_900913 = new OpenLayers.Projection("EPSG:900913");

// マーカーレイヤ
var markers = new OpenLayers.Layer.Markers( "Markers" );
map_location.map.addLayer(markers);

// アイコン
var size = new OpenLayers.Size(50,50);
var icon = new OpenLayers.Icon('/static/guides/plate7.512.png', size);

// Google Map用に変換した位置を作成
var p = {{ instance.location.geojson|safe }};   // Venue.location の位置
var pos = new OpenLayers.LonLat(
    p.coordinates[0], p.coordinates[1]).transform(EPSG_4236, EPSG_900913);

// マーカー
var mark = new OpenLayers.Marker(pos, icon);

// マーカー追加
markers.addMarker(mark);

</script>
{% endblock %}
~~~

![](https://raw.githubusercontent.com/hdknr/scriptogr.am/fcb11148fc517fdcb042efd8698e1c4a4b05a91b/django/geodjango/django-floppyforms.marker.png)
