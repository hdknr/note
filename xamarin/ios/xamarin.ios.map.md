## 中心地にピンが立ってしまう

- MKMapViewDelegate でアノテーションのビューを返してしまっているとか

~~~csharp
public override MKAnnotationView GetViewForAnnotation (
  MKMapView mapView, IMKAnnotation annotation)
{
  bool enable_initial_pin = false;

  if (annotation is MKUserLocation)
    return null;

  if (annotation is MapObjAnnotation) {
    return (annotation as MapObjAnnotation).CreateView (mapView);
  }


  if (!enable_initial_pin)
      return null;

  // show pin annotation
  var anView = (MKPinAnnotationView)mapView.DequeueReusableAnnotation (pId);

  if (anView == null)
    anView = new MKPinAnnotationView (annotation, pId);

  ((MKPinAnnotationView)anView).PinColor = MKPinAnnotationColor.Red;
  anView.CanShowCallout = true;

  return anView;
}

~~~


# Info.plist: Maps Integration なしでもMapKIT 使えます

- "Maps Integration Enabled" にすると、

# アノテーションが多すぎ

- https://robots.thoughtbot.com/how-to-handle-large-amounts-of-data-on-maps

# 矢印を書く

- http://stackoverflow.com/questions/17829611/how-to-draw-an-arrow-between-two-points-on-the-map-mapkit
- http://stackoverflow.com/questions/13695317/rotate-a-point-around-another-point

# 描画

- http://glassonion.hatenablog.com/entry/20100623/1277246927
- MKPolyline, MKPolylineView
- MKPolygon , MKPolygonView
- MKCircle , MKCircleView

# 文字を描く

- http://stackoverflow.com/questions/1302824/iphone-how-to-draw-text-in-the-middle-of-a-rect

# 点線

# 線の太さ

`LineWidth`

- http://pinkstone.co.uk/how-to-draw-an-mkpolyline-on-a-map-view/
- http://stackoverflow.com/questions/32573756/mkmapview-draw-connected-lines-between-all-points
