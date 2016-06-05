## RelativeLayout : Header - Content - Footer

~~~bash
attribute,Hader,Content,Footer
id,@+id/header,@+id/content,@+id/footer
layout_width,fill_parent,fill_parent,fill_parent
layout_height,wrap_content,fill_parent,wrap_content
layout_above,,@+id/footer,
layout_below,,@+id/header,
layout_alignParentLeft,true,,
layout_alignParentTop,true,,
layout_alignParentBottom,,,true
layout_alignParentRight,,,true
~~~

- [今さら聞けないRelativeLayoutの話 ](http://qiita.com/yysk/items/c686153b39d32571d1bd)

## テキストのセンタリング

~~~xml
<TextView
        android:gravity="center" />
~~~

- center(垂直水平中央), center_vertical(垂直中央), center_horizontal (水平中央)

## LinerLayout でウィジェットの表示非表示

~~~csharp
    ListView OccupanceyList {
      get {
        return FindViewById<ListView>(Resource.Id.OccupancyList);}}

    public void SetOccupancy(List<Occupancy> occupancies)
		{
			if (_api != null) {
				if (occupancies.Count > 0) {
          // do somehting
					OccupanceyList.Visibility = ViewStates.Visible;

				} else {
					OccupanceyList.Visibility = ViewStates.Gone;
				}
			}
		}
~~~    

## 強制的にサイズを変更

~~~csharp
private int PixelsToDp(int pixels)
{
  //Android.Util
  return (int)TypedValue.ApplyDimension(
    ComplexUnitType.Dip, pixels, Resources.DisplayMetrics);
}
~~~

~~~csharp
myWidget.LayoutParameters.Height = PixelsToDp (300);
~~~
