NewtonSoft.Json: 型に定義されていない任意のフィールドを辞書に追加する(インデクサ)


受け取ったJSONのパースではなく、任意のフィールドを追加してJSONにして渡す。
ExtendsをDictionary<string,JToken> でつくって、JTokenでset/getするインデクサを用意する。
        

```cs

        public class MyToken 
        {
            [JsonIgnore]
            public int? id {get;set;}
            public int Number { get; set; }
            public string Name { get; set; }

            [JsonExtensionData]
            protected IDictionary<string, JToken> Extends = new Dictionary<string, JToken>();                   
  
            public JToken this[string name]
            {
                get { return this.Extends[name]; }
                set {this.Extends[name] = value;}
            }
        }
```
        
テスト:

```cs
        
        [TestMethod]
        public void TestSerializerExtensible()
        {

            var token_str = @"
            { ""Number"": 432143, ""Name"" : ""Hoge Hoge"", ""http://hoge.com/"" : true, ""id"":35 }
            ";

            var token =  JsonConvert.DeserializeObject<MyToken>(token_str);

            Assert.AreEqual(token.Name, "Hoge Hoge");
            Assert.AreEqual(token.Number, 432143);
            Assert.IsNull(token.id);

            token.id = 1;
            Assert.IsTrue(token.Extends["http://hoge.com/"].ToObject<bool>());
            Assert.AreEqual(token.Extends["id"].ToObject<int>(), 35);
            Assert.AreEqual(token.id, 1);
            
            // 新規作成
            var token2 = new MyToken();

            token2["My name is"] = "Prince";
            token2["My age is"] = 9;
            var str2 = JsonConvert.SerializeObject(token2);
            Console.WriteLine(str2);    

            // 復元
            var token3 = JsonConvert.DeserializeObject<MyToken>(str2);
            Assert.AreEqual(token3["My age is"], 9);
            Assert.AreEqual(token3["My name is"], "Prince");


        }
```