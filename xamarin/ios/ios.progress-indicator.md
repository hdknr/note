- https://developer.xamarin.com/recipes/ios/standard_controls/popovers/display_a_loading_message/

## 単純なスピナー

- アプリケーション起動時

~~~csharp

partial class RootViewContoller : UIViewController
{
  public RootViewContoller (IntPtr handle) : base (handle)
  {
  }

  UIActivityIndicatorView activitySpinner;

  void StartSpinner()
  {
    var centerX = View.Frame.Width / 2;
    var centerY = View.Frame.Height / 2;
    if (activitySpinner == null) {
      activitySpinner = new UIActivityIndicatorView (UIActivityIndicatorViewStyle.WhiteLarge);
      activitySpinner.Frame = new CoreGraphics.CGRect (
        centerX - activitySpinner.Frame.Width/2,
        centerY - activitySpinner.Frame.Height/2,
        activitySpinner.Frame.Width,
        activitySpinner.Frame.Height);
      activitySpinner.AutoresizingMask = UIViewAutoresizing.All;
      View.AddSubview (activitySpinner);
    }
    if (activitySpinner != null) {
      View.BackgroundColor = UIColor.Gray;
      activitySpinner.StartAnimating ();
    }
  }

  void StopSpinner()
  {
    if(activitySpinner != null ){
      View.BackgroundColor = UIColor.White;
      activitySpinner.StopAnimating ();
      activitySpinner.Dispose();
      activitySpinner= null;
    }
  }

  public override void ViewWillAppear (bool animated)
  {
    StartSpinner ();
    base.ViewWillAppear (animated);
  }
  public override void ViewDidAppear (bool animated)
  {
    StopSpinner ();
    base.ViewDidAppear (animated);
  }
}  
