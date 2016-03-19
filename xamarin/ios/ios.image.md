## UIImage

- [RestSharp.Portable](https://github.com/Sellegit/RestSharp.Portable)

~~~csharp

public async void Get(string url)
{		
  var req = new RestRequest (url);
  using (var client = new RestClient (url)) {
    try {
      var res = await client.Execute (req);
      Image = UIImage.LoadFromData(NSData.FromArray(res.RawBytes));

      this.SetNeedsDisplayInRect(Frame);		    // 再描画
    } catch (Exception ex) {
      Console.WriteLine ("WebImage exception {0} {1}", ex.Message, url);
    }
  }
}
~~~


## Regina

- [実行中の実機がどのRetinaのタイプか判断する方法 [swift2.1]](http://anthrgrnwrld.hatenablog.com/entry/2015/11/15/094426)
