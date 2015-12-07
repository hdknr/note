GeoDjango Database Functions
==============================

.. list-table::

    *   - Area
        - 地理フィールドや表現を受け取る
        - `Area <https://docs.djangoproject.com/en/1.9/ref/contrib/gis/measure/#django.contrib.gis.measure.Area>`_
          を返す

    *   - AsGeoJSON
        - 地理フィールドや表現を受け取る
        - `GeoJSON <http://geojson.org/>`_ を返す


    *   - AsGML
        - 地理フィールドや表現を受け取る
        - `GML <https://en.wikipedia.org/wiki/Geography_Markup_Language>`_ を返す

    *   - AsKML
        - 地理フィールドや表現を受け取る
        - `KML <https://developers.google.com/kml/documentation/>`_ を返す

    *   - AsSVG
        -
        - `SVG <http://www.w3.org/Graphics/SVG/>`_ を返す

    *   - BoundingCircle
        - 
        - 最小の円ポリゴンを返す

    *   - Centroid
        -
        - centroid(重心，中心軌跡，図心，質量中心) 値を返す

    *   - Difference
        - (A, B)２つの地理フィールドや表現を受け取る
        - 地理的差分を返す(Bに交わらないA)

    *   - Distance
        - (A, B)２つの地理フィールドや表現を受け取る
        - 距離を返す

    *   - Envelope
        - 
        - 境界ボックスを返す

    *   - ForceRHR
        -
        - ポリゴンを右ハンドル交通ルールで返す

    *   - GeoHash
        - 
        - `Geohash <https://en.wikipedia.org/wiki/Geohash>`_ を返す

    *   - Intersection
        - (A, B)２つの地理フィールドや表現を受け取る
        - 共通部分を返す

    *   - Length
        - 
        - `Distance <https://docs.djangoproject.com/en/1.9/ref/contrib/gis/measure/#django.contrib.gis.measure.Distance>`_  で長さを返す

    *   - MemSize
        -
        - 地理データのバイト数を返す

    *   - NumGeometries
        - 
        - 地理データコレクションの要素数を返す

    *   - NumPoints
        -
        - ポイント数を返す

    *   - Perimeter
        - 
        - 周囲を `Distance <https://docs.djangoproject.com/en/1.9/ref/contrib/gis/measure/#django.contrib.gis.measure.Distance>`_ で返す

    *   - PointOnSurface
        -
        - 表面上のPointを返す

    *   - Reverse
        - 
        - 逆座標で返す

    *   - Scale
        - x, y, z でスケールを指定 
        - スケール計算して返す

    *   - SnapToGrid
        - 
        -
    
    *   - SymDifference
        - (A, B)２つの地理フィールドや表現を受け取る
        - 対称差分(?)  

    *   - Transform
        - SRID
        - 指定されたSRIDに変換する

    *   - Translate
        - x, y, z
        - 指定された x, y, zでオフセットさせる

    *   - Union
        - 
        - 和を返す
