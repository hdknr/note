NewtonSoft.Json: 型に定義されていないフィールドを辞書に入れる

タイプシリアライザで処理されないフィールドをJTokenで辞書にいれるので、Linq が必要:

```cs

    using Newtonsoft.Json;
    using Newtonsoft.Json.Converters;
    using Newtonsoft.Json.Linq;
```

Number, Name を受け付ける。 id はJsonにしない。 
定義しないフィールドは Extends の辞書に入れる。::


```cs

        public class MyToken 
        {
            [JsonIgnore]
            public int? id {get;set;}
            public int Number { get; set; }
            public string Name { get; set; }

            [JsonExtensionData]
            public IDictionary<string, JToken> Extends;

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

        }
```