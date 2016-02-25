# Interface builder

- http://qiita.com/hayashi311/items/14ddfa146a83139c41fc

#Launch Screen

- http://baranoheyade.hateblo.jp/entry/2014/11/27/154128

# WebView

- http://qiita.com/amay077/items/ada1a4ead6bf8b2400fa

# Annotation


- https://developer.xamarin.com/guides/ios/platform_features/ios_maps_walkthrough/

# Timer

- http://stackoverflow.com/questions/19244607/nstimer-versus-timer-in-xamarin-ios-when-to-use-what


# Info.plist

- ビルド番号

https://forums.xamarin.com/discussion/2278/how-do-you-get-current-version-information-programmatically

~~~
BuildLabel.Text = string.Format (
  @"Build {0}", NSBundle.MainBundle.InfoDictionary ["CFBundleVersion"]);

~~~

- http://www-01.ibm.com/support/knowledgecenter/SSHS8R_6.3.0/com.ibm.worklight.dev.doc/dev/c_splash_images_ios.html?lang=ja

# AppDelegate

- https://forums.xamarin.com/discussion/11712/getting-a-reference-to-the-appdelegate

# Drop Down Menu

- https://github.com/blounty/SlideDownMenu


- [TableAndCellStyles](https://github.com/xamarin/mobile-samples/tree/master/TablesList)
- [monotouch-samples](https://github.com/xamarin/monotouch-samples)
- http://daifuku-p.org/w/?p=767
- http://stackoverflow.com/questions/17821371/uiimage-loaded-from-url-in-xamarin-c-sharp
- http://www.moonmile.net/blog/archives/2969

# TableView
http://ios-practice.readthedocs.org/en/latest/docs/tableview/
- http://iphone-tora.sakura.ne.jp/uitableviewcell.html


Section Header:

- https://forums.xamarin.com/discussion/18037/tablesection-w-out-header
- UITableViewSource.TitleForHeader, TitleForFooter のオーバーライドをやめると消える

スタイル

- UITableViewCellStyleDefault	画像（左）と主テキスト（右）があるセル
- UITableViewCellStyleValue1	主テキスト（左）とサブテキスト（右）があるセル
- UITableViewCellStyleValue2	サブテキスト（左）と主テキスト（右）があるセル
- UITableViewCellStyleSubtitle	画像（左）と主テキスト（右上）とサブテキスト（右下）があるセル

UITableViewStyle

- http://stackoverflow.com/questions/18982347/uitableviewcell-in-ios7-now-has-gaps-on-left-and-right

イメージ

- http://qiita.com/hanoopy/items/d7855b1ff12ef7edeaec


リロード

- http://stackoverflow.com/questions/19105252/update-tableview-data

# imageView

~~~
enum UIViewContentMode : Int {

    case ScaleToFill
    case ScaleAspectFit // contents scaled to fit with fixed aspect. remainder is transparent
    case ScaleAspectFill // contents scaled to fill with fixed aspect. some portion of content may be clipped.
    case Redraw // redraw on bounds change (calls -setNeedsDisplay)
    case Center // contents remain same size. positioned adjusted.
    case Top
    case Bottom
    case Left
    case Right
    case TopLeft
    case TopRight
    case BottomLeft
    case BottomRight
}
~~~

# Navigation

- http://glassonion.hatenablog.com/entry/20120601/1338477967
http://stackoverflow.com/questions/6913212/ios-how-to-recognize-that-we-got-back-from-a-child-uiviewcontroller-within-the

ViewWillAppearで画面表示するときに調整する

~~~csharp
public override void ViewWillAppear (bool animated)
{
  RootViewContoller.Navigation.ShowButtons (true);

  base.ViewWillAppear (animated);
}
~~~

# Xamarin

- [Introduction to the Xamarin Designer for iOS](https://developer.xamarin.com/guides/ios/user_interface/designer/introduction/)
- [Working with Tables and Cells](https://developer.xamarin.com/guides/ios/user_interface/tables/)


# WebView

- [Web View](http://developer.xamarin.com/guides/android/user_interface/web_view/)
- [Load Local Content](https://developer.xamarin.com/recipes/ios/content_controls/web_view/load_local_content/)
- [簡単な例](https://github.com/hdknr/scriptogr.am/blob/master/xamarin/xamarin.ios.webview.simple.cs)

# Draw on MapKIT

- [Xamarin.iOSで地図に図形を表示するには？（MapKit使用）](http://www.buildinsider.net/mobile/xamarintips/0018)

# GEO

- [How do I convert kilometres to degrees in Geodjango/GEOS?](http://stackoverflow.com/questions/5217348/how-do-i-convert-kilometres-to-degrees-in-geodjango-geos)
- [NTS TopologySuite](http://nettopologysuite.github.io/html/index.html)
- [Calculating Distance between two Latitude and Longitude GeoCoordinates](http://stackoverflow.com/questions/6366408/calculating-distance-between-two-latitude-and-longitude-geocoordinates)

- https://github.com/SharpMap/SharpMap
- [Simple calculations for working with lat/lon + km distance?](http://stackoverflow.com/questions/1253499/simple-calculations-for-working-with-lat-lon-km-distance)

## 座標変換



# MapKIT

- [iPhoneアプリで位置情報と地図を使うための基礎知識 (1/3)](http://www.atmarkit.co.jp/ait/articles/1104/04/news117.html)
- [MKMapView上でのタップイベントの取得方法!!](http://web-terminal.blogspot.jp/2013/01/mkmapview.html)
- [Objective-CでMKMapViewの緯度経度を取得とドラッグイベントを制御する方法](http://seikoudoku2000.hatenablog.com/entry/20110503/1304436895)
- [determine if MKMapView was dragged/moved](http://stackoverflow.com/questions/5556977/determine-if-mkmapview-was-dragged-moved)


- マップの移動イベント
- MapLoaded のイベントの後でも呼ばれる

~~~csharp

MainMap.RegionChanged += (object sender, MKMapViewChangeEventArgs e) =>
{
  Console.WriteLine("***** RegionChanged");

};
~~~

- [XAMARIN TUTORIAL – IOS MAPKIT PART 1](http://leiflarsen.org/2015/xamarin-tutorial-ios-mapkit-part-1)

## 現在地

- [Display a Location](http://developer.xamarin.com/recipes/ios/content_controls/map_view/display_a_location/)
- [Get user's current location in Xamarin iOS](http://stackoverflow.com/questions/25657575/get-users-current-location-in-xamarin-ios)
- iOS8 : [RequestWhenInUseAuthorization](http://developer.xamarin.com/api/member/MonoTouch.CoreLocation.CLLocationManager.RequestWhenInUseAuthorization/)
- [iOS 8 Dev Tip: Getting the GPS Location using Core Location](http://matthewfecher.com/app-developement/getting-gps-location-using-core-location-in-ios-8-vs-ios-7/)

# ビューコントローラのライフライム

- Androidだと ActivityをFinishしないと生きている
- iOS だと別のビューコントローラをPushViewControllerすると、現在のビューコントローラが死ぬ

# Autolayout

- [Autolayout時にUIViewのframeを変更する方法](http://qiita.com/ryusukefuda/items/ec04b743683c58958fc3)

- auto layout にする

~~~csharp

button.TranslatesAutoresizingMaskIntoConstraints = false;

~~~

- [今度こそ克服するAutoLayoutの使い方・基礎編～SwiftからはじめるiOSアプリ開発:その5【初心者向けアプリ開発3分tips】](http://engineer.typemag.jp/article/ra-ios-tips06)


# Layout

- http://qiita.com/edo_m18/items/5c224c823ca163629f54

# Button

- [【XamarinによるiOS超入門 】 ボタン ( UIButton )](http://furuya02.hatenablog.com/entry/2015/01/09/041915)
- [Font](https://developer.xamarin.com/recipes/ios/standard_controls/labels/change_the_font/)
- [UIButtonで、画像とタイトルの位置を入れ替える時にハマった話 (UIEdgeInsets)](http://qiita.com/paming/items/a3b61dff825070f8ef40)
- [UIButtonの画像(imageView)の左寄せ、右寄せ(alignment)の設定](http://qiita.com/90_jill/items/791d72740ceecaf30d00)
- [Auto Layout with the Xamarin Designer for iOS](https://developer.xamarin.com/guides/ios/user_interface/designer/designer_auto_layout/)


# DropDown

- [ValorePartners/IOSDropdown](https://github.com/ValorePartners/IOSDropdown)
- [TouchBeganでタッチを検出する](https://developer.xamarin.com/guides/cross-platform/application_fundamentals/touch/part_1_touch_in_ios/)
- [TableViewのカスタマイズ](https://developer.xamarin.com/guides/ios/user_interface/tables/part_3_-_customizing_a_table's_appearance/)
- [透明背景のTableView](http://stackoverflow.com/questions/18753411/uitableview-clear-background)

# iOS

- [Suggested Approach for Modal Login Section](https://forums.xamarin.com/discussion/11879/suggested-approach-for-modal-login-section)
- [Xamarin.iOS/Android で、文字列と画像をPCLを使って共有させる方法](http://www.moonmile.net/blog/archives/5859)
- [Xamarin.iOS/Androidアプリで、バンドルリソース処理を完全共通化できそうな仕様](http://qiita.com/kochizufan/items/69d69f37cf991d452226)
- [Transparent Background Modal View](http://b2cloud.com.au/how-to-guides/invisible-background-modal-view/)


- [cornerRadiusを片側だけ効かせる（UIViewの一部だけ角丸にする）](http://qiita.com/shu223/items/8093f8490019d432af52)

~~~csharp

this.View.Layer.CornerRadius = 10.0f;
this.View.Layer.MasksToBounds = true;

~~~

- [Cocoa Touch: How To Change UIView's Border Color And Thickness?](http://stackoverflow.com/questions/3330378/cocoa-touch-how-to-change-uiviews-border-color-and-thickness)

~~~objective-c
view.layer.borderColor = [UIColor redColor].CGColor;
view.layer.borderWidth = 3.0f;
~~~

- [親のviewのframeからはみ出した要素はタップに反応しない](http://qiita.com/edo_m18/items/b1528f7aea0e06fbe6b4)
