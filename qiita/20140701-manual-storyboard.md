Xamarin:Storyboard: 指定したビューに強制的に遷移させる

- カスタムURLスキーマでサイトからアクティベーションコードをもらって端末アプリをアクティベートするユースケース


# Activationを行うViewを追加 #
- ビュー (ActivationController)追加
- Storyboard ID を指定する

![image](https://lh6.googleusercontent.com/-G3zejPqS8vs/U7KTl2zz-bI/AAAAAAAAAgs/UNvQjoOSGEo/w1128-h1098-no/manual_storyboard.1.png)

- Activation Codeを表示させるラベル(ActivateLabel)

![image](https://lh6.googleusercontent.com/-qrnjSVtLvLg/U7KTl4_c0WI/AAAAAAAAAgo/tmMeB5lm3Cw/w1286-h1098-no/manual_storyboard.2.png)

- Activateさせるボタン(ActivateButton)

![image](https://lh4.googleusercontent.com/-WF8prPYA5fI/U7KTlyLOa4I/AAAAAAAAAgk/5z3zR8cpGLc/w1338-h1098-no/manual_storyboard.3.png)


# カスタムスキーマを定義 #

- Info.plist
- Advancedタブ
- "qrcode"という “URL Schemes”を定義


# Activationのビューのラベルにcodeをセット# 

- 実際は ActivateButtonのタッチイベントのハンドラも定義するが省略

```csharp

    using System;
    using MonoTouch.Foundation;
    using MonoTouch.UIKit;
    using System.CodeDom.Compiler;
    
    namespace QrCoder
    {
    	partial class ActivationController : UIViewController
    	{
    		string _activation_code = null;
    		
    		public string ActivationCode
    		{
    			set{ this._activation_code = value; }
    		}
    
    		public override void ViewDidAppear (bool animated)
    		{
    			base.ViewDidAppear (animated);
    			this.ActivateCode.Text = _activation_code ?? "" ;
    		}
    	}
    }
```

# AppDelegateでカスタムスキーマで起動するように設定 #

- OpenUrlをオーバーライド

```csharp

		ActivationController _activation_controller = null; 

		public override bool OpenUrl (
			UIApplication application, 
			NSUrl url, string sourceApplication, NSObject annotation)
		{
			// url :  qrcode://host/path?query#fragment 

            // ビューコントローラをStoryboardからロードしてクラス作成する
			if (_activation_controller == null) {
				_activation_controller = this.Window.RootViewController.Storyboard.InstantiateViewController (
					"ActivationController"
				) as ActivationController;
			}

            // URL Query
			var query = System.Web.HttpUtility.ParseQueryString (url.Query); // System.Web.WebServices

			if (string.IsNullOrEmpty (query ["code"]))
                // codeパラメータがなければActivateしない
				return false;

            // ビューにコードをセット
			_activation_controller.ActivationCode = query ["code"].ToString ();

            // ナビゲーションコントローラを取得し、ActivationControllerビューをそこにプッシュする
			var controller = (UINavigationController)this.Window.RootViewController;
			controller.PushViewController (_activation_controller, true);

            // OpenUrlが処理されてUIが変わります
			return true;
		}
```


# Safariからテスト #

- qrcode://me/activate?code=activation_code でActivationビューが起動して、それにコードが設定せれている
- "Activate Now"をクリックして、端末のアプリをアクティベートする



