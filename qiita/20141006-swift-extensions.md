Swift vs. C# : Extensions

- クラス継承をしないで機能拡張

Swift:

- Add computed properties and computed static properties
- Define instance methods and type methods
- Provide new initializers
- Define subscripts
- Define and use new nested types
- Make an existing type conform to a protocol

C#: Extension Methods


- インスタンスメソッドが追加される(ように見える)


# Extension Syntax

Swift:

~~~
extension SomeType: SomeProtocol, AnotherProtocol {
    // implementation of protocol requirements goes here
}
~~~

-  [Adding Protocol Conformance with an Extension](https://developer.apple.com/library/prerelease/mac/documentation/Swift/Conceptual/Swift_Programming_Language/Protocols.html#//apple_ref/doc/uid/TP40014097-CH25-XID_405)


# Computed Properties

- Double を拡張するプロパティ

~~~
extension Double {
    var km: Double { return self * 1_000.0 }
    var m: Double { return self }
    var cm: Double { return self / 100.0 }
    var mm: Double { return self / 1_000.0 }
    var ft: Double { return self / 3.28084 }
}
~~~

~~~
  9> 10.0.km
$R0: Double = 10000
~~~

# Initializers

~~~
  1> struct Size { 
  2.     var width = 0.0, height = 0.0 
  3. } 
  4. struct Point { 
  5.     var x = 0.0, y = 0.0 
  6. } 
  7. struct Rect { 
  8.     var origin = Point() 
  9.     var size = Size() 
 10. }
~~~
 
~~~ 
 12> extension Rect { 
 13.     init(center: Point, size: Size) { 
 14.         let originX = center.x - (size.width / 2) 
 15.         let originY = center.y - (size.height / 2) 
 16.         self.init(origin: Point(x: originX, y: originY), size: size) 
 17.     } 
 18. }
~~~

~~~ 
 19> let centerRect = Rect(center: Point(x: 4.0, y: 4.0), 
 20. size: Size(width: 3.0, height: 3.0))
centerRect: Rect = {
  origin = {
    x = 2.5
    y = 2.5
  }
  size = {
    width = 3
    height = 3
  }
}
~~~

# Methods


~~~
  1> extension Int { 
  2.     func repetitions(task: () -> ()) { 
  3.         for i in 0..<self { 
  4.             task() 
  5.         } 
  6.     } 
  7. }
  8> 3.repetitions({ 
  9.     println("Hello!") 
 10.     })
~~~~

~~~
Hello!
Hello!
Hello!
~~~


C#: Extension Methods

~~~
csharp> public static class Extensions {
      >     public static void Repeat(this int i , Action<int> act ){
      >          for(int x=0; x < i; x++ ) act(x);
      >     }   
      > }
~~~

~~~      
csharp> 3.Repeat(delegate(int i){ Console.WriteLine(string.Format("{0} *** \n",i));});

0 *** 

1 *** 

2 *** 
~~~

# Mutating Instance Methods

- 破壊的

~~~
  1> extension Int { 
  2.     mutating func square() { 
  3.         self = self * self 
  4.     } 
  5. }
~~~  

~~~
  6> var someInt = 3
someInt: Int = 3
  7> someInt.square()
  8> someInt
$R0: Int = 9
~~~

# Subscripts

~~~
  1> extension Int { 
  2.     subscript(var digitIndex: Int) -> Int { 
  3.         var decimalBase = 1 
  4.         while digitIndex > 0 { 
  5.             decimalBase *= 10 
  6.             --digitIndex 
  7.         } 
  8.         return (self / decimalBase) % 10 
  9.     } 
 10. }
~~~

~~~ 
 11> 746381295[0]
$R0: Int = 5
 12> 746381295[1]
$R1: Int = 9
~~~

# Nested Types


~~~
  1> extension Int { 
  2.     enum Kind { 
  3.         case Negative, Zero, Positive 
  4.     } 
  5.     var kind: Kind { 
  6.         switch self { 
  7.         case 0: 
  8.             return .Zero 
  9.         case let x where x > 0: 
 10.             return .Positive 
 11.         default: 
 12.             return .Negative 
 13.         } 
 14.     } 
 15. }
~~~

~~~
 17> 3.kind
$R0: Int.Kind = Positive

 18> (-1).kind
$R1: Int.Kind = Negative

 19> 0.kind
$R2: Int.Kind = Zero
~~~

# C# Dynamic Type

[C# Dynamic](http://www.dotnetperls.com/dynamic) :

>Dynamic is advanced functionality.
>It can be useful.
>But usually it should be avoided.
>It erases many benefits of the C# language.


[Dynamic Object](http://msdn.microsoft.com/ja-jp/library/system.dynamic.dynamicobject.aspx)
([StackOverFlow](https://stackoverflow.com/questions/10512936/using-dynamic-to-add-methods)):

- Dictionaryのホルダーを内部に持って、System.Dynamic.DynamicObjectのメソッドのオーバーライドでごにょごにょする

~~~
using System.Dynamic;

class DynamicDuck : DynamicObject 
{
      Dictionary<string, object> dictionary
           = new Dictionary<string, object>();
    public int Count
    {   
        get { return dictionary.Count; }
    }   
    public override bool TryGetMember(
          GetMemberBinder binder, out object result)
    {   
          string name = binder.Name.ToLower();
            return dictionary.TryGetValue(name, out result);
    }   
    public override bool TrySetMember(
         SetMemberBinder binder, object value)
    {   
          dictionary[binder.Name.ToLower()] = value;
          return true;
    }   
 }
~~~

~~~
dynamic d = new DynamicDuck();
d.firstname = "Gideon";
d.Quack = (Action)(() => Console.WriteLine("Quack by " + d.firstname));
d.Quack();
~~~

~~~
Quack by Gideon
~~~
