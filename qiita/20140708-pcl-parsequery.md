C#:PCL版の URI Query の Dictionary化

```csharp


    using System;
    using System.Linq;
    using System.Collections.Generic;
    using NUnit.Framework;

    using MonoTouch.UIKit;

	[TestFixture]
	public class UnitMisc : UnitBase
	{
  
		public Dictionary<string, string> ParseQuery(string query)
		{
			return query
					.Split ("?&".ToCharArray ())
					.Where (i => string.IsNullOrEmpty (i) == false)
					.Select (i => i.Split ('='))
					.ToDictionary (
						i => Uri.UnescapeDataString (i [0]), 
						i => Uri.UnescapeDataString (i [1]));
		}


		
		[Test]
		public void TestUri()
		{

			var authreq = _ (@"
			openid://?
  			response_type=id_token
  			&client_id=https%3A%2F%2Fclient.example.org%2Fcb
  			&scope=openid%20profile
  			&state=af0ifjsldkj
  			&nonce=n-0S6_WzA2Mj
  			&registration=%7B%22logo_uri%22%3A%22https%3A%2F%2F
    		client.example.org%2Flogo.png%22%7D
			");

			var uri = new Uri (authreq);

			var query = ParseQuery (uri.Query);

			Assert.AreEqual (query.Count, 6);
			Assert.AreEqual (query ["response_type"], "id_token");
			Assert.AreEqual (query ["client_id"], "https://client.example.org/cb");
			Assert.AreEqual (query ["state"], "af0ifjsldkj");
			Assert.AreEqual (query ["scope"], "openid profile");
			Assert.AreEqual (query ["nonce"], "n-0S6_WzA2Mj");
			Assert.AreEqual (query ["registration"],
				@"{""logo_uri"":""https://client.example.org/logo.png""}");

		}
	}
```		
