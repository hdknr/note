# Landscape

- http://pentan.info/android/screen_orientation.html
- http://developer.android.com/intl/ja/guide/topics/manifest/activity-element.html#screen
- http://stackoverflow.com/questions/2150287/force-an-android-activity-to-always-use-landscape-mode

~~~csharp
OnCreate(){
  RequestedOrientation = Android.Content.PM.ScreenOrientation.Landscape;
}
~~~~

# Sevice

- http://stackoverflow.com/questions/25987377/keeping-an-android-app-running-in-the-background-preventing-it-from-stopping-dy
- https://developer.android.com/intl/ja/training/run-background-service/create-service.html

- https://developer.xamarin.com/guides/android/application_fundamentals/services/
- https://developer.xamarin.com/guides/android/application_fundamentals/services/part_1_-_started_services/
- https://github.com/xamarin/monodroid-samples/tree/master/ServiceSamples

- https://developer.xamarin.com/recipes/android/fundamentals/service/create_a_simple_service/
- http://techbooster.jpn.org/andriod/application/1570/

パラメータを渡す:

- http://www.coderanch.com/t/603994/Android/Mobile/Passing-variable-Activity-running-Service
- http://stackoverflow.com/questions/4300291/example-communication-between-activity-and-service-using-messaging
- https://developer.xamarin.com/guides/android/application_fundamentals/services/part_1_-_started_services/


Activity:

~~~
Intent intent = new Intent("com.hayes.android.MyService");
intent.putExtra("MyService.data", "myValue");
startService(intent);
~~~

Service:

~~~
@Override
public int onStartCommand (Intent intent, int flags, int startId) {
    if (intent.getAction().equals("com.hayes.android.MyService")) {
        String value = intent.getStringExtra("MyService.data");
        // do something with the value here
    } else {
        Log.d(MY_TAG, "Received intent with action="+intent.getAction()+"; now what?");
    }
    return START_NOT_STICKY;
}
~~~

止まらないようにする:


- https://forums.xamarin.com/discussion/9797/remote-notifications
- http://furuya02.hatenablog.com/entry/20140503/1399767382

# AlarmManager

- http://techbooster.jpn.org/andriod/application/2166/


# Power

- http://developer.android.com/intl/ja/reference/android/os/PowerManager.html

- http://qiita.com/amay077/items/1ebc77d2f57414532976

~~~
$ adb -s F6NPFP056580 shell dumpsys power   | grep WAKE
  PARTIAL_WAKE_LOCK              'TaxiDriverStatus' (uid=10196, pid=15958, ws=null, time=1s)
~~~

~~~csharp
[Android.App.Service]
[Android.App.IntentFilter(new String[]{ Settings.RunningServiceIdentifer})]
public class TaxiDrivingStatus :Android.App.Service, ILocationListener
{
  .....

const stirng ServiceName = "TexiService";
Android.OS.PowerManager.WakeLock PowerLock { get; set;}

public void KeepWakup(bool wakeon){
  if (wakeon) {
    PowerLock = (GetSystemService (PowerService) as Android.OS.PowerManager)
      .NewWakeLock (Android.OS.WakeLockFlags.Partial,ServiceName);				
    PowerLock.Acquire ();
  } else {
    PowerLock.Release ();
  }
}

public override Android.OS.IBinder OnBind (Android.Content.Intent intent)
{
  KeepWakup (true);
  return TaxiMessenger.Binder;
}
public override bool OnUnbind (Android.Content.Intent intent)
{
  KeepWakup (false);
  return base.OnUnbind (intent);
}
~~~

# Location

- http://www.adakoda.com/android/000125.html
- http://www.howtogeek.com/142654/find-out-which-apps-are-keeping-your-android-awake-with-wakelock-detector/


##  Spinner

- http://www.synapse.ne.jp/anko/spinner2.html


# Layout

- https://forums.xamarin.com/discussion/1051/relative-layout
- http://stackoverflow.com/questions/6647177/set-equal-width-of-columns-in-table-layout-in-android
- http://stackoverflow.com/questions/4821945/have-textview-scale-its-font-size-to-fill-parent
- http://stackoverflow.com/questions/5033012/auto-scale-textview-text-to-fit-within-bounds/5280436#5280436
- http://blog.global-eng.co.jp/android/2011/01/11/view%E3%82%B5%E3%82%A4%E3%82%BA%E3%81%AE%E8%A8%AD%E5%AE%9A%E3%83%BB%E5%8F%96%E5%BE%97/
- http://shitappaprogramer.seesaa.net/article/143152877.html
- http://qiita.com/Yuki_Yamada/items/eb4a25cedca2ff8078fd


# エラー処理

- http://qiita.com/ta-yamaoka/items/e374921d642e9ac84b3b
