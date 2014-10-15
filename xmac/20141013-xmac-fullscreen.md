Xamarin.Mac: Full Screenで開始


~~~csharp

	public partial class MainWindow : MonoMac.AppKit.NSWindow
	{
		#region Constructors

		// Called when created from unmanaged code
		public MainWindow (IntPtr handle) : base (handle)
		{
			Initialize ();
		}
		
		// Called when created directly from a XIB file
		[Export ("initWithCoder:")]
		public MainWindow (NSCoder coder) : base (coder)
		{
			Initialize ();
		}
		
		// Shared initialization code
		void Initialize ()
		{
		    // この２行
			this.CollectionBehavior |= NSWindowCollectionBehavior.FullScreenPrimary;
			this.ToggleFullScreen (this);
		}

		#endregion

	}
~~~	
