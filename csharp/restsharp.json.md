## 簡単な例

### サーバー

- Django REST Framework
- `Token` で認証されたユーザーの名前を返す

~~~py
from django.contrib.auth.decorators import permission_required
from rest_framework import (
    decorators, authentication, permissions,)

from app.views import JSONResponse

@decorators.api_view(['GET', 'POST', ])
@decorators.authentication_classes((authentication.TokenAuthentication,))
@decorators.permission_classes((permissions.IsAuthenticated,))
@permission_required('drivers.change_drivingstatus')
def default(request):
    print request.data
    data = dict(endpont="default", status='OK',
                user=request.user.username, **request.POST)
    res = JSONResponse(data)
    return res
~~~    


### クライアント


~~~csharp

using System.Linq;
using System.Collections.Generic;

using RestSharp.Portable;
using RestSharp.Portable.HttpClient;

using Newtonsoft.Json.Linq;

namespace TourPortable
{
	public class MyClass
	{
		public MyClass ()
		{
		}

		public static async void Run()
		{
			var base_url = "http://myapp.deb:8000";
			using (var client = new RestClient (base_url)) {
				var req = new RestRequest ("/drivers/api/", Method.POST)
					.AddHeader ("Authorization", "Token 686abb26a73511e5a9a1080027b4adda")
					.AddJsonBody (
						new Dictionary<string, string>(){
							{"name1", "value1"}, {"name2", "value"}
						});

				var res = await client.Execute<JObject> (req);

				System.Diagnostics.Debug.Assert (res.ContentType == "application/json");
				System.Diagnostics.Debug.Assert (res.Data.Value<string>("status") == "OK");		
				System.Diagnostics.Debug.WriteLine ("USER = " + res.Data.Value<string> ("user"));
			}

		}
	}
}
~~~

### Actionコールバックを引数にする場合

~~~csharp
using Newtonsoft.Json.Linq;

// ボタンタップ
partial void UIButton3_TouchUpInside (UIButton sender)
{
  MyClass.RunAction((JObject obj) =>  {
    Console.WriteLine("USER=" + obj.Value<string>("user"));
  });
}
~~~

~~~csharp
public static async void RunAction(Action<JObject> action)
{
  var base_url = "http://eco.deb:8000";
  using (var client = new RestClient (base_url)) {
    var req = new RestRequest ("/drivers/api/", Method.POST)
      .AddHeader ("Authorization", "Token 686abb26a73511e5a9a1080027b4adda")
      .AddJsonBody (
        new Dictionary<string, string>(){
          {"name1", "value1"}, {"name2", "value"}
        });

    var res = await client.Execute<JObject> (req);
    action (res.Data);
  }
}
~~~
