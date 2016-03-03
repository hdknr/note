- [GitHub's Xamarin Starter Apps について](http://blog.amay077.net/blog/2013/12/22/about-githubs-xamarin-starter-apps/)
- [クロスプラットフォーム対応KVS Akavache を使ってお手軽にデータを保存する](http://qiita.com/amay077/items/356ad0028b7e6fbf089f)
- [Showing Images in list view adapter using Akavache](http://stackoverflow.com/questions/27425301/showing-images-in-list-view-adapter-using-akavache)
- [Akavache is AKA Awesome! ](https://codemilltech.com/akavache-is-aka-awesome/)

# API

## 取得

- Get( アイテム取得)
- GetObject, GetObjects(オブジェクト取得)
- GetAllObjects (型のオブジェクトを全て取得)

## 保存

- Insert
- InsertObject , InsertObjects

## 削除

- Invalidate
- InvalidateObject, InvalidateObjects
- InvalidateAllObjects
- InvalidateAll

## メタ情報

- GetAllKeys(キーの取得)
- GetCreatedAt(作成時間取得)
- GetObjectCreatedAt(オブジェクトの作成時間)

## その他

- Flush (ディスクに書き込む)
- Vacuum(SQLite VACUUM)

## ログイン

- SaveLogin (ログイン情報保存)
- GetLoginAsync(ログイン情報取得)
- EraseLogin(ログイン情報削除)


## ファイル

- DownloadUrl
- LoadImage(キャッシュから), LoadImageFromUrl(ネットから)

## 複合

-  GetOrFetchObject(キャッシュに存在しなかったら取得してい保存)
-  GetOrCreateObject(asyncじゃないバージョンのGetOrFetchObject)
-  GetAndFetchLatest(キャッシュからかえしたあとで、すぐに更新)

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

# JSON
