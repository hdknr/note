Xamarin.Mac: AVPlayerのビデオ表示位置のトップマージンを０にする


# Interface Builder でAVPlayerViewのAutoresizingを設定する

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/xmac/AVPlayer/1.autoresizing.png)



# AVPlayerViewの実装クラス作成


~~~csharp:AVPlayerView.cs

[MonoMac.Foundation.Register("AVPlayerView")]
public class AVPlayerView : MonoMac.AppKit.NSView
{
    //...
}
~~~

# AVPlayerViewのリサイズハンドラを実装

- Macの座標は Bottom-Leftがオリジンみたい
- AVPlayerLayerのなかのVideoは自動的にセンタリングされるようです
- Videoの高さとAVPlayerLayerの高さの差だけSetBoundsOrigin()で持ち上げてやると良さそうです

~~~ csharp:AVPlayerView.cs

		public override void ResizeSubviewsWithOldSize (System.Drawing.SizeF oldSize)
		{
			// AVPlayerLayerのBounds == this.Bounds

			base.ResizeSubviewsWithOldSize (oldSize);

			var margin = this.Bounds.Height - _playerlayer.VideoRect.Height;
		
			this.SetBoundsOrigin(
				new System.Drawing.PointF(0.0f, margin));
				
		}
~~~		

![image](https://raw.githubusercontent.com/hdknr/scriptogr.am/master/xmac/AVPlayer/2.top_margin_0.png)





	
