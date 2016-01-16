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

# Autolayout

- [Autolayout時にUIViewのframeを変更する方法](http://qiita.com/ryusukefuda/items/ec04b743683c58958fc3)

- auto layout にする

~~~csharp

button.TranslatesAutoresizingMaskIntoConstraints = false;

~~~

- [今度こそ克服するAutoLayoutの使い方・基礎編～SwiftからはじめるiOSアプリ開発:その5【初心者向けアプリ開発3分tips】](http://engineer.typemag.jp/article/ra-ios-tips06)

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
