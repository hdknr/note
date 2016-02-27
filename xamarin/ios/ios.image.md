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
