PCL : ReflectinでGetConsturctor(s)が使えないっぽい


ので、typeof(クラス).GetTypeFino().DeclaredConstructors から探す方向で。

```csharp

    using System;
    using System.Linq;
    using System.Reflection;
```   
    
３つのコンストラクタを持つサンプルクラス:


```csharp

	public class Person
	{
		public string nickname = "";

		public Person(){}
		public Person(string firstname, string lastname){
		}
		public Person(string nickname){
			this.nickname = nickname;
		}

	}  
	  
```    

Person(string nickname)を探すテスト:


```csharp

		[Test]
		public void TestFindConstructor()
		{
			var t = typeof(Person).GetTypeInfo ();
			
			var cs = t.DeclaredConstructors.Where (
				ci => ci.GetParameters ().Count() == 1 &&
				ci.GetParameters().First().ParameterType == typeof(System.String)
			).FirstOrDefault();
				
			Assert.IsNotNull (cs);
			var person = (Person)cs.Invoke (new string[]{ "Monkey" });
			Assert.AreEqual (person.nickname, "Monkey");
		}
```		
