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
