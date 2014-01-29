Date: 2013-06-22
Title: MVC4 Web API : Put,Post は voidなので 204(No Content)が返ります

デフォルトのWeb API コントローラ

        // POST api/clientinfo
        public void Post([FromBody]string value)
        {
        }

        // PUT api/clientinfo/5
        public void Put(int id, [FromBody]string value)
        {
        }


テストコード

			// RestSharp 使ってます
            request =  new RestRequest("/api/clientinfo", Method.POST)
                 {
                     RequestFormat = DataFormat.Json,
                      
                 };
            request.AddBody(new { client_id = "i_am_a_client" });
            response =( new RestClient(url)).Execute( request );

            Assert.AreEqual(response.StatusCode, 					System.Net.HttpStatusCode.NoContent);　　　　// 204

            

200で登録されたオブジェクトをJsonで返す修正バージョンコントローラ。

        	// POST api/clientinfo
  			// public void Post([FromBody]string value)
        	public object Post([FromBody]Dictionary<string,string> value)
        	{
            	return new { id = 1, 
                	client_id="hello_new_client", 
               		response_uri=value["response_uri"] };
        	}   


テストコード

            request =  new RestRequest("/api/clientinfo", Method.POST)
                 {
                     RequestFormat = DataFormat.Json,
                      
                 };
            request.AddBody(new { response_uri = "http://i_am_a_client/response" });
            response =( new RestClient(url)).Execute( request );

            Assert.AreEqual(response.StatusCode, System.Net.HttpStatusCode.OK); // 200

			// Json.NET で戻しています
            var jres= JsonConvert.DeserializeObject<Dictionary<string, object>>(response.Content);

            Assert.AreEqual(jres["client_id"], "hello_new_client");

ちなみにWeb APIのASP.NETの 設定は、XMLのシリアライザをドロップして、Jsonで処理するようにしています

		/// App_Start/WebApiConfig.cs
		///
        public static void Register(HttpConfiguration config)
        {
            config.Routes.MapHttpRoute(
                name: "DefaultApi",
                routeTemplate: "api/{controller}/{id}",
                defaults: new { id = RouteParameter.Optional }
            );

            // XMLフォーマッタを使わない -> (Content-Typeが指定されないと)Jsonが使われる
            config.Formatters.Remove(config.Formatters.XmlFormatter);  
        }