Xamarin.Forms: iOSでアノテーションのドラッグドロップ

## Xamarin.Forms でマップを定義

~~~csharp
using System;
using Xamarin.Forms;
using Xamarin.Forms.Maps;

namespace HelloXamap
{
	public class HelloMap : Map
	...
}
~~~

## カスタムレンダラ定義

- iOS用のカスタムレンダラ

~~~csharp
[assembly:ExportRenderer(
	typeof(HelloXamap.HelloMap),
	typeof(HelloXamap.iOS.HelloMapRenderer))]

namespace HelloXamap.iOS
{
	public class HelloMapRenderer : MapRenderer
	{
		private MKMapView _native_map {
			get { return (this.NativeView as MapRenderer).Control as MKMapView; } }

  }
~~~  

## アノテーション

~~~csharp
using System;

using MapKit;
using CoreLocation;


namespace HelloXamap.iOS
{
	public class Bike : MKAnnotation{
	....
}
~~~

## カスタムレンダラでアノテーションを追加

~~~csharp
public class HelloMapRenderer : MapRenderer {
	protected override void OnElementChanged (ElementChangedEventArgs<View> e)
	{
			var location = new CLLocationCoordinate2D(35.658987, 139.702776);
			var bike = new Bike(location, "Shibuya", "City of Light");

			// 追加
			_native_map.AddAnnotation(bike);

			// 追加されたら、ドラッグ可能にする。
			// この時点でドラッグドロップのUI処理は勝手にやってくれます
			_native_map.DidAddAnnotationViews += (
					object sender,
					MKMapViewAnnotationEventArgs ae
			) => {
				foreach(var v in ae.Views){
					v.Draggable=true;
				}
			};

			// ドラッグイベントの検知
			_native_map.ChangedDragState += (
				object cs,
				MKMapViewDragStateEventArgs ce
			) => {
					if(ce.NewState == MKAnnotationViewDragState.Starting ){
							Console.WriteLine("dragging.....");
							return ;
					}
					if(ce.NewState == MKAnnotationViewDragState.Ending){
							Console.WriteLine("draged!!!!!");
							return ;
					}
			};
			//.....
	}
}
~~~
