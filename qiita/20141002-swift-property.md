Swift vs. C#: Properties

- Computed Properties & Stored Properties


# Stored Properties

Swift:

- Class & Strucutreに“所有される構成要素”
- variable stored properties(var)
- constant stored properties(let)

C#: 

- Field (const, readonly...)
- Property


## Stored Properties of Constant Structure Instances

Swift:

~~~
  1> struct Point{ var x = 0 ; let y = 0 } 
  2> var p = Point()
p: Point = {
  x = 0
  y = 0
}
  3> p.x = 10
  4> p.y = 10
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/66693/repl7.swift:2:5: error: cannot assign to 'y' in 'p'
p.y = 10
~~~ ^
~~~

C#: そもそも constはインスタンスではなくてクラスのスコープ

- struct はパラメータ初期化のコンストラクタを明示的に宣言する必要がある

~~~
csharp> public struct Point {      
      >   public int x ;           
      >   public const int y=0;
      >   public Point(int x ) { this.x = x ; } // 必須
      > };
csharp> var p = new Point(0);
csharp> p.y
(1,4): error CS0176: Static member `Point.y' cannot be accessed with an instance reference, qualify it with a type name instead
csharp> Point.y
0
csharp> p.x = 10
csharp> p.x
10
~~~

Swift: structインスタンスをletで定数にできる

~~~
  4> let pf = Point()
pf: Point = {
  x = 0
  y = 0
}
  5> pf.x = 10
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/66693/repl11.swift:2:6: error: cannot assign to 'x' in 'pf'
pf.x = 10
~~~~ ^
~~~

C#: structインスタンスをreadonlyで定数にできる

~~~
csharp> public class Container {
      >    public const Point Origin = new Point(0);
      > }
(2,23): error CS0283: The type `Point' cannot be declared const
~~~

~~~
csharp> public class Container {
      >    public readonly Point Origin = new Point(0);
      > }
