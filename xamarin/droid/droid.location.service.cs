using Android.Locations;			
using Android.Util;			


public abstract class AbstractDrivingStatus : 
Android.App.Service, Android.Locations.ILocationListener
{
	// サービススレッドハンドラ
	public Android.OS.Handler MainHandler = new Android.OS.Handler();

	/// <summary>
	/// 更新スレッド開始
	/// </summary>
	public void StartUpdatingStatus()
	{
		CurrenTimer = new Timer ((o) => {
			UpdateStatus ();
		}, null, 0, Interval);
	}

	/// <summary>
	/// 定期的に状態を更新する
	/// </summary>
	void UpdateStatus()
	{
		if (!IsLocationManagerStated) {
			// 位置情報サービスが開始されていなかったら開始させる
			MainHandler.Post (() => {
				StartLocationManager ();
			});
		}
		ReportStatus ();
	}

	/// <summary>
	/// ロケーションマネージャを開始する
	/// </summary>
	void StartLocationManager()
	{
		LocationManager = (LocationManager)GetSystemService (LocationService);
		LocationProviderName = LocationManager.GetProviders (
			new Criteria {
				Accuracy = Accuracy.NoRequirement
			},
			true
		).FirstOrDefault ();

		if (!string.IsNullOrEmpty (LocationProviderName)) {
			// 前回の位置情報を強制的に報告する
			this.OnLocationChanged (
				LocationManager.GetLastKnownLocation (LocationProviderName));

			// 端末位置情報更新依頼する
			OnProviderEnabled (LocationProviderName);
		} else {
			ToastMessage (string.Format (
				"No Location Servicer is working. Check battery"));
		}
	}

	/// <summary>
	/// ロケーションマネージャが有効になった(ILocationListener)
	/// 端末位置情報更新依頼する
	/// </summary>
	/// <param name="provider">プロバイダ名</param>
	public void OnProviderEnabled(string provider) {
		LocationManager.RequestLocationUpdates (
			provider,
			MillisecondsToNotify,			// 位置通時時間間隔
			MeterToNotify,					// 位置通知移動間隔
			this);
		ToastMessage ("Start Runnning Location Service");
	}

	/// <summary>
	/// 位置情報が更新された(ILocationListener)
	/// </summary>
	/// <param name="location">Location.</param>
	public void OnLocationChanged(Android.Locations.Location location)
	{
		UpdateStatus (location);
	}

	// UI にメッセージを送る
	void ToastMessage(string msg )
	{
		MainHandler.Post (() => {
			Android.Widget.Toast.MakeText (
				this, msg,
				Android.Widget.ToastLength.Short).Show ();
		});
	}
}
