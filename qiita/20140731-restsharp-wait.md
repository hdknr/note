RestSharp.Portable: Task&lt;IRestResponse&gt;をWait()できないのでTaskでラップする


URIをRestSharpでGETする:

```csharp

		public Task<IRestResponse> AsyncRestSharp(string uri)
		{
			var client = new RestClient (uri);
			var req = new RestRequest ("/", HttpMethod.Get);
			var res =  client.Execute (req);

			return res;
		}

```

		
TaskをWait()するとメインスレッドが止まってしまうダメな例(iOS)：

```csharp
		
		[Test]
		public void TestRestSharpWithTask()
		{
          　var call = AsyncRestSharp ("http://www.google.com");
			call.Wait ();
			Console.WriteLine( call.result.RawBytes.ToUtf8() );

		}		
```
		
		
さらに非同期TaskでラップしてWaitすると行ける
		
```csharp

		[Test]
		public void TestRestSharpWithTask()
		{

			var tcs = new TaskCompletionSource<string>();
			Task.Run (async () => {
				var res = await AsyncRestSharp("http://www.google.com");
				tcs.SetResult( res.RawBytes.ToUtf8());
			});
			tcs.Task.Wait();

			Console.WriteLine (tcs.Task.Result);
		}		
```
		

ちなみにToUtf8():

```csharp

	public static class Extensions
	{
		public static string ToUtf8(this byte[] src )
		{
			return System.Text.Encoding.UTF8.GetString (src);
		}
	}
```			

もうちょいコーディグが楽になるようなディレクティブとかできないかな。
