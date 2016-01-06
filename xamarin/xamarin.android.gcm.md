- [Collect Android Logs and Version info in Xamarin.Android
Raw](https://gist.github.com/Redth/5862119)
- [【Xamarin.Android】ユーザの環境を得る【OS,端末名,アプリのバージョン】](http://chomado.com/programming/c-sharp/xamarin-android-get-user-environment-info/)
Android.OS.Build.VERSION.Release



# Google Cloud Message (GCM)

- [Mobile Services Android アプリへのプッシュ通知の追加](https://azure.microsoft.com/ja-jp/documentation/articles/mobile-services-javascript-backend-android-get-started-push/)
- [Walkthrough - Using Remote Notifications in Xamarin.Android](https://developer.xamarin.com/guides/cross-platform/application_fundamentals/notifications/android/remote_notifications_in_android/)
- Google:[Send Messages to Topics](https://developers.google.com/cloud-messaging/topic-messaging)
- `Google Play Store` アプリは必須
- [[Android]通知を表示する。その２。](http://mousouprogrammer.blogspot.jp/2013/05/android_13.html)    
- [PendingIntent](http://androidpg.blogspot.jp/2012/02/progressbar_09.html)
- [Android4.1で追加された Notification のスタイル](http://dev.classmethod.jp/smartphone/android/android-tips-23-android4-1-notification-style/)

## Google Developer Console

- [console.developers.google.com](https://console.developers.google.com)

##  Xamarin

- [RemoteNotificationsサンプル](https://github.com/xamarin/monodroid-samples/tree/master/RemoteNotifications)
- [Push Notification Plugin for Xamarin](https://github.com/rdelrosario/xamarin-plugins/tree/master/PushNotification)

流れ:

1. Nuget: Xamarin.GooglePlayServices.Gcm
2. パーミッション: Properties/AndroidManifest.xml
3. 実装:  Google Play Serviceが使えるかを確認
4. 実装:  `登録トークン` 取得(GCMへの登録インテントサービス)
5. 実装:  IDリスナーサービス: `登録トークン` 受け取る(リフレッシュ対応)
6. 実装:  GCMリスナーサービス: サーバーからのメッセージを GCM 経由で受け取る


topic messaging:

- アプリサーバーがトピックにメッセージを送る

### 1) Nuget

- `Xamarin Google Play Services - GCM` をインストール

MainActivity.cs:

~~~csharp
using Android.Gms.Common;
using Android.Util;
~~~

### 2) パーミッション(AndroidManifest.xml)

Package Name:

- バンドル識別子みたいなやつ

~~~xml
<?xml version="1.0" encoding="utf-8"?>
<manifest ....
      package="jp.lafoglig.push.pushnotification">
      ...
~~~      

パーミッッション:

~~~xml

<?xml version="1.0" encoding="utf-8"?>
<manifest ...
      package="jp.lafoglig.push.pushnotification">
  <uses-permission android:name="com.google.android.c2dm.permission.RECEIVE" />
  <uses-permission android:name="android.permission.WAKE_LOCK" />
  <uses-permission android:name="android.permission.INTERNET" />
  <uses-permission android:name="jp.lafoglig.push.pushnotification.permission.C2D_MESSAGE" />
  <permission android:name="jp.lafoglig.push.pushnotification.permission.C2D_MESSAGE"
    android:protectionLevel="signature" />
  ...
</manifest>
~~~

### 3) Google Play が使えるか？ MainActivity.IsPlayServicesAvailable()

~~~csharp
[Activity (
    MainLauncher = true,
    ConfigurationChanges = ConfigChanges.ScreenSize | ConfigChanges.Orientation)]
public class MainActivity : global::Xamarin.Forms.Platform.Android.FormsApplicationActivity
{
    protected override void OnCreate (Bundle bundle)
    {
        //......
        IsPlayServicesAvailable ();
    }
    public bool IsPlayServicesAvailable ()
    {
        int resultCode = GooglePlayServicesUtil.IsGooglePlayServicesAvailable (this);
        if (resultCode != ConnectionResult.Success)
        {
            if (GooglePlayServicesUtil.IsUserRecoverableError (resultCode))
                //.....
            else
            {
                // .....
                Finish ();
            }
            return false;
        }
        else
        {
            // .....
            return true;
        }
    }
}
~~~

### 4) `登録トークン` 取得

- [What is Instance ID?](https://developers.google.com/instance-id/)
- Google のInstance ID サービスをつかってセキュリティトークンを作る
- このセキュリティトークンはクライアントアプリがアプリケーションサーバーにアクセスする許可を与える
- GCM からは `登録トークン` を受け取る
- 登録トークンをアプリケーションサーバーに送る
- トピックチャネルをサブスクライブする

~~~csharp
using System;
using Android.App;
using Android.Content;
using Android.Util;
using Android.Gms.Gcm;
using Android.Gms.Gcm.Iid;

namespace PushNotification.Droid
{
	[Service(Exported = false)]	// システムが起動するサービスではない
	class RegistrationIntentService : IntentService
	{
		string  PACKAGE_NAME = "jp.lafoglig.push.pushnotification";

		static object locker = new object();

		public RegistrationIntentService() :
      base("RegistrationIntentService") { } // ワーカースレッド名

		protected override void OnHandleIntent (Intent intent)
		{
			try
			{
				Log.Info ("RegistrationIntentService",
                  "Calling InstanceID.GetToken");

				lock (locker)   // インテントが別スレッドで同時に走る、かもしないので
				{
          // インスタンスID を取得
					var instanceID = InstanceID.GetInstance (this);

          // トークンを取得(GCMより登録トークン)
					var token = instanceID.GetToken (
						PACKAGE_NAME,
            GoogleCloudMessaging.InstanceIdScope, null);

					Log.Info ("RegistrationIntentService",
                    "GCM Registration Token: " + token);

          // トークンをサーバーに送信
					SendRegistrationToAppServer (token);   

          // トークンでトピックをサブスクライブ
					Subscribe (token);
				}
			}
			catch (Exception e)
			{
				Log.Debug("RegistrationIntentService",
                  "Failed to get a registration token");
				return;
			}
		}

		void SendRegistrationToAppServer (string token)
		{
        // アプリケーションサーバーにトークンを送る
        // サーバーではこのトークンを送信したユーザーIDに紐づけること
		}

		void Subscribe (string token)
		{
      var topic =  "/topics/global";
      // トピックをサブスクライブする
			var pubSub = GcmPubSub.GetInstance(this);
			pubSub.Subscribe(token, topic, null);
		}
	}
}
~~~

- このインテントサービスを MainActivityから呼ぶ

~~~csharp
protected override void OnCreate (Bundle bundle)
{
    base.OnCreate (bundle);
    //....

    if (IsPlayServicesAvailable ())
    {
        var intent = new Intent (
          this, typeof (RegistrationIntentService));
        StartService (intent);
    }
}
~~~

### 5) リフレッシュトークンの処理


~~~csharp

using Android.App;
using Android.Content;
using Android.Gms.Gcm.Iid;

namespace PushNotification.Droid
{
	[Service(Exported = false),        // システム起動ではない
		IntentFilter(new[] {            // 登録トークンのリフレッシュを処理する
			"com.google.android.gms.iid.InstanceID"
		})
	]
	class RefreshListenerService : InstanceIDListenerService
	{
		public override void OnTokenRefresh()
		{
      // #4 の登録トークン受け取りサービスを起動
			var intent = new Intent (
				this, typeof (RegistrationIntentService));
			StartService (intent);
		}
	}
}
~~~

### 6) メッセージの取得

~~~csharp
using Android.App;
using Android.Content;
using Android.OS;
using Android.Gms.Gcm;
using Android.Util;

namespace PushNotification.Droid
{
	[Service (Exported = false),            // システム起動ではない
	 IntentFilter (
		new [] {"com.google.android.c2dm.intent.RECEIVE" }) // GCM メッセージを受け取る
	]
	public class MessageListenerService : GcmListenerService
	{
        ///
		/// <summary>
        /// 受信コールバック
		/// </summary>
		/// <param name="from">From.</param>
		/// <param name="data">バンドルデータオブジェクト</param>
		public override void OnMessageReceived (string from, Bundle data)
		{
			var message = data.GetString ("message");

			Log.Debug ("MessageListenerService", "From:    " + from);
			Log.Debug ("MessageListenerService", "Message: " + message);

            // メッセージを通知領域に通知
			SendNotification (message);
		}

		void SendNotification (string message)
		{
            // インテント
			var intent = new Intent (
                this,
                typeof(MainActivity));   // このアプリケーション
			intent.AddFlags (ActivityFlags.ClearTop);

            // ペンデイングインテントでラップ
			var pendingIntent = PendingIntent.GetActivity (
					this,                           // コンテクスト  
                    0,                              // リクエストコード (0でよい)
                    intent,                         // 送信するインテント
                    PendingIntentFlags.OneShot);    // １回送信して終わり

            // 通知を作る
			var notificationBuilder = new Notification.Builder(this)
				.SetSmallIcon (Resource.Drawable.icon)  // 通知ドロワーに表示するアイコンを設定
				.SetContentTitle ("GCM Message")        // Notificationを開いたときに表示されるタイトル
				.SetContentText (message)               // Notificationを開いたときに表示されるサブタイトル
				.SetAutoCancel (true)                   // タップするとキャンセル(消える)
				.SetContentIntent (pendingIntent);      // ペンディングインテント

            // 通知サービスマネージャ
			var notificationManager = (NotificationManager)GetSystemService(
				Context.NotificationService);

            // マネージャ経由して通知する
			notificationManager.Notify (
				0, notificationBuilder.Build());
		}
	}
}
~~~
