GeoDjango: ルート上に位置補正(案)

- 現在地がずれて報告されたときに、定られた経路上に補正したい
- 経路からの距離をもとめて、報告位置からの円をつくる
- 円と交わった線分の中心地を補正位置とする
- 円の半径は得られた距離より広めにとって交わるようにする

## Station: 次の駅までの経路情報を持たせる

~~~py
class Station(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    '''駅の場所'''
    route = models.MultiLineStringField(
        null=True, blank=True, default=None,)
    '''次の駅までのルート'''
~~~

- 位置情報

~~~py
class Place(models.Model):
    name = models.CharField(max_length=50)
    location = models.PointField()
~~~

- 渋谷駅の次駅(原宿駅)までの経路

~~~py
from maps.models import *
shibuya = Station.objects.get(id=4)
print shibuya.route.json

'{"type": "MultiLineString", "coordinates":
[
[
[139.70290249127422, 35.65853244841824],
[139.70220578977614, 35.660106185584475],
[139.70233453581062, 35.666122196250748],
[139.70220578977614, 35.661849580175264],
[139.70083249876564, 35.6624248920371],
[139.70087541410746, 35.663017633256636],
[139.701240194531, 3566122196250748],
[139.702.663505769779796],
[139.7013903982364, 35.664499467052565],
[139.69892276594632, 35.66474353115777],
[139.70023168394405, 35.66606843756664],
[139.70102561781286,596],
[139.70364, 35.4996 35.66666115173598],
[139.70184100935262, 35.666783180577326],
[139.70205558607074, 35.66917142178526],
[139.70287097761047, 35.66953749623893],
[139.702828062268 01841009352677326], 020565, 35.67018248047786]]]}'
~~~

![](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/django/geodjango/geodjango.route.correction.route.png)

- 神南小学校

~~~py
jinsho = Place.objects.get(id=8)
print jinsho.location.json
{"type": "Point", "coordinates": [139.6980199665418, 35.66322098512026]}
~~~

![](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/django/geodjango/geodjango.route.correction.location.png)


## 経路中に補正する

- 距離

~~~py
d = shibuya.route.distance(jinsho.location)     
~~~

- 少し広めの円

~~~py
circle = jinsho.location.buffer(d + 0.00001)
print type(circle)
<class 'django.contrib.gis.geos.polygon.Polygon'>
~~~

- 交わる線

~~~py
line = circle.intersection(shibuya.route)
print type(line)
<class 'django.contrib.gis.geos.linestring.LineString'>
~~~

- その中心が大体補正された場所

~~~py
print line.centroid.json
{"type": "Point", "coordinates": [139.69893397721165, 35.6647436800696]}
~~~

![](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/django/geodjango/geodjango.route.correction.corrected.png)