~~~
~~~
csharp> var c = new Container();
csharp> c.Origin.x = 100;
(1,11): error CS1648: Members of readonly field `Container.Origin' cannot be modified (except in a constructor or a variable initializer)
csharp> var p2 = c.Origin;
csharp> p2.x = 100;
csharp> p2.x
100
~~~

## Lazy Stored Properties


> A lazy stored property is a property whose initial value is not calculated until the first time it is used. 

> You indicate a lazy stored property by writing the lazy modifier before its declaration.


Swift:

~~~
  6> class Container { 
  7.     lazy var position = Point() 
  8. }    
  9> var c = Container()
c: Container = {
  position.storage = nil
}
 10> c.position.x
$R0: Int = 0
 11> c
$R1: Container = {
  position.storage = (x = 0, y = 0)
}
~~~

C#:  Propertyを使う

~~~
public class Point 
{
  public int x;
  public const int y = 0;
}

public class Container {
  public Point _pos=null;
  public Point Position {
    get {
      this._pos = this._pos ?? new Point();
      return this._pos;
    }
  }
}
~~~
~~~
        var c = new Container();
        Assert(c._pos == null );        
        Assert(c.Position.x == 0 );
        Assert(c._pos != null );        
~~~


## Stored Properties and Instance Variables


Objective-Cでの値の持ち方

- プロパティ
- インスタンス変数をバッキングストアとして使う

Swiftはプロパティのみ

よくわかっていません。　Computed Propertiesで get/setすればよいということではないのかな？


# Computed Properties


Swift:

~~~
struct Point { var x = 0.0, y = 0.0 }
struct Size { var width = 0.0, height = 0.0 }

struct Rect {
    var origin = Point()
    var size = Size()
    var center: Point {
        get {
            return Point(
                x: origin.x + (size.width / 2) ,
                y: origin.y + (size.height / 2)
            )
        }
        set(value) {
            origin.x = value.x - (size.width / 2)
            origin.y = value.y - (size.height / 2)
        }
    }
}

var square = Rect(
        origin: Point(x: 0.0, y: 0.0),
        size: Size(width: 10.0, height: 10.0))

let p1 = square.center
square.center = Point(x: 15.0, y: 15.0)

assert(p1.x != square.center.x)
~~~

C#

~~~
public struct Point { 
    public double x = 0.0; public double y = 0.0 ;
    public Point(double x, double y)
    { this.x = x; this.y = y; }
}
public struct Size { 
    public double width  = 0.0f; public double height  = 0.0f ;
    public Size(double w, double h)
    { this.width = w; this.height=h;}
}

public struct Rect
{
    public Point origin;
    public Size  size;

    public Point Center 
    {
        get {
            return new Point(
                origin.x + (size.width / 2) ,
                origin.y + (size.height / 2)
            );
        }
        set{
            origin.x = value.x - (size.width / 2.0);
            origin.y = value.y - (size.height / 2.0);
        }
    }
    public Rect(Point p, Size s )
    {
        this.origin =p ; this.size =s ;
    }
}

var square = new Rect( 
    new Point(0.0f, 0.0f), 
    new Size(10.0f, 10.0f));

var p1 = square.Center;
square.Center = new Point(15.0, 15.0);
Console.WriteLine(p1.x == square.Center.x);

False
~~~

## Shorthand Setter Declaration


Swift: newValue

~~~
        set {
            origin.x = newValue.x - (size.width / 2)
            origin.y = newValue.y - (size.height / 2)
        }
~~~    

C# : value

~~~
        set {
            origin.x = value.x - (size.width / 2)
            origin.y = value.y - (size.height / 2)
        }
~~~      

## Read-Only Computed Properties


Swift:  setがなければ getの修飾も省略できる

~~~
    var readonly_center : Point {
       return center
    }
    
assert(square.center.x == square.readonly_center.x )
    
~~~              

C#: getは省略できない        


# Property Observers



オブザーバー:

- willSet is called just before the value is stored.
- didSet is called immediately after the new value is stored. 


~~~
  1> struct Point { 
  2.     var x: Int = 0 { 
  3.         willSet(val){ println("setting \(val) to x")} 
  4.         didSet{ println("x is now \(x)")}
  5.     } 
  6. }
~~~
~~~
  7> var p = Point(x:0)
p: Point = {
  x = 0
}
  8> p.x = 10
setting 10 to x
x is now 10
~~~    
 
C# : set の中でやる

~~~
    set {
       // do will set
       _x = value;
       // do did set
    } 
~~~

C# 6.0: プロパティに初期値をセットできるので

~~~
    public int X { get;set; } = x;
    public int Y { get;set; } = y;
~~~

# Global and Local Variables


Swift: グローバル変数でもいろいろできる

オブザーバー:

~~~
  1> var x: Int = 0 { didSet{ println("set to \(x)")} }
x: Int = 0
  2> x = 3
set to 3
~~~

get/set: うれしいのだろうか。。。

~~~
  1> var x : Int = 0;
x: Int = 0
  2> var y : Int { get{ return 2*x } set { x = 2*newValue }}
y: Int = <computed property>
  3> y
$R0: Int = 0
  4> x = 1
  5> y
$R1: Int = 2
  6> y = 3
  7> x
$R2: Int = 6
  8> y
$R3: Int = 12
~~~

C#: 変数はどこかクラスにあって static フィールドにも get/set できる

# Type Properties

C#: Static Property


## Type Property Syntax / Querying and Setting Type Properties

Swift : struct, enum <- static, class <- class

~~~
 19> struct Point { 
 20.     var x = 0 
 21.     var y = 0 
 22.     static var shared = 0 
 23.     static let origin = 0 
 24. }    
~~~

~~~
 26> var p1 = Point(x:10, y:10)
p1: Point = {
  x = 10
  y = 10
  shared = 140461199908160
  origin = 140461199915776
~~~

~~~
 28> var p2 = Point(x:100, y:100)
p2: Point = {
  x = 100
  y = 100
  shared = 7365411997647719716
  origin = 3547200665735411558
}
~~~

~~~
 29> Point.shared = 3 
 30> Point.shared
$R1: Int = 3

 31> Point.origin
$R2: Int = 0

 33> Point.origin = 3
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/71998/repl37.swift:2:14: error: cannot assign to the result of this expression
Point.origin = 3
~~~~~~~~~~~~ ^
~~~


- error: class variables not yet supported

~~~
  2> class Point { 
  3.     var x = 0 
  4.     var y = 0 
  5.     class var origin  = (0, 0) 
  6. }    
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/86707/repl8.swift:5:5: error: class variables not yet supported
    class var origin  = (0, 0)
    ^~~~~
~~~

- 別途ストレージを用意(グローバルとか)

~~~
 15> var global_origin = (0, 0)
global_origin: (Int, Int) = {
  0 = 0
  1 = 0
}

 24> class Point { 
 25.     var x = 0 
 26.     var y = 0 
 27.     class var origin :(Int, Int) {  
 28.         get{ return global_origin}  
 29.         set { global_origin = newValue }  
 30.     } 
 31. } 
 
 50> Point.origin = (100, 100) 
 51.  
 51> Point.origin
$R4: (Int, Int) = {
  0 = 100
  1 = 100
}
~~~
 
- structはstatic OK

~~~
  1> struct Point { 
  2.     static var count = 0 
  3.     var x: Int = 0 { 
  4.         didSet { Point.count++ } 
  5.     } 
  6. }  
~~~

~~~
  7> var p1 = Point(x:0)
p1: Point = {
  count = 0
  x = -3458755736018865426
}
  8> var p2 = Point(x:0) 
  9. 
p2: Point = {
  count = 0
  x = 8070459310046764983
}
  9> p1.x = 10
 10> p2.x = 20
 11> Point.count
$R0: Int = 2
~~~
    
- C#

~~~
csharp> public class Point {
      >   public static int Count = 0;
      >   protected int _x = 0;
      >   public int X {
      >     get { return _x; }
      >     set { _x = value; Count++; }
      >  }
      > }
csharp> var p1 = new Point();
csharp> var p2 = new Point();
csharp> p1.X = 10;
csharp> p2.X = 20;
csharp> p2.X == p1.X * 2
true
csharp> Point.Count
2
~~~


