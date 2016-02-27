UIWebView: ダイアログ(っぽいView)のアンカーをクリックしたら閉じる


## WebContentView

~~~csharp
using Foundation;
using System;
using System.CodeDom.Compiler;
using UIKit;
using ObjCRuntime;


namespace PhonePop
{
	partial class WebContentView : UIView
	{
		const string NibName = "WebContentView";

		public UIWebView Html {get { return ContentHtml; }}

		public WebContentView (IntPtr handle) : base (handle)
		{
		}

		public static WebContentView Factory()
		{
			var arr = NSBundle.MainBundle.LoadNib (NibName, null, null);
			return Runtime.GetNSObject<WebContentView> (arr.ValueAt(0));
		}
	}
}
~~~

## WebContentViewController

~~~csharp
using System;

using UIKit;

using Foundation;
using ObjCRuntime;

namespace PhonePop
{
	public partial class WebContentViewController : UIViewController
	{
		WebContentView HtmlView { get;set; }

		public WebContentViewController () : base ("WebContentViewController", null)
		{
		}

		public override void ViewDidLoad ()
		{
			base.ViewDidLoad ();
			// Perform any additional setup after loading the view, typically from a nib.

			HtmlView = WebContentView.Factory();
			HtmlView.Frame = View.Frame;
			View.AddSubview (HtmlView);

			SetupHtml ();

		}

		void SetupHtml()
		{
			var dialog_delegete  = new MyWebView ();
			dialog_delegete.OnNavigating += (
				object sender,
				NSUrlRequest request,
				UIWebViewNavigationType naviType) => {
				if (request.Url.AbsoluteString.IndexOf ("close") >= 0) {
					this.DismissViewController (true, () => {});
				}
			};

			HtmlView.Html.Delegate = dialog_delegete;

			string contentDirectoryPath =
				System.IO.Path.Combine (NSBundle.MainBundle.BundlePath, "");

			string htmml = @"<html><body><a href=""#close"">Close</a></body></html>";

			HtmlView.Html.LoadHtmlString(htmml,
				new NSUrl(contentDirectoryPath, true));
		}

		public  class MyWebView : UIWebViewDelegate
		{
			public delegate void OnNavigatingEvent(
				object sender, NSUrlRequest request,UIWebViewNavigationType naviType );
			public event OnNavigatingEvent OnNavigating;
			public bool ForceLoading {get;set; } = true;

			public override bool ShouldStartLoad (
					UIWebView webView, NSUrlRequest request,
					UIWebViewNavigationType navigationType)
			{
				if (OnNavigating != null) {
					OnNavigating (webView, request, navigationType);
				}

				return ForceLoading;
			}
		}
	}
}
~~~
