## AppDelegate

~~~csharp
public static class Extensions
{
public static Dictionary<string, string> ParseQuery(this string query)
{
  return query
    .Split ("?&".ToCharArray ())
    .Where (i => string.IsNullOrEmpty (i) == false)
    .Select (i => i.Split ('='))
    .ToDictionary (
      i => Uri.UnescapeDataString (i [0]),
      i => Uri.UnescapeDataString (i [1]));
}
}
~~~

~~~csharp
[Register ("AppDelegate")]
public class AppDelegate : UIApplicationDelegate
{
  public Dictionary<string,string> Query {get; private set;}
  public override bool OpenUrl (UIApplication app, NSUrl url, NSDictionary options)
  {
    //  ここでなんかする
    Query = url.Query.ParseQuery ();
    return true;
  }

}
~~~  


## 起動すみ

~~~csharp

public partial  class RootViewController : UIViewController
{

  public override void ViewDidLoad ()
		{
			base.ViewDidLoad ();
		  // do anything

			var observer = NSNotificationCenter.DefaultCenter.AddObserver (
				UIApplication.DidBecomeActiveNotification,
				(NSNotification notify) => {
          // do something
			});
		}
}
~~~


## 未起動


~~~csharp
public partial  class RootViewController : UIViewController
{

  public override void ViewDidAppear (bool animated)
  {
    base.ViewDidAppear (animated);

    var query = (UIApplication.SharedApplication.Delegate as AppDelegate).Query;
    if (query != null) {
        // do anything and reset query
    }
  }
}
~~~
