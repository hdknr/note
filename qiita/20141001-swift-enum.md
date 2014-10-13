Swift vs. C#: Enumerations



# Enumeration Syntax


~~~
 74> enum CompassPoint { 
 75.     case North 
 76.     case South 
 77.     case East 
 78.     case West 
 79. }
~~~
~~~
 83> enum CompassPoint { 
 84.     case North, South, East, West 
 85. }    
~~~

~~~
 80> var i = CompassPoint.North
i: CompassPoint = North
 81> i = .South
 82> i
$R27: CompassPoint = South
~~~

C#:

~~~
    enum CompassPoint { 
        North, South, East, West 
    } ; 
    
    public static void Run()
    {
        var i = CompassPoint.South;
        Assert(i == CompassPoint.South);
    }
~~~		


# Matching Enumeration Values with a Switch Statement



~~~
 87> j = .West
 88> j == .West
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/40015/repl120.swift:2:3: error: could not find member 'West'
j == .West
~~^~~~~~~~
~~~

~~~
 88> switch j { case .West: println("Yes");  default: println("?"); } 
Yes
~~~

~~~
csharp>     enum CompassPoint { 
      >         North, South, East, West 
      >     } ; 

csharp> var i = CompassPoint.East 
csharp> i == CompassPoint.East
true
~~~	

# Associated Values


> You can define Swift enumerations to store associated values of any given type, 
> and the value types can be different for each member of the enumeration if needed. 

~~~
 89> enum Barcode { 
 90.     case UPCA(Int, Int, Int, Int) 
 91.     case QRCode(String) 
 92. }
 
 
 93> var bc1 = Barcode.UPCA(1,1,1,1)
bc1: Barcode = UPCA {
  UPCA = {
    0 = 1
    1 = 1
    2 = 1
    3 = 1
  }
}
 94> var bc2 = Barcode.UPCA(2,2,2,2)
bc2: Barcode = UPCA {
  UPCA = {
    0 = 2
    1 = 2
    2 = 2
    3 = 2
  }
}
 96> switch bc2 {  
 97.     case .UPCA(1,1,1,1): println("1");  
 98.     case .UPCA(2,2,2,2): println("2");  
 99.     default: println("?") 
100. } 
2
~~~

C# : これはできないので、static readonly T  t =  new T(){} とかやるかな？

~~~

public class BarcodeEnum
{
   public static readonly UPCA UPCA1 = new UPCA(1,1,1,1);
   public static readonly UPCA UPCA2 = new UPCA(2,2,2,2);
   public static readonly QRCode QRCodeApple = new QRCode("apple.com");
}

Assert( var1 == BarcodeEnum.UPCA1);
~~~

>Enumerations similar to these are known as discriminated unions, tagged unions, or variants in other programming languages.

- [Discriminated Unions(F#)](http://msdn.microsoft.com/en-us/library/dd233226.aspx)
- [Tagged Unions](https://en.wikipedia.org/wiki/Tagged_union)
- [Variant type](https://en.wikipedia.org/wiki/Variant_type)

# Raw Values

Swift:

~~~
 107> enum CompassPoint: Character{
 108.     case North="N", South="S", East="E", West="W"
 109. } 
~~~
 
~~~
 110> enum CompassPoint: Int{
 111.     case North=0, South, East, West 
 112. } 
~~~

~~~
  9> CompassPoint.North.toRaw() == 0
$R2: Bool = true
~~~

C#:

~~~
    enum CompassPoint { 
        North=0, South, East, West 
    } ; 
~~~
~~~
Assert ((int)i == 1);
Assert (i.ToString () == "South");
~~~
    
# Initializing from a Raw Value


Swift: よくわからん

~~~
 16> CompassPoint.fromRaw(0) 
$R7: CompassPoint? = Some
 17> CompassPoint.fromRaw(1)
$R8: CompassPoint? = Some
 18> CompassPoint.fromRaw(2)
$R9: CompassPoint? = Some
 19> CompassPoint.fromRaw(3)
$R10: CompassPoint? = Some
 20> CompassPoint.fromRaw(4)
$R11: CompassPoint? = nil
~~~

~~~
 32> var i = CompassPoint.fromRaw(0) 
i: CompassPoint? = Some

 36> i?.toRaw()
$R18: Int? = 0

 37> i?
$R19: CompassPoint? = Some

 38> i?.toRaw() == CompassPoint.North.toRaw()
$R20: Bool = true

~~~

C#: 文字列からも戻せる

~~~
    enum CompassPoint { 
        North=0, South, East, West 
    } ; 
    
    public static void Run()
    {   
        var i = CompassPoint.South;

        Assert(i == CompassPoint.South);

        Assert(i == (CompassPoint)1);
        Assert(i == (CompassPoint)Enum.ToObject(typeof(CompassPoint), 1));
        Assert(i == (CompassPoint)Enum.Parse(typeof(CompassPoint), "South"));
    }   
~~~




