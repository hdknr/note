using System;
using System.Threading.Tasks;

using RestSharp.Portable;
using RestSharp.Portable.HttpClient;

using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

using Akavache;
using Akavache.Sqlite3;

using NetTopologySuite;
using NetTopologySuite.IO.Converters;
using NetTopologySuite.Geometries;

namespace AppLib
{
	public class UrlResource: RestRequest
	{
		public BaseApi () { }
		public BaseApi(
      string path , Method method = Method.POST):base(path, method) { }

		public static RestClient CreateClient(){
			return new RestClient (Helpers.Settings.BaseUrl);
		}

		public string Url {
			get { return string.Format("{0}{1}",
				Helpers.Settings.BaseUrl, this.Resource);}
		}

		public async Task<JToken> Get(){
			using (var client =CreateClient()) {
				this.SetPayload ();
				var res = await  client.Execute<JToken> (this);
				return res.Data;
			}
		}

		public void GetObject<T>(Action<T> action)
		{
			BlobCache.LocalMachine.GetOrFetchObject<JToken> (
				this.Url,             // URL as Key
				() => this.Get ())
			.Subscribe (o => action (o.ToObject<T> ()));
		}

    // TODO: use Akavache
		public void SetToken(string token=null){
			token = token?? Helpers.Settings.Token;
			this.AddHeader ("Authorization", "Token " + token);
		}

		public Point Location {get; set ;}

		public class Payload {
			[JsonConverter(typeof(AppLib.GeosConverter))]
			public Point  location { get; set; }
		}

		public virtual void SetPayload(){
			this.AddJsonBody (
				new Payload{ location = this.Location }
			);
		}
	}
}
