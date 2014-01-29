Date: 2013-09-18  10:00
Title: Json.NET : カスタムシリアライザを含むオブジェクトをフラットにして送信する
Type: post  
Excerpt:   

ここでフラットにするというのは、
    
         var user = new User();
         user.Home.Zip = "111222"

というオブジェクトをJsonにするのに

        { "Home" : {"Zip" : "111222" } }
        
では無く、

        { "Home.Zip" : "1112222" }

とすること。これは、2つのJson

        [ "Home.Zip"]
        [ "1112222" ]
 
にわけることで、最初のメタデータのリストをネゴシエートしておけば、データのリストだけ送ることで、復元できるようにするため。要するにJsonデータを圧縮するということになります。


DateTimeを1970-01-01からの通算秒数にシリアライズするカスタムシリアライザ:

       public class TickSecondsConverter : JsonConverter
        {
            public static long ToTicks(DateTime datetime)
            {
                DateTime dateTime = (DateTime)datetime;
                TimeSpan span = dateTime.Subtract(new DateTime(1970, 1, 1, 0, 0, 0));
                return Convert.ToInt64(span.TotalSeconds);
            }

            public override void WriteJson(JsonWriter writer, object value,
                JsonSerializer serializer)
            {

                long ticks = 0;

                if (value is DateTime)
                {
                    ticks = ToTicks((DateTime)value);
                }
                writer.WriteValue(ticks);
            }
            public override object ReadJson(JsonReader reader, Type objectType, object existingValue,
                JsonSerializer serializer)
            {
                DateTime ret = new DateTime(1970, 1, 1, 0, 0, 0);
                return ret.AddSeconds(Convert.ToDouble(reader.Value));
            }

            public override bool CanConvert(Type objectType)
            {
                return (objectType == typeof(DateTime));
            }

        }
msec を無視しているのがポイント。

このシリアライザをつかった RootObject:

        public class RootObject
        {

            [JsonConverter(typeof(TickSecondsConverter))]
            public DateTime CreatedAt = DateTime.Now;

            public string ToJson()
            {
                return JsonConvert.SerializeObject(this,
                        Formatting.None,
                        new JsonSerializerSettings
                        {
                            TypeNameHandling = TypeNameHandling.None,
                            DefaultValueHandling = DefaultValueHandling.Ignore
                        });
            }
            public JObject ToJObject()
            {
                return JsonConvert.DeserializeObject<JObject>(
                     this.ToJson(),
                     new JsonSerializerSettings
                     {
                         TypeNameHandling = TypeNameHandling.None,
                         TypeNameAssemblyFormat =
                          System.Runtime.Serialization.Formatters.FormatterAssemblyStyle.Simple
                     }
                 );
            }
        }
        

RootObjectを継承した階層クラス構造をもつUser:

        public class User : RootObject
        {
            public class Address
            {
                public string Zip { get; set; }
                public string Prefecture { get; set; }
                public string City { get; set; }
                public string Town { get; set; }
            }

            public string FamilyName { get; set; }
            public string FirstName { get; set; }

            public Address Home { get; set; }
            public Address Office { get; set; }
            
        }       

カスタムシリアラザイザの処理を施したいので、一度Userなどのオブジェクトを一度Jsonに変換してからJObjectに戻す事で、変換済のデータを含んだ階層をトラバースできる。これをつかって、オブジェクトのデータをフラットにする：

        public static void FlattenJObject(
                    Dictionary<string, object> data, //フラット化したデータのコンテナ
                    string prefix,
                    JObject dict)
        {

            foreach(var item in dict )
            {
                var key = prefix + "." + item.Key;

                if (item.Value is JObject)
                {
                    FlattenJObject(data, key, 
                            (JObject)item.Value); //次の階層の処理
                }
                else
                {
                    data[key] = item.Value;
                }
            }
        }

テスト:

        [TestMethod]
        public void WithJObject()
        {
            /// サンプルユーザー
            var user = new User
            {
                FamilyName = "あああ",
                FirstName = "いいい",
                Home = new User.Address { Zip = "1112222" },
                Office = new User.Address { Zip = "3334444" }
            };
            Console.WriteLine(user.CreatedAt.ToString());
            // 2013/09/18 10:36:16    とか        
            Console.WriteLine(user.ToJson());
            /* 階層化している
            {"CreatedAt":1379500576,"FamilyName":"あああ","FirstName":"いいい",
               "Home":{"Zip":"1112222"},
               "Office":{"Zip":"3334444"}}
            */
                        

            // フラット構造に変える
            var flat_map = new Dictionary<string, object>();
            FlattenJObject(flat_map, "user", user.ToJObject());
            Console.WriteLine(JsonConvert.SerializeObject(flat_map));
            /*
            {  "user.CreatedAt":1379500576,"user.FamilyName":"あああ",
               "user.FirstName":"いいい","user.Home.Zip":"1112222",
               "user.Office.Zip":"3334444"}
            */
            
            // 構造化Dictionaryに変換する
            var structured_map = new Dictionary<string, object>();
            foreach (var item in flat_map)
            {
                var keys = item.Key.Split('.');
                var val = item.Value;

                var target = structured_map;
                if (keys.Length > 1)
                {
                    for (int x = 0; x < keys.Length - 1; x++)
                    {
                        if (!target.ContainsKey(keys[x]))
                        {

                            target[keys[x]] = new Dictionary<string, object>();
                        }
                        target = (Dictionary<string, object>)target[keys[x]];
                    }
                }

                target[keys[keys.Length - 1]] = val;
            }
            Console.WriteLine(JsonConvert.SerializeObject(structured_map));
            /*
            {"user":
               {"CreatedAt":1379500576,"FamilyName":"あああ","FirstName":"いいい",
                 "Home":{"Zip":"1112222"},"Office":{"Zip":"3334444"}
               }
            }
            */
           
            // Userを復元する
            User restored_user = null;
            if (structured_map.ContainsKey("user"))
            {
                restored_user = JsonConvert.DeserializeObject<User>
                    (JsonConvert.SerializeObject(structured_map["user"]));
            }

            Assert.IsNotNull(restored_user);
            Assert.AreEqual(restored_user.Office.Zip,
                                user.Office.Zip);
            Assert.AreEqual(restored_user.CreatedAt.ToString(),
                                 user.CreatedAt.ToString());
            Assert.AreNotEqual(restored_user.CreatedAt,
                                user.CreatedAt);
        }       
        