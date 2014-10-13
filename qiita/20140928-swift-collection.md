Swift vs. C#: Collection Types

# Collection Types

Swift:

1. Array(ordered lists of values of the same type)
2. Dictionary(unordered collections of values of the same type)


C#:

1. System.Collections
2. System.Collections.Generic
3. System.Collections.Concurrent
4. System.Collections.Specialized
5. System.Collections.Immutable

# Mutability of Collections

- Mutable & Immutable (Swift/C#)

~~~
  1> var mutable: [String] = ["Cat", "Dog"]
mutable: [String] = 2 values {
  [0] = "Cat"
  [1] = "Dog"
}
  2> mutable[0] = "Mouse"
  3> mutable
$R0: [String] = 2 values {
  [0] = "Mouse"
  [1] = "Dog"
}
~~~

~~~
  4> let immutable: [String] = mutable
immutable: [String] = 2 values {
  [0] = "Mouse"
  [1] = "Dog"
}
  5> immutable[0] = "Pig"
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/9119/repl9.swift:2:1: error: '@lvalue $T5' is not identical to 'String'
immutable[0] = "Pig"
^

~~~

- var宣言しないとimmutable(それはそうか)

~~~
 15> Array<Int>().append(0)
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/9119/repl31.swift:2:1: error: immutable value of type 'Array<Int>' only has mutating members named 'append'
Array<Int>().append(0)
^            ~~~~~~

~~~

~~~
csharp> var mutable = new List<string>{ "Cat", "Dog" };
csharp> mutable
{ "Cat", "Dog" }
csharp> mutable[0] = "Mouse";
csharp> mutable
{ "Mouse", "Dog" }
~~~

~~~
csharp> var immutable = mutable.AsReadOnly();     
csharp> immutable
{ "Mouse", "Dog" }
csharp> immutable[0] = "Pig";
(1,11): error CS0200: Property or indexer `System.Collections.ObjectModel.ReadOnlyCollection<string>.this[int]' cannot be assigned to (it is read-only)
~~~~

- readonly しても mutable

~~~
csharp> class Animal { public readonly static List<string> Animals = new List<string>{"Cat", "Dog"};};  
csharp> Animal.Animals
{ "Cat", "Dog" }
csharp> Animal.Animals[0] = "Pig";
csharp> Animal.Animals  
{ "Pig", "Dog" }
~~~

- ただし readonly なので

~~~
csharp> Animal.Animals = new List<string>();
(1,9): error CS0198: A static readonly field `Animal.Animals' cannot be assigned to (except in a static constructor or a variable initializer)
~~~

- ReadOnlyCollection型で宣言

~~~
csharp> using System.Collections.ObjectModel;
csharp> class Animal { public static ReadOnlyCollection<string> Animals = new List<string>{"Cat", "Dog"}.AsReadOnly();};  
csharp> Animal.Animals[0] = "Pig"
(1,16): error CS0200: Property or indexer `System.Collections.ObjectModel.ReadOnlyCollection<string>.this[int]' cannot be assigned to (it is read-only)
~~~


# Arrays

## Array Type Shorthand Syntax

~~~
  5> var a : Array<String> = ["Cat", "Dog"]
a: [String] = 2 values {
  [0] = "Cat"
  [1] = "Dog"
}
~~~

~~~
  6> var a : [String] = ["Cat", "Dog"]
a: [String] = 2 values {
  [0] = "Cat"
  [1] = "Dog"
}
~~~

- C# : 短縮系は無いと思う

## Array Literals

~~~
  7> [1, 2, 3]
$R1: [Int] = 3 values {
  [0] = 1
  [1] = 2
  [2] = 3
}
~~~

~~~
  9> ["Apple", "Oragnge"]
$R3: [String] = 2 values {
  [0] = "Apple"
  [1] = "Oragnge"
}
~~~

- C# : リテラルとかない。コンストラクタ必須

~~~
csharp> new int[]{1, 2, 3};
{ 1, 2, 3 }
~~~


## Accessing and Modifying an Array

~~~
 10> var a: [String]
a: [String] = 0 values
 11> a.isEmpty
$R4: Bool = true

 12> a.count
$R5: Int = 0
~~~

~~~
csharp> (new string[]{}).Length == 0
true
~~~

~~~
 19> var a: [String]
a: [String] = 0 values
 20> a.append("Dog")
 21> a
$R9: [String] = 1 value {
  [0] = "Dog"
}
~~~

~~~
csharp> var a = new List<string>{};
csharp> a.Add("Dog");
csharp> a
{ "Dog" }
~~~

~~~
 22> a += ["Cat", "Pig"]
 23> a
$R10: [String] = 3 values {
  [0] = "Dog"
  [1] = "Cat"
  [2] = "Pig"
}
~~~

~~~
csharp> a.Concat(new List<string>{"Cat", "Pig"});
{ "Dog", "Cat", "Pig" }
csharp> a
{ "Dog" }

csharp> a += new List<string>{"Cat", "Pig"};  
(1,2): error CS0019: Operator `+=' cannot be applied to operands of type `System.Collections.Generic.List<string>' and `System.Collections.Generic.List<string>'

~~~


~~~
 25> var a = Array(1...5)
a: [Int] = 5 values {
  [0] = 1
  [1] = 2
  [2] = 3
  [3] = 4
  [4] = 5
}

 26> a[2...3] = [10, 20]
 27> a
$R11: [Int] = 5 values {
  [0] = 1
  [1] = 2
  [2] = 10
  [3] = 20
  [4] = 5
}

~~~

- C# 苦しい

~~~
csharp> var a = Enumerable.Range(1,5).ToList<int>();
csharp> a.GetType();
System.Collections.Generic.List`1[System.Int32]
csharp> a.InsertRange(2, new List<int>{10,20})       
csharp> a.RemoveRange(4, 2);                         
csharp> a
{ 1, 2, 10, 20, 5 }
~~~


~~~
 29> a.insert(100, atIndex:0)
 30> a
$R13: [Int] = 6 values {
  [0] = 100
  [1] = 1
  [2] = 2
  [3] = 10
  [4] = 20
  [5] = 5
}
 31> a.removeAtIndex(1)
$R14: (Int) = 1
 32> a
$R15: [Int] = 5 values {
  [0] = 100
  [1] = 2
  [2] = 10
  [3] = 20
  [4] = 5
}
 33> a.removeLast()
$R16: Int = 5
~~~

~~~
csharp> a.RemoveAt(a.Count() -1)  
csharp> a
{ 1, 2, 10, 20 }
csharp> a.Insert(0, 9999)   
csharp> a
{ 9999, 1, 2, 10, 20 }
~~~


## Iterating Over an Array


~~~
 34> var a = Array(1...5)
a: [Int] = 5 values {
  [0] = 1
  [1] = 2
  [2] = 3
  [3] = 4
  [4] = 5
}
 36> for i in a { print("\(i),")};println()
1,2,3,4,5,

~~~

~~~
csharp> foreach(var i in Enumerable.Range(1, 5).ToList<int>()){ Console.Write(string.Format("{0},", i));} ; Console.WriteLine();
1,2,3,4,5,
~~~

~~~
 37> for (i, value) in enumerate(a) { print("\(i):\(value),")};println() 
0:1,1:2,2:3,3:4,4:5,
~~~

~~~
csharp> foreach(var item in a.OfType<object>().Select((value, index) => new {value, index})){
      >    Console.Write(string.Format("{0}:{1}, ", item.value, item.index));                 
      > }
1:0, 2:1, 3:2, 4:3, 5:4,
~~~


## Creating and Initializing an Array

~~~
 40> var a = [Double](count: 3, repeatedValue: 0.1)
a: [(Double)] = 3 values {
  [0] = 0.10000000000000001
  [1] = 0.10000000000000001
  [2] = 0.10000000000000001
}
~~~

~~~
csharp> Enumerable.Repeat(0.1, 3).ToList<double>();
{ 0.1, 0.1, 0.1 }
~~~


# Dictionaries

## Dictionary Type Shorthand Syntax / Dictionary Literals


~~~
 41> ["TYO": "Tokyo", "DUB": "Dublin"]
$R18: [String : String] = {
  [0] = {
    key = "TYO"
    value = "Tokyo"
  }
  [1] = {
    key = "DUB"
    value = "Dublin"
  }
}

 42> var city : Dictionary<String, String> = ["TYO": "Tokyo", "DUB": "Dublin"] 
city: [String : String] = {
  [0] = {
    key = "TYO"
    value = "Tokyo"
  }
  [1] = {
    key = "DUB"
    value = "Dublin"
  }
}

~~~

- C#: コンストラクタ必要

## Accessing and Modifying a Dictionary

~~~
 43> city.isEmpty
$R19: Bool = false

 44> city.count
$R20: Int = 2
~~~


~~~
csharp> var city = new Dictionary<string,string>{{"TYO", "Tokyo"}, {"DUB", "Dublin"}};

csharp> city.Count()
2
~~~

~~~
 45> city["SFO"] = "San Francisco"
 
 46> city
$R21: [String : String] = {
  [0] = {
    key = "SFO"
    value = "San Francisco"
  }
  [1] = {
    key = "TYO"
    value = "Tokyo"
  }
  [2] = {
    key = "DUB"
    value = "Dublin"
  }
}
~~~

~~~
csharp> city["SFO"] = "San Francisco"
csharp> city
{{ "TYO", "Tokyo" }, { "DUB", "Dublin" }, { "SFO", "San Francisco" }}
~~~

~~~
47> city.removeValueForKey("DUB")
$R22: String? = "Dublin"

 48> city
$R23: [String : String] = {
  [0] = {
    key = "TYO"
    value = "Tokyo"
  }
  [1] = {
    key = "SFO"
    value = "San Francisco"
  }
}
~~~

~~~
csharp> city.Remove("DUB")
true

csharp> city
{{ "TYO", "Tokyo" }, { "SFO", "San Francisco" }}
~~~

## Iterating Over a Dictionary

~~~
 49> for(key, value) in city { println("\(key)=\(value)") } 
TYO=Tokyo
SFO=San Francisco
~~~

~~~
csharp> foreach(var item in city){ Console.WriteLine(string.Format("{0}={1} ", item.Key, item.Value));}
TYO=Tokyo 
SFO=San Francisco 
~~~


~~~
 50> city.keys
$R24: LazyBidirectionalCollection<MapCollectionView<[String : String], String>> = {
  _base = {
    _base = {
      [0] = {
        key = "TYO"
        value = "Tokyo"
      }
      [1] = {
        key = "SFO"
        value = "San Francisco"
      }
    }
    _transform =
  }
}
 51> city.values
$R25: LazyBidirectionalCollection<MapCollectionView<[String : String], String>> = {
  _base = {
    _base = {
      [0] = {
        key = "TYO"
        value = "Tokyo"
      }
      [1] = {
        key = "SFO"
        value = "San Francisco"
      }
    }
    _transform =
  }
}
~~~
~~~
 52> Array(city.keys)
$R26: [String] = 2 values {
  [0] = "TYO"
  [1] = "SFO"
}
 53> Array(city.values)
$R27: [String] = 2 values {
  [0] = "Tokyo"
  [1] = "San Francisco"
}

 55> [String](city.keys)
$R28: [(String)] = 2 values {
  [0] = "TYO"
  [1] = "SFO"
}

~~~

~~~
 54> for i in city.keys { println("\(i)")}
TYO
SFO
~~~

~~~
csharp> city.Keys
{ "TYO", "SFO" }

csharp> city.Values
{ "Tokyo", "San Francisco" }

csharp> city.Keys.GetType()
System.Collections.Generic.Dictionary`2+KeyCollection[System.String,System.String]
~~~

##　Creating an Empty Dictionary

~~~
 56> [Int: String]()
$R29: [Int : String] = {}
 57> var d = [String: String]()
d: [String : String] = {}
 58> d["TYO"] = "Tokyo"
 59> d = [:]
 60> d
$R30: [String : String] = {}
~~~

~~~
csharp> var d = new Dictionary<string, string>();
csharp> d["TYO"] = "Tokyo"
csharp> d
{{ "TYO", "Tokyo" }}

csharp> d.Clear()

csharp> d
{}
~~~

## Hash Values for Dictionary Key Types

- Swift : Key はハッシュできないといけない(hashable)

~~~
 61> "TYO".hashValue
$R31: Int = 4799450059715620566
~~~

- C# : カスタムオブジェクトをキーにするならGetHashCode, Equalsをオーバーライドすること

~~~
csharp> "TYO".GetHashCode()
83562
~~~

- 以下は問題ない

~~~
		public class Profile {
			public string Name { get; set; }
		}

		[Test()]
		public void PlayGround()
		{
			var d = new Dictionary<Profile, string> ();

			var p1 = new Profile{ Name = "hoge" };
			var p2 = new Profile{ Name = "foo" };
			d [p1] = "hoge";
			d [p2] = "foo";

			Assert.AreNotEqual (
				p1.GetHashCode (), p2.GetHashCode ());

		}
~~~		



