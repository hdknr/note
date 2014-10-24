CoreAnimation: TODO: 止め方を調べる

- Windowをゆらす事はできるが止め方がよくわからない

WindowDidLoad() でゆらす:

~~~csharp

	public partial class MainWindowController : MonoMac.AppKit.NSWindowController
	{
	    //....

		public override void WindowDidLoad ()
		{
			base.WindowDidLoad ();

            Shake();
		}
~~~

アニメーションを作ってセットして、 Windowを移動すると揺れる。

~~~csharp
				
        void Shake()
		{
			var key = new NSString (@"frameOrigin");
			var animation = CreateShakeAnimation (this.Window.Frame);
			var animations =  NSDictionary.FromObjectAndKey (animation, key);

			Window.Animations = animations;

			((NSWindow)this.Window.Animator).SetFrameOrigin(
				Window.Frame.Location);	
										
		}
~~~

ゆらすアニメーションの作成

~~~ csharp

		CAKeyFrameAnimation CreateShakeAnimation(
			RectangleF frame, 
			int shakes = 100,
			float swing = 0.02f,
			float duration = 10.0f
		)
		{
			var shakePath = new CGPath();

			shakePath.MoveToPoint(frame.GetMinX(), frame.GetMinY());

			for (int index = 0; index < shakes; index++)
			{
				shakePath.CGPathAddLineToPoint(
					frame.GetMinX() - frame.Size.Width * swing, frame.GetMinY());

				shakePath.CGPathAddLineToPoint(
					frame.GetMinX() + frame.Size.Width * swing, frame.GetMinY());
			}

			shakePath.CloseSubpath();

			return new CAKeyFrameAnimation () {
				Path = shakePath,
				Duration = duration
			};
		}

~~~
		
