Swift vs. C#: Methods

> Classes, structures, and enumerations  can all define instance methods

- C# : enum にインスタンスメソッド定義できないと思います。

>  Classes, structures, and enumerations can also define type methods, which are associated with the type itself. 

- C# : enum にクラスメソッド定義できないと思います。


# Instance Methods


~~~
  1> class Counter { var i = 0; func inc(x:Int=1) { i += x } } 
~~~

~~~
  2> var c = Counter() 
c: Counter = {
  i = 0
}
  3> c.inc() ; c.inc(x:3);
  4> c.i
$R0: Int = 4
~~~

## Local and External Parameter Names for Methods


Swift: 2つめ以降の引数は外部名を指定してコール。まじで。。。。 (#入らない)

~~~
  1> class Counter { var i = 0; 
         func inc(x:Int, times:Int) 
            { i += x * times } 
     }
  2> var c = Counter()
c: Counter = {
  i = 0
}

  3> c.inc(1, 3)
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/88924/repl9.swift:2:6: error: missing argument label 'times:' in call
c.inc(1, 3)
     ^
         times: 


  3> c.inc(1, times:3)
  4> c.i
$R0: Int = 3

~~~



C#: いつでも外部名指定できる

~~~
public class Counter{
  public int Count = 0;
  public void Inc(int x, int times ){
     Count += x * times;
  } 
}

var c = new Counter();
c.Inc(x:3, times:4);
c.Inc(times:3, x:4);
c.Inc(2, 5);
c.Inc(2, times:3);
~~~

## Modifying External Parameter Name Behavior for Methods


Swift: 外部名指定できる

~~~
  1> class Counter { var i = 0; 
          func inc(x:Int, times xx:Int) 
          { i += x * xx } }
          
  2> var c = Counter()
c: Counter = {
  i = 0
}
  3> c.inc(2,times:4)
  4> c.i
$R0: Int = 8
~~~

- "_" 修飾すると２番目も外部名入らない

~~~
  7> class Counter { 
          var i = 0; 
          func inc(x:Int, _ xx:Int) 
          { i += x * xx } } 
          
  8> var c = Counter()
c: Counter = {
  i = 0
}
  9> c.inc(5,5 )
 10> c.i
$R1: Int = 25
~~~



## The self Property


Swift : self

C# : this


## Modifying Value Types from Within Instance Methods


> Structures and enumerations are value types. 

> By default, the properties of a value type cannot be modified from within its instance methods.

~~~
 11> struct Point { 
 12.     var x=0 , y = 0 
 13.     func move(dx: Int, _ dy: Int){ 
 14.         x += dx; y += dy; 
 15.     } 
 16. }    
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/89045/repl27.swift:5:11: error: cannot invoke '+=' with an argument list of type '(Int, Int)'
        x += dx; y += dy;
        ~~^~~~~
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/89045/repl27.swift:5:20: error: cannot invoke '+=' with an argument list of type '(Int, Int)'
        x += dx; y += dy;
                 ~~^~~~~
~~~

Swift: mutating 

~~~
 11> struct Point { 
 12.     var x=0 , y = 0 
 13.     mutating func move(dx: Int, _ dy: Int){ 
 14.         x += dx; y += dy; 
 15.     } 
 16. } 
 17> var p = Point()
p: Point = {
  x = 0
  y = 0
}
 18> p.move(1,1)

 20> p
$R3: Point = {
  x = 1
  y = 1
}
~~~

C#: デフォルト mutating

~~~
public struct Point{
    public int X;
    public int Y;
    public void Move(int dx, int dy ) { 
       X += dx ; Y += dy; 
    }   
    public Point(int x , int y){ 
       X = x ; Y = y;
    }   
}

Point p;
p.Move(10, 10);
~~~

## Assigning to self Within a Mutating Method

Swift: self入れ替え

~~~
  1> struct Point { 
  2.     var x = 0, y = 0 
  3.     mutating func grow(nx: Int, _ ny: Int) { 
  4.         self = Point(x:nx * 2 , y: ny * 2) 
  5.     } 
  6. }
  7> var p :Point
p: Point = {
  x = 0
  y = 0
}
~~~

~~~
 10> enum Turn { 
 11.     case  Alice, Bob, Cindy 
 12.      
 13.     mutating func next() { 
 14.         switch self { 
 15.         case Alice: self = Bob 
 16.         case Bob: self = Cindy 
 17.         case Cindy: self = Alice 
 18.         } 
 19.     } 
 20. }
 21> var t :Turn
t: Turn = Alice
 22> t.next()
 23> t
$R1: Turn = Bob
 24>  
~~~

C#: 

~~~
public struct Point{
    public int X;
    public int Y;

    public void Assign(Point p )
    {
        this = p;
    }
}

Point p1 = new Point(10,10);
Point p2 = new Point(100,100);
p1.Assign(p2)
Console.WriteLine(p1.X);
Console.WriteLine(p1.Y);

100
100
~~~

### classは self変更できないよ
参照がただからそうでしょう

Swift:

~~~
  8>   class Point {  
  9.       var x = 0, y = 0  
 10.       mutating func grow(nx: Int, ny: Int) {  
 11.             self = Point(x:nx * 2 , y: ny * 2)  
 12.       }  
 13.   } 
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/2880/repl9.swift:4:7: error: 'mutating' isn't valid on methods in classes or class-bound protocols
      mutating func grow(nx: Int, ny: Int) { 
      ^~~~~~~~
      
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/2880/repl9.swift:5:18: error: cannot assign to 'self' in a method
            self = Point(x:nx * 2 , y: ny * 2) 
            ~~~~ ^
~~~

C#: 同じく
            
~~~
public class Point{
    public int X;
    public int Y;

    public void Assign(Point p)
    {
        this = p;
    }
}

Point p1 = new Point(10,10);
Point p2 = new Point(100,100);
p1.Assign(p2):q

(12,9): error CS1604: Cannot assign to `this' because it is read-only
~~~

Python:

~~~
>>> class Object(object):
...   def assign(self, obj):
...     self = obj
...   def __init__(self, val):
...     self.val = val
... 
>>> o1 = Object(3)
>>> o2 = Object(300)
>>> o1.assign(o2)
>>> o1.val
3
~~~


# Type Methods


Swift:

~~~
  8> class Point { 
  9.     class func origin() -> (Int, Int){ 
 10.         return (0, 0) 
 11.     } 
 12. } 

 13> Point.origin()
$R0: (Int, Int) = {
  0 = 0
  1 = 0
}
~~~

C#: Static Method

~~~
public struct Point{
    public static Tuple<int,int> Origin(){
        return Tuple.Create(0,0);
    }   
}

var o = Point.Origin();
Console.WriteLine(o);
~~~


Swift: selfはType

~~~
 21> class Object { 
 22.     class func typemethod() {
 23.         println(self) 
 24.     } 
 25.     func instancemethod(){
 26.         println(self) 
 27.     } 
 28. } 

 29> Object.typemethod()
(Metatype)

 30> Object().instancemethod()
__lldb_expr_21.Object
~~~    

C# : this など使えません


## 同じクラス内の別のメソッド

Swift:

~~~
  1> class Object { 
  2.     class func A(){ 
  3.         println("A")
  4.     } 
  5.     class func B(){ 
  6.         print("B->") 
  7.         A() 
  8.     } 
  9. }   
 10> Object.B()
B->A
~~~

C#:

~~~
public struct Object{ 
  public static void A(){
    Console.WriteLine("A");
  }
  public static void B(){
    Console.Write("B->");
    A();
  }
}


Object.B();
B->A
~~~

