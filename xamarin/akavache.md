- [GitHub's Xamarin Starter Apps について](http://blog.amay077.net/blog/2013/12/22/about-githubs-xamarin-starter-apps/)
- [クロスプラットフォーム対応KVS Akavache を使ってお手軽にデータを保存する](http://qiita.com/amay077/items/356ad0028b7e6fbf089f)
- [Showing Images in list view adapter using Akavache](http://stackoverflow.com/questions/27425301/showing-images-in-list-view-adapter-using-akavache)
- [Akavache is AKA Awesome! ](https://codemilltech.com/akavache-is-aka-awesome/)


# Image キャッシュ

~~~csharp

using Akavache;
using Splat;

public static class Extensions {

  public static void FromUrl(this UIImageView view, string url)
  {
    Akavache.BlobCache.LocalMachine.LoadImageFromUrl (url, false)
      .Subscribe(new Action<Splat.IBitmap>(pic => { 
        (new NSObject()).InvokeOnMainThread(()=>{
          view.Image =  pic.ToNative();
          view.SetNeedsDisplay();	// 再描画
        });
      }), ex => Console.WriteLine(ex));
  }

}
~~~
