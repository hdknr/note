Date: 2013-07-11  12:00
Title:  Json.NET : 型付き定数のシリアライズ
Type: post  
Excerpt:   

IntelliSense で補完させたりしたいので、定数クラスを作ってそれにstatic readonlyのインスタンスを定義するなど。そのままJson.NETでシリアライズするとクラスでシリアライズされてしまうのでカスタムシリアライザを定義するといいんでしょう。


Constant クラス:

    /// <summary>
    /// 定数の管理
    /// </summary>
    public class Constant
    {
        protected string _value;
        public string Value { get { return _value; } }

        public static bool operator ==(Constant a, Constant b)
        {
            return a._value == b._value;
        }
        public static bool operator !=(Constant a, Constant b)
        {
            return a._value != b._value;
        }
        public override bool Equals(object obj)
        {
            return (this.GetType() == obj.GetType() 
                    && this._value == ((Constant)obj)._value);

        }
        /// <summary>
        /// 定数の変換
        /// </summary>
        /// <typeparam name="T"></typeparam>
        public class ConstantConverter<T> : JsonConverter
        {

            public override void WriteJson(JsonWriter writer, object value,
                JsonSerializer serializer)
            {

                writer.WriteValue(
                     typeof(T).GetProperty("Value").GetValue(value, null)
                    );

            }
            public override object ReadJson(JsonReader reader, Type objectType, object existingValue,
                JsonSerializer serializer)
            {
                var ctor = typeof(T).GetConstructor(new Type[] { typeof(string) });
                return ctor.Invoke(new object[] { reader.Value });
            }

            public override bool CanConvert(Type objectType)
            {
                return (objectType == typeof(string));
            }

        }

    }

このサブクラスで実際の定数を管理:


    public class JweAlg : Constant
    {
        public JweAlg(string value) { _value = value; }

        #region Jwe
        public static readonly JweAlg RSA1_5 = new JweAlg( "RSA1_5" );
        public static readonly JweAlg RSA_OAEP = new JweAlg("RSA-OAEP");
        public static readonly JweAlg A128KW = new JweAlg("A128KW");
        public static readonly JweAlg A256KW = new JweAlg("A256KW");
        public static readonly JweAlg dir = new JweAlg("dir" );
        public static readonly JweAlg ECDHES = new JweAlg("ECDH-ES" );
        public static readonly JweAlg ECDHES_A128KW = new JweAlg( "ECDH-ES+A128KW" );
        public static readonly JweAlg ECDHES_A256KW = new JweAlg( "ECDH-ES+A256KW" );
        #endregion

    }

定数はこうやって使う:


        public class Jwe
        {
            [JsonConverter(typeof(Constant.ConstantConverter<JweAlg>))]
            public JweAlg alg { get; set; }  

            public static Jwe FromJson(string json)
            {

                var ret = JsonConvert.DeserializeObject<Jwe>(json,
                    new JsonSerializerSettings
                    {
                        NullValueHandling = NullValueHandling.Ignore
                    }

                    );

                return ret;
            }

            public string ToJson(string[] excludes = null)
            {
                return JsonConvert.SerializeObject(this,
                     new JsonSerializerSettings
                     {
                         ContractResolver = new JsonResolver(excludes),
                         NullValueHandling = NullValueHandling.Ignore
                     }
                    );
            }


        }

テストコード:

            var jwe = new Jose.Jwe() { alg = Jose.JweAlg.ECDHES_A128KW};
            var jwe2 = Jose.Jwe.FromJson(jwe.ToJson());
            Assert.IsTrue(jwe2.alg == Jose.JweAlg.ECDHES_A128KW);
            