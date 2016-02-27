# Facebook

- http://blog.shibayan.jp/entry/20140114/1389629844

# Auth

- http://sharpmobilecode.com/xamarin-ios-apps-adding-loginsignup-capabilities/


# icon badge

- http://stackoverflow.com/questions/15196761/ios-decrease-icon-badge-number
- http://stackoverflow.com/questions/4722669/how-can-i-add-a-badge-to-a-standard-uibutton
- http://stackoverflow.com/questions/5684636/how-to-add-badges-on-uibarbutton-item
- https://github.com/cargowire/Mono.MKNumberBadgeView



# Draw Text

- https://developer.xamarin.com/recipes/ios/graphics_and_drawing/core_text/draw_unicode_text_with_coretext/
- http://dev.classmethod.jp/smartphone/xamarin-ios-draw-string/

- http://dev.classmethod.jp/smartphone/xamarin-ios-single-view-app/

- http://stackoverflow.com/questions/3602439/mkannotationview-drawrect-not-getting-called
- http://stackoverflow.com/questions/8008277/getting-an-mkannotationview-subclass-with-a-dynamically-drawn-pin
- https://forums.xamarin.com/discussion/14675/simple-drawling-annotation-on-mapview


# plist

- http://eien.seesaa.net/article/298475902.html

~~~bash
$ which plutil
/usr/bin/plutil
$ plutil -convert xml1 Info.plist  -o ~/Download/Info.plist.xml      # To XML
$ plutil -convert binary1 filename.plist    # to Binary
~~~~k

- http://unix.stackexchange.com/questions/14120/extract-only-a-specific-file-from-a-zipped-archive-to-a-given-directory

~~~bash
$ unzip -l MyAppIosVs.1.0.160126.9.ipa  | grep Info
     1534  01-26-16 22:51   Payload/MyAppiOS.app/Info.plist
      865  01-26-16 22:51   Payload/MyAppiOS.app/Main~ipad.storyboardc/Info-8.0+.plist
      865  01-26-16 22:51   Payload/MyAppiOS.app/Main~ipad.storyboardc/Info.plist
      865  01-26-16 22:51   Payload/MyAppiOS.app/Main~iphone.storyboardc/Info-8.0+.plist
      865  01-26-16 22:51   Payload/MyAppiOS.app/Main~iphone.storyboardc/Info.plist
        8  01-26-16 22:53   Payload/MyAppiOS.app/PkgInfo


$ unzip -j MyAppIosVs.1.0.160126.10.ipa Payload/MyAppiOS.app/Info.plist -d .
Archive:  MyAppIosVs.1.0.160126.10.ipa


$ plutil -convert xml1 Info.plist -o Info.plist.xml
~~~


# ATS

- https://developer.xamarin.com/guides/ios/platform_features/introduction_to_ios9/ats/
- http://qiita.com/yanayanalte/items/e6d83c12af77fa238a58
- http://stpsysdev.blogspot.jp/2015/10/ats.html

# MapKIT
- http://blog.fenrir-inc.com/jp/2011/06/mapkit-pin.html
- http://www.dorapro.co.jp/engineerblog/?p=357
- http://anthrgrnwrld.hatenablog.com/entry/2015/10/23/081001
- http://qiita.com/Yuta/items/d3ebc1b8ad032c63c3c8

1. Launce Image Source を指定すること

- http://forums.xamarin.com/discussion/23842/map-problem-on-ios8
- https://forums.xamarin.com/discussion/25476/xamarin-ios-8-2-breaks-xamarin-mobile-geolocation-alert


# Button

- イメージをストレッチさせる

~~~
UIButton button_hunberger = UIButton.FromType(UIButtonType.Custom);
UIImage image_hunberger = UIImage.FromBundle("hunberger.png");
button_hunberger.TranslatesAutoresizingMaskIntoConstraints = false;
button_hunberger.ContentMode = UIViewContentMode.ScaleAspectFit;
//			button_hunberger.HorizontalAlignment = UIControlContentHorizontalAlignment.Fill;
//			button_hunberger.VerticalAlignment = UIControlContentVerticalAlignment.Fill;

button_hunberger.SetImage(image_hunberger, UIControlState.Normal);

header.Add(button_hunberger);
header.AddConstraints (new NSLayoutConstraint[] {
  button_hunberger.CtLeftTo(header, 10),
  button_hunberger.CtMiddleOn(header),
  button_hunberger.CtHeightRate(header,0.6f),
  button_hunberger.CtAspect (1.0f),

});
~~~

# Interface builder

- http://www.atmarkit.co.jp/ait/articles/1007/23/news110.html
- http://stackoverflow.com/questions/12301256/is-it-possible-to-set-uiview-border-properties-from-interface-builder


# labels
- http://buchi.hatenablog.com/entry/2014/09/11/135036

# URL /Custom Scheme

- http://stackoverflow.com/questions/21804984/custom-url-handling-ios-xamarin
- https://chomado.com/programming/c-sharp/xamarin-launch-with-url-scheme/
- http://riccardo-moschetti.org/2014/10/03/opening-a-mobile-app-from-a-link-the-xamarin-way-url-schemas/
- https://github.com/xamarin/Rivets

- AppDelegate
~~
public override bool OpenUrl(UIApplication application, NSUrl url, string sourceApplication, NSObject annotation)
    {
          new UIAlertView("Airdrod File Received!", "File " + url + " received!", null, "OK", null).Show();
        return true;
    }
~~~    


# Annotation

- https://developer.xamarin.com/guides/ios/platform_features/ios_maps_walkthrough/

# Timer

- http://stackoverflow.com/questions/19244607/nstimer-versus-timer-in-xamarin-ios-when-to-use-what


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

# カスタムスキーム

- http://nlogic.jp/?p=417
- http://reliphone.jp/canopenurl/
- http://psychlab.jugem.jp/?eid=712
- https://developer.xamarin.com/api/member/UIKit.UIApplication.CanOpenUrl/p/Foundation.NSUrl/
- https://forums.xamarin.com/discussion/1908/launching-another-app
- https://forums.xamarin.com/discussion/8519/yes-no-confirmation-uialertview
