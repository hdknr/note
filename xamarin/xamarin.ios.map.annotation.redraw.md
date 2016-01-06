MapKIT:  マップのアノテーションを移動する

- アノテーションを選択直後に選択解除すると再描画してくれる模様

~~~csharp

using System;

using UIKit;
using CoreGraphics;
using CoreLocation;

using Xamarin.Forms;
using Xamarin.Forms.Maps.iOS;
using Xamarin.Forms.Platform.iOS;

[assembly:ExportRenderer( // Xamarin.Forms Dependency Injection         
  typeof(HelloXamap.HelloMap),
  typeof(HelloXamap.iOS.HelloMapRenderer))
]
public class HelloMapRenderer : MapRenderer
{
  // MapKITのマップビュー
  private MKMapView _native_map {
    get { return (this.NativeView as MapRenderer).Control as MKMapView; } }

  // アノテーション(MKAnnotationサブクラス)
  public Bike _running_bike = new Bike (
    new CLLocationCoordinate2D(35.658987, 139.702776),
    "渋谷", "City of Light");

  // とりあえずタイマーをトリガーにする
  System.Timers.Timer _timer = new System.Timers.Timer (1000.0);

  public HelloMapRenderer():base(){

    _timer.Elapsed +=  (
      object sender,
      System.Timers.ElapsedEventArgs ev
    ) =>  {
      // 位置変更(北東に斜めに移動)
      _running_bike.SetCoordinate (new CLLocationCoordinate2D (
        _running_bike.Coordinate.Latitude + 0.001,
        _running_bike.Coordinate.Longitude + 0.001));

      BeginInvokeOnMainThread(delegate {  // UIの命令を呼ぶおまじない
        // 選択 & 解除　すると再描画される模様
        _native_map.SelectAnnotation(_running_bike, true);
        _native_map.DeselectAnnotation(_running_bike,true);
      });

    };
    _timer.Enabled = true;
    _timer.Start ();
  }
}
~~~
