# IntentService


## リソース

- [Creating a Background Service in Android Using IntentService](http://javatechig.com/android/creating-a-background-service-in-android)
- [Xamarin.Android で画面遷移時にデータを渡す](http://qiita.com/amay077/items/8752e7e5db233f5cc73f)
- [Xamarin.Android で Intent を受けとるには？](http://qiita.com/amay077/items/f08fde7bb5dba87c5f91)


## IParcelable : IntentService -> Activity 間のデータ渡し

- Parcel : 小包
- Android では、Activity とか Service をまたぐオブジェクトは Percelable インターフェースを実装しなければならない
- Mono.Android.Export.dll を参照する

~~~csharp
using System;
using Android.OS;
using Java.Interop;

namespace PushNotification.Droid
{
	public class Packet : Java.Lang.Object, IParcelable
	{
    // アプリケーションデータ
		public string Token { get ; set; }
    //.....

		public Packet () { }

    // 必須
		public int DescribeContents()
		{
			return 0;
		}

    // 必須
		public void WriteToParcel(Parcel dest, ParcelableWriteFlags flags)
		{
			dest.WriteString(this.Token);
		}

		// クリエーターファクトリー : public static final Parcelable.Creator の代わり
		[ExportField("CREATOR")]
		public static IParcelableCreator GetCreator()
		{
			return new PacketParcelableCreator();
		}

    // クリエーター
		class  PacketParcelableCreator : Java.Lang.Object, IParcelableCreator
		{
			Java.Lang.Object IParcelableCreator.CreateFromParcel(Parcel source)
			{
				return new Packet{ Token = source.ReadString()};
			}

			Java.Lang.Object[] IParcelableCreator.NewArray(int size)
			{
				return new Java.Lang.Object[size];
			}
		}
	}
}
~~~

## MainActivity : IntentServiceを起動してPacketを受け取る


~~~csharp
using System;

using Android.App;
using Android.Content;
using Android.Content.PM;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using Android.OS;

using Xamarin.Forms;

using Android.Gms.Common;
using Android.Util;

namespace PushNotification.Droid
{
	[Activity (Label = "PushNotification.Droid",
   Icon = "@drawable/icon",
  MainLauncher = true, ConfigurationChanges = ConfigChanges.ScreenSize | ConfigChanges.Orientation)]
	public class MainActivity : global::Xamarin.Forms.Platform.Android.FormsApplicationActivity
	{
		protected override void OnCreate (Bundle bundle)
		{
			base.OnCreate (bundle);

			global::Xamarin.Forms.Forms.Init (this, bundle);

			LoadApplication (new App ());

			// Sample Serviceの起動
			StartService (new Intent (this, typeof(SampleService)));
		}

		[BroadcastReceiver]
		[IntentFilter(new string[]{ SampleService.SERVICE_NAME})]
		public class ResultReceiver : BroadcastReceiver{
			public override void OnReceive(Context context, Intent intent){
				//インテントを受け取った際の処理    
				var obj = intent.GetParcelableExtra("Packet") as Packet;
				Console.WriteLine ("Token = {0}", obj.Token);
			}
		}
	}
}
~~~

## IntentService: 単純なトークンを返す

~~~csharp

using System;
using Android.App;
using Android.Content;
using Android.Util;
//using Android.Gms.Gcm;
//using Android.Gms.Gcm.Iid;			// Instance ID


namespace PushNotification.Droid
{
	[Service(Exported = false)]	// システムが起動するサービスではない
	class SampleService : IntentService
	{
		public const  string  SERVICE_NAME = "SampleIntentService";

		static object locker = new object();

		public SampleService() : base(SERVICE_NAME) { }

    ///サービスメイン
		protected override void OnHandleIntent (Intent intent)
		{
			lock (locker)
			{
					NotifyBroadCast();
			}
		}

    /// 通知する
		public void NotifyBroadCast()
		{
			var intent = new Intent (SampleService.SERVICE_NAME);
			intent.PutExtra ("Packet", new Packet{ Token = "xxxxxxxx" });
			SendBroadcast (intent);
		}
	}
}
~~~
