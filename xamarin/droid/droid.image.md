# SetImageUri はつかえません

- [Xamarin](https://developer.xamarin.com/api/member/Android.Widget.ImageView.SetImageURI/p/Android.Net.Uri/)

This does Bitmap reading and decoding on the UI thread, which can cause a latency hiccup.
If that's a concern,
consider using ImageView.SetImageDrawable(Drawable) or
ImageView.SetImageBitmap(Bitmap) and BitmapFactory instead.

- [Android ImageViewにウェブ上の画像表示](http://blog.iscw.jp/?p=658)


# Bitmap をダウンロード

- [System.Net.WebClient](https://developer.xamarin.com/api/type/System.Net.WebClient/)
- [Android.Graphics.BitmapFactory](https://developer.xamarin.com/api/type/Android.Graphics.BitmapFactory/)

~~~csharp
public static Bitmap GetImageBitmapFromUrl(string url)
{
    using (var webClient = new WebClient())
    {
      var imageBytes = webClient.DownloadData(url);
      if (imageBytes != null && imageBytes.Length > 0)
      {
        return BitmapFactory.DecodeByteArray(imageBytes, 0, imageBytes.Length);
      }
    }
    return null;
}

~~~
