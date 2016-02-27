MKMapView: 多すぎる移動イベントを間引く

## マップの移動イベントが多すぎ

- MapView の RegionChange でイベントを拾う
- OnMapMovedでアノテーションとかルート描画するが、オブジェクトが多く動作が重い

~~~csharp
class MapDelegate : MKMapViewDelegate
{
  public override void RegionChanged (MKMapView mapView, bool animated)
  {
      OnMapMoved (mapView);
  }
}
~~~

## 簡易ジョブキューで処理を先送りさせる

- 1.5秒

~~~csharp
using System.Collections.Concurrent;
ConcurrentQueue<Point> MoveEventQueue = new ConcurrentQueue<Point> ();
~~~

~~~csharp
public void OnMapMoved(MKMapView map)
{
  MoveEventQueue.Enqueue (map.CenterCoordinate.ToPoint ());

  System.Threading.Tasks
    .Task.Delay (System.TimeSpan.FromSeconds (1.5))
    .ContinueWith (
    (task) => {
        // UI Thread
        InvokeOnMainThread (() => { MapMovedTo (map); });
    }
  );
}
~~~

##  キューが積まれているならば処理しない

- 最後のイベントだけ処理させる

~~~csharp
public void MapMovedTo(MKMapView map)
{
  Point pt;

  MoveEventQueue.TryDequeue (out pt);
  if (pt != null && MoveEventQueue.Count () > 0) {
    return;
  }
  RedrawAnnotaions(map);
}
~~~
