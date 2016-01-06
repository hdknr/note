Xamrin.Forms: MessagingCenter

- [Publish and Subscribe with MessagingCenter](https://developer.xamarin.com/guides/xamarin-forms/messaging-center/)
- [MVVM - Messenger and View Services in MVVM](https://msdn.microsoft.com/ja-jp/magazine/jj694937.aspx)
- [MVVM(Model View ViewModel)デザインパターンとData Bindingの参考URLメモ(2015-03時点)](http://hblog.glamenv-septzen.info/entry/2015/03/29/232520)
- [MVVM Light Toolkit](http://www.mvvmlight.net/)
- [MVVM Light Messenger](http://wpfapptutorial.com/mvvm-light-messenger) 

## Forms側にボタンを作ってタップしたらOS情報をラベルに記載

- ボタンがクリックされた時に `button_click` イベントを送信する
- サブスクライバに SetLabel を読んでもらう

~~~csharp
using System;

using Xamarin.Forms;

namespace PushNotification
{
  ///
  /// MainPage = new MainContent();
	public class MainContent : ContentPage
	{
		Label  _label = new Label();
		Button _button = new Button{ Text = "Tap Here"};

		public MainContent ()
		{
			Content = new StackLayout {
				Children = {
					_label, _button
				},        
				VerticalOptions = LayoutOptions.Center,
				HorizontalOptions = LayoutOptions.Center					
			};

			this._button.Clicked +=  (object sender, EventArgs e) =>
			{
				MessagingCenter.Send(this, "button_click");
			};
		}

		public void SetLabel(string msg){
			_label.Text = msg;
		}
	}
}
~~~

## サブスクライバ

- `button_click` をサブスクライブする
- MainContent.SetLabel(msg) でOS情報を渡す

### Android

~~~csharp
using Android.App;
using Android.Content;
using Android.Content.PM;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using Android.OS;

using Xamarin.Forms;

namespace PushNotification.Droid
{
	[Activity (Label = "PushNotification.Droid",
   Icon = "@drawable/icon", MainLauncher = true,
   ConfigurationChanges = ConfigChanges.ScreenSize | ConfigChanges.Orientation)]
	public class MainActivity : global::Xamarin.Forms.Platform.Android.FormsApplicationActivity
	{
		protected override void OnCreate (Bundle bundle)
		{
			base.OnCreate (bundle);

			global::Xamarin.Forms.Forms.Init (this, bundle);

			LoadApplication (new App ());

			MessagingCenter.Subscribe<MainContent> (this, "button_click", (content) => {
				content.SetLabel(string.Format("{0} {1}",
					Android.OS.Build.VERSION.Release,
					DateTime.Now.ToLongTimeString() ));
			});
		}
	}
}
~~~

### iOS

~~~csharp
using System;
using System.Collections.Generic;
using System.Linq;

using Foundation;
using UIKit;

using Xamarin.Forms;

namespace PushNotification.iOS
{
	[Register ("AppDelegate")]
	public partial class AppDelegate : global::Xamarin.Forms.Platform.iOS.FormsApplicationDelegate
	{
		public override bool FinishedLaunching (UIApplication app, NSDictionary options)
		{
			global::Xamarin.Forms.Forms.Init ();

			LoadApplication (new App ());

			MessagingCenter.Subscribe<MainContent> (this, "button_click", (content) => {
				content.SetLabel(string.Format("{0} {1}",
					new NSProcessInfo().OperatingSystemVersionString,
					DateTime.Now.ToLongTimeString() ));
			});

			return base.FinishedLaunching (app, options);
		}
	}
}
~~~
