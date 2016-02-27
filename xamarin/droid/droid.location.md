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

- http://qiita.com/yasumodev/items/5f0f030f0ebfcecdff11

~~~csharp
public LocationManager  LocationManager { get; private set; }
public string LocationProviderName {get; private set; }

long UpdateMilliseconds { get; set; } = 3000;
float UpdateMeter { get ; set; } = 5.0f;

public void StartUpdate()
{
  if (LocationManager == null) {
    LocationManager = (LocationManager)GetSystemService (LocationService);

    LocationProviderName = LocationManager.GetProviders (
      new Criteria{ Accuracy = Accuracy.Fine },
      true
    ).FirstOrDefault ();				
  }

  if (!string.IsNullOrEmpty (LocationProviderName)) {
    OnProviderEnabled (LocationProviderName);
    this.OnLocationChanged (
      LocationManager.GetLastKnownLocation (LocationProviderName));

    StartWorker ();

  } else {
    ToastMessage (string.Format(
      "No Location Servicer is working. Check battery"));
  }				
}

public void OnProviderEnabled(string provider) {

  LocationManager.RequestLocationUpdates (
    provider,
    UpdateMilliseconds,
    UpdateMeter,
    this);
  ToastMessage ("Start Runnning Location Service");
}
void ToastMessage(string msg )
{
  (new Android.OS.Handler ()).Post (() => {
    Android.Widget.Toast.MakeText (
      this, msg,
      Android.Widget.ToastLength.Short).Show ();
  });
}
~~~
