Date: 2013-07-10  16:00
Title:  RestSharp: AddBodyに文字列渡すとさらにシリアライズされてしまう
Type: post  
Excerpt:   

ので、シリアリズ済の文字列をBodyにセットするにはAddParameterでリクエストオブジェクトを作るようです:

        /// リクエストオブジェクトを作ります　: Requestクラスを作っています
        protected RestRequest CreateRequest(string payload, DataFormat format = DataFormat.Json)
        {
            var ret = new RestRequest(this.Path, this._method);    // Path,_methodは別途用意
            ret.RequestFormat = format;
            ret.AddParameter( (format == DataFormat.Json ) ? "application/json" : "text/xml", 
                payload, ParameterType.RequestBody);
            //  ret.AddBody(payload);            // これだと文字列がさらにシリアライズされてしまう
            return ret;

        }

        
このリクエストオブジェクトをPOSTするには:

        public IRestResponse Post(string payload, string path =null, 
                                   DataFormat format = DataFormat.Json )
        {   
            if ( !string.IsNullOrEmpty(path))    
            {   
                this.Path = path;
            }   

            if (this.Client == null)
                this.CreateClient();

            this._method = Method.POST;            // あるいは、PUT

            return this.Client.Execute(
                            this.CreateRequest(payload,format)
                        ) ;
        }   
     
ちなみにクライアントオブジェクトはこうやってます:


        protected void CreateClient()
        {
            this.Client = new RestClient(this.BaseUrl);
            if (this._auth_basic != null)
            {
                this.Client.Authenticator = this._auth_basic;
            }
        }        

パスを指定するのめんどくさいので、コンストラクタでBaseUrlとパスの分割:


        public Requester(string url) : this()
        {
            Uri u = new Uri(url);
            this.Path = u.AbsolutePath;

            this.BaseUrl = Regex.Replace(url, this.Path + "$", "");

        }

最終的にはこんな呼び方:


        public bool PostObject(string url, MyObject obj)
        {
            var req = new Requester(url);
            var res = req.Post(obj.ToJson(),string.Empty,DataFormat.Json);    //ToJsonで独自にシリアライズ
            return res.StatusCode == System.Net.HttpStatusCode.OK;            // OK?
        }