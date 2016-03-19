
- [Google APIs Analytics iOS Library](https://www.nuget.org/packages/Xamarin.Google.iOS.Analytics/3.14.0.1)
- [xamarin iOS/AndroidでGoogle Analyticsを使うには](http://qiita.com/hIDDEN_xv/items/f524c719b0be79eda4b7)

# Sample

~~~csharp

using System;
using UIKit;
using Google.Analytics;

namespace App.iOS
{
	public static class GoogleExtensions
	{
		public static void SendScreenName(
			this UIViewController controller, string screen_name)
		{
			Gai.SharedInstance.DefaultTracker.Set (
				GaiConstants.ScreenName, screen_name);

			Gai.SharedInstance.DefaultTracker.Send (
				DictionaryBuilder.CreateScreenView ().Build ());
		}

		public static ITracker CreateTracker(string id){
			Gai.SharedInstance.DispatchInterval = 20;
			Gai.SharedInstance.TrackUncaughtExceptions = true;
			return Gai.SharedInstance.GetTracker (id );
		}
	}
}
~~~

- [Google Analytics Reports](https://forums.xamarin.com/discussion/16459/google-analytics-reports)

~~~csharp
public const string AllowTrackingKey = "AllowTracking";
public override bool WillFinishLaunching (UIApplication application, NSDictionary launchOptions)
{
var optionsDict = NSDictionary.FromObjectAndKey (new NSString ("YES"), new NSString (AllowTrackingKey));
NSUserDefaults.StandardUserDefaults.RegisterDefaults (optionsDict);

// User must be able to opt out of tracking
       GAI.SharedInstance.OptOut = !NSUserDefaults.StandardUserDefaults.BoolForKey (AllowTrackingKey);
GAI.SharedInstance.DispatchInterval = 5;
GAI.SharedInstance.TrackUncaughtExceptions = true;
                Tracker = GAI.SharedInstance.GetTracker("HighLowGlitter", TrackingId);
return true;
}
~~~
