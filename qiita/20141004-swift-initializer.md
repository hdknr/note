Swift vs. C# : Initialization

> Initialization is the process of preparing an instance of a class, structure, or enumeration for use. 

- Swift : イニシャライザ , C# : [コンストラクタ](http://msdn.microsoft.com/ja-jp/library/ace5hbzh.aspx)

> Unlike Objective-C initializers, Swift initializers do not return a value. 

- C#も同じ

# Setting Initial Values for Stored Properties

> Classes and structures must set all of their stored properties to an appropriate initial value by the time an instance of that class or structure is created.

Stored Propertyはイニシャライザかデフォルト値で必ず設定されないといけない。

## Initializers

Swift:

~~~
struct Point { 
   var X: Int
   init(){ X = 100 }
}
~~~

C#: コンストラクタ

## Default Property Values

Swift:

~~~
  1> struct Point {  
  2.    var X: Int = 100 
  3. }
  4> var p : Point
  
p: Point = {
  X = 0
}

  5> var p = Point()
p: Point = {
  X = 100
}
~~~

C#: structはコンストラクタ用意する必要があるので、デフォルト値は意味ない

~~~
public struct Point {
   public int X = 100;
   public Point(int x ){
      X = x;
   }
}

Point p;
Console.WriteLine(p.X);

var p2  = new Point(200);
Console.WriteLine(p2.X);

0
200
~~~

~~~
public class Point {
   public int X = 100;
}

var p  = new Point();
Console.WriteLine(p.X);

100
~~~

# Customizing Initialization


## Initialization Parameters

Swift:

~~~
struct Point { 
   var X: Int
   init(x: Int){ X = x}
}

println( Point(x:90).X )
90
~~~

~~~
struct Point { 
   var X: Int
   init(X x: Int){ X = x}
}

println( Point(X:90).X )
90
~~~

C#: 外部名も使える

~~~
public struct Point {
   public int X = 100;
   public int Y = 100;
   public Point(int x, int y ){
      X = x; Y = y;
   }
}

var p = new Point(y:9, x:8);
_.Print("X={0} Y={1}", p.X, p.Y);

X=8 Y=9
~~~

## Local and External Parameter Names

~~~
struct Point { 
   var X: Int
   init(X: Int){ self.X = X}
}

println( Point(X:90).X )
90
~~~

Swift: 通常、外部名必要

~~~
struct Point { 
   var X: Int
   init(X x: Int){ X = x}
}

println( Point(90).X )

./swift3.swift:8:16: error: missing argument label 'X:' in call
println( Point(90).X )
               ^
               X: 
~~~


## Initializer Parameters Without External Names


Swift: アンダースコアで外部名不要

~~~
struct Point { 
   var X: Int
   init(_ x: Int){ X = x}
}

println( Point(90).X )

90
~~~

## Optional Property Types

Swift: イニシャライザ終わる迄に初期化必須

~~~
struct Point { 
   var X: Int
   var Y: Int
   init(_ x: Int){ X = x}
}

./swift3.swift:6:25: error: variable 'self.Y' used before being initialized
   init(_ x: Int){ X = x}
                        ^
~~~


- nil可能にすればよい

~~~
struct Point { 
   var X: Int
   var Y: Int?
   init(_ x: Int){ X = x}
}
~~~


~~~
 7> class Point {  
  8.    var X: Int 
  9.    var Y: Int 
 10.    init(_ x: Int){ } 
 11. }
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/21901/repl7.swift:5:20: error: property 'self.X' not initialized
   init(_ x: Int){ }
~~~

C#: structは同じく

~~~
public struct Point {
   public int X = 100;
   public int Y = 100;
   public Point(int x, int y ){}
}

(4,31): error CS0171: Field `Point.X' must be fully assigned before control leaves the constructor
(4,31): error CS0171: Field `Point.Y' must be fully assigned before control leaves the constructor

~~~

C#: class は問題ない(default(T)で初期化される)

~~~
public class Point {
   public int X ;
   public int Y ;
   public Point(){}
}

var p = new Point();
_.Print("X ={0}, Y={1}", p.X, p.Y );
~~~


## Modifying Constant Properties During Initialization

Swift: initではletに設定できる

~~~
struct Position{
    let origin: Int
    init(o: Int){
        origin = o
    } 
}
var p =  Position(o:100)
println(p.origin)
~~~



- デフォルト値で設定済でもinit()なら出来る

~~~
struct Position{
    let origin: Int = 100
    init(o: Int){
        origin = o
    } 
}
~~~

その後だめ

~~~
./swift3.swift:11:10: error: cannot assign to 'origin' in 'p'
p.origin = 200
~~~~~~~~ ^
~~~

C#: readonly はコンストラクタ内部で変更

~~~
public class Point {
   public readonly int Origin = 100;
   public int X ;
   public int Y ;
   public Point(){
        Origin = 200;
   }
}

var p = new Point();
_.Print("X ={0}, Y={1} Origin={2}", p.X, p.Y, p.Origin );

p.Origin = 300;

X =0, Y=0 Origin=200

(1,4): error CS0191: A readonly field `Point.Origin' cannot be assigned to (except in a constructor or a variable initializer)

~~~


# Default Initializers

Swift: Classのデフォルトイニシャライザー

~~~
  1> class Size{ 
  2.     var width = 100 
  3.     var height = 100 
  4.     var depth: Int? 
  5. }
  6> var s = Size()
s: Size = {
  width = 100
  height = 100
  depth = nil
}
~~~

- structだめじゃない？

~~~
  6> struct Size{
  7.     var width = 100 
  8.     var height = 100 
  9.     var depth: Int? 
 10. } 
 11. 
 11> var s = Size()
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/13139/repl5.swift:2:13: error: missing argument for parameter 'width' in call
var s = Size()
            ^
~~~

- initializerが呼ばれなければよい。が、イニシャライズされない。

~~~
 11> var s : Size
s: Size = {
  width = 0
  height = 0
  depth = 0
}
~~~
 
C#: structはコンストラクタ必須。クラスは T() がデフォルトで指定しなくても呼ぶ事ができる。


## Memberwise Initializers for Structure Types


~~~
 12> var s = Size(width:10, height:10, depth:10) 
s: Size = {
  width = 10
  height = 10
  depth = 10
}
~~~


# Initializer Delegation for Value Types

Swift:

> nitializers can call other initializers to perform part of an instance’s initialization. 

> This process, known as initializer delegation, avoids duplicating code across multiple initializers.


~~~
  2. struct Point {  
  3.    var X: Int 
  4.    var Y: Int? 
  5.    init(x: Int, y: Int) { X=x ; Y=y } 
  6.    init(pos: (Int, Int)) { self.init(x:pos.0, y:pos.1) } 
  7. } 
  8> var p = Point(pos: (10,10))
p: Point = {
  X = 10
  Y = 10
}
~~~

- 引数タイプではなく引数名(外部名)でメソッドシグネチャが識別

~~~
  9> struct Point {  
 10.    var X: Int  
 11.    var Y: Int? 
 12.    init(x: Int, y: Int) { X=x ; Y=y } 
 13.    init(dx: Int, dy: Int) { X=2*dx ; Y=2*dy } 
 14.    init(pos: (Int, Int)) { self.init(x:pos.0, y:pos.1) } 
 15.    init(dpos: (Int, Int)) { self.init(dx:dpos.0, dy:dpos.1) } 
 16. }
 17> var p1 = Point(pos: (1,1))
p1: Point = {
  X = 1
  Y = 1
}
 18> var p2 = Point(dpos: (1,1))
p2: Point = {
  X = 2
  Y = 2
}
~~~

- なので明示的に指定した外部名が異なればよい。以下もOK

~~~
    init(dx x: Int, dy y: Int) { X=2*x ; Y=2*y } 
~~~

- これはいけるが

~~~
 30> struct PointEx{  
 31.     var X = 0 , Y = 0 
 32.     init(_ x: Int, y: Int){ X=x ; Y=y} 
 33.     init(_ pos: (Int, Int)){ self.init(pos.0, y:pos.1)} 
 34. } 
~~~

- これはだめ

~~~
 36> struct PointEx{  
 37.     var X = 0 , Y = 0 
 38.     init(_ x: Int, _ y: Int){ X=x ; Y=y} 
 39.     init(_ pos: (Int, Int)){ self.init(pos.0, pos.1)} 
 40. }
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/15503/repl23.swift:5:35: error: could not find an overload for 'init' that accepts the supplied arguments
    init(_ pos: (Int, Int)){ self.init(pos.0, pos.1)}
                             ~~~~~^~~~~~~~~~~~~~~~~~
~~~


C#: this(arglist) で呼べる

~~~
public class Point {
   public int X ;
   public int Y ;
   public Point():this(9,9){
   }
   public Point(int x , int y)
   {
        X=x ; Y =y;
   }
}

var p = new Point();
_.Print("X ={0}, Y={1}", p.X, p.Y );

X =9, Y=9
~~~


# Class Inheritance and Initialization

Swift:

> All of a class’s stored properties—including any properties the class inherits from its superclass—must be assigned an initial value during initialization.

~~~
  1> class Point{ 
  2.    var x : Int 
  3.    var y : Int 
  4.    init() { x = 10 ; y = 10 } 
  5. } 
  
  6> class PointEx : Point{}                                                                                                              
  
  7> var p = PointEx()

p: PointEx = {
  __lldb_expr_1.Point = {
    x = 10
    y = 10
  }
}
~~~

Swift:

- designated initializers 
- convenience initializers


C#:

~~~
public class Point {
   public int X ;
   public int Y ;
   public Point():this(9,9){
   }
   public Point(int x , int y)
   {
        X=x ; Y =y;
   }
}

public class PointEx: Point{}
var p = new PointEx();
_.Print("X ={0}, Y={1}", p.X, p.Y );

X =9, Y=9

~~~

## Designated Initializers and Convenience Initializers

Swift:

クラス継承したときにイニシャライザのチェーンが発生するので、その時のチェーンの仕方の話

Designated Initializers:

-  primary initializers


Convenience initializers:

- secondary initializers
- supporting initializers     
    
 
C#: Swiftみたいにめんどくさくないと思う
   

## Syntax for Designated and Convenience Initializers


~~~
  3> class Point{ 
  4.    var x : Int 
  5.    var y : Int 
  6.    init() { x = 10 ; y = 10 } 
  7.    init(_ i: Int, _ j : Int) { x = i ; y = j }  
  8.    convenience init(pos: (Int, Int)) { self.init(pos.0, pos.1) } 
  9. }

 11> var p = Point()
p: Point = {
  x = 10
  y = 10
}
 12> var p = Point(5,5)
p: Point = {
  x = 5
  y = 5
}
 13> var p = Point(pos: (3,3))
p: Point = {
  x = 3
  y = 3
}
~~~

- delegate initizalizer呼ばないといけない

~~~
  1> class Point{ 
  2.    var x : Int 
  3.    var y : Int 
  4.    init() { x = 10 ; y = 10 } 
  5.    init(_ i: Int, _ j : Int) { x = i ; y = j }  
  6.    convenience init(pos: (Int, Int))  
  7.    { x = pos.0 ; y = pos.1 } 
  8. }
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/16604/repl1.swift:7:16: error: convenience initializer for 'Point' must delegate (with 'self.init')
   convenience init(pos: (Int, Int)) 
               ^
~~~

- delegate initializerを呼ぶのであれば convenience宣言しないといけない

~~~
  1> class Point{ 
  2.     var x = 0 , y = 0 
  3.     init(i: Int, j:Int) {  
  4.         println("init Point") 
  5.         x = i; y = j 
  6.     } 
  7.     init(pos: (Int, Int)){ 
  8.         println("init Point by pos") 
  9.         self.init(i: pos.0, j: pos.1 ) 
 10.     } 
 11. }
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/18195/repl1.swift:8:5: error: designated initializer for 'Point' cannot delegate (with 'self.init'); did you mean this to be a convenience initializer?
    init(pos: (Int, Int)){
    ^
    convenience 
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/18195/repl1.swift:10:14: note: delegation occurs here
        self.init(i: pos.0, j: pos.1 )

~~~


### Initializer Chaining

Swiftルール

Rule1:

- サブクラスのdesignated initializerは直上スーパークラスのdesignated initializerを呼ばないといけない

Rule 2:

- convenience initializer はクラス内の別のイニシャライザーを呼ばないといけない

Rule 3:

- convenience initializer最終的にはクラスのdesignated initializerのどれかを呼ばないといけない

#### 簡単なチェーン

![image](https://developer.apple.com/library/prerelease/mac/documentation/Swift/Conceptual/Swift_Programming_Language/Art/initializerDelegation01_2x.png)

#### 複雑なチェーン

![image](https://developer.apple.com/library/prerelease/mac/documentation/Swift/Conceptual/Swift_Programming_Language/Art/initializerDelegation02_2x.png)


### Two-Phase Initialization

Swift : Two-Phase で初期化します

Phase 1:

- あるクラスのイニシャライザが呼ばれる(designated か convenience)
- メモリが割り当てられる。まだ初期化されない
- designated initializeが処理が終わる迄にstored propertiesに値が割り当てられる。メモリが初期化される。
- designated initializerスーパークラスのイニシャライザに処理を引き継ぐ。スパークラスでうへの処理を行う。
- これを最後のスーパークラスまでさかのぼって繰り返す。
- ここですべてのstored propertiesが初期化されてPhase1終了

Phase 2

- おおもとのサブクラスから、各designated initializerがインスタンスへのカスタマイズ処理を行う。
- ここで、selfにアクセス可能な状態になっていて、propertiesを変更したり、instance methodをコールできたりする。とか。
- 最後にチェーンの中にあるconvenience initializersがインスタンスへのカスタマイズ処理が行えるようになる。

## Initializer Inheritance and Overriding

Swift: 明示的に overrideしないといけない

~~~
  1> class Point{ 
  2.     var x = 0 , y = 0 
  3.     init() {  
  4.         println("init Point") 
  5.         x = 10; y = 10  
  6.     } 
  7. } 
  8.  
  9. class PointEx: Point{ 
 10.     init() {  
 11.         println("init PointEx") 
 12.         x = 20; y = 20 
 13.     } 
 14. }
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/17373/repl1.swift:11:5: error: overriding declaration requires an 'override' keyword
    init() { 
    ^
    override 
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/17373/repl1.swift:4:5: note: overridden declaration is here
    init() { 
    ^
~~~

Swift: 親のプロパティは親が面倒みる

~~~
  1> class Point{ 
  2.     var x = 0 , y = 0 
  3.     init() {  
  4.         println("init Point") 
  5.         x = 10; y = 10  
  6.     } 
  7. } 
  8.  
  9. class PointEx: Point{ 
 10.     override init() {                                                                                                                 
 11.         println("init PointEx") 
 12.         x = 20; y = 20 
 13.     } 
 14. }
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/17373/repl2.swift:13:9: error: use of property 'x' in base object before super.init initializes it
        x = 20; y = 20
        ^
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/17373/repl2.swift:13:17: error: use of property 'y' in base object before super.init initializes it
        x = 20; y = 20
                ^
~~~

Swift: super呼べば良い

~~~
  1> class Point{ 
  2.     var x = 0 , y = 0 
  3.     init() { println("*") } 
  4.     init(i: Int, j:Int) {  
  5.         println("init Point") 
  6.         x = i; y = j 
  7.     } 
  8.     init(pos: (Int, Int)){ 
  9.         println("init Point by pos") 
 10.         x = pos.0; y = pos.1 
 11.     } 
 12. } 

 14. class PointEx: Point{ 
 15.     override init() { 
 16.         println("*") 
 17.         super.init() 
 18.     } 
 19.     override init(i: Int, j:Int) { 
 20.         println("init PointEx") 
 21.         super.init(i:i, j:j) 
 22.     } 
 23. }

 25> var p = PointEx(i: 3, j:3 )
init PointEx
init Point
p: PointEx = {
  __lldb_expr_1.Point = {
    x = 3
    y = 3
  }
}
~~~  

クラスメソッド違って、イニシャライザは自動的にサブクラスには引き継がれない(C#はデフォルトコンストラクタ以外引き継がない)

~~~
 26> var p2 = PointEx(pos: (3,3 ))
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/17948/repl10.swift:2:17: error: extra argument 'pos' in call
var p2 = PointEx(pos: (3,3 ))
                ^     ~~~~~~
                
 26> var p2 = Point(pos: (3,3))
init Point by pos
p2: Point = {
  x = 3
  y = 3
}
~~~
                
## Automatic Initializer Inheritance

条件があえば自動的に引きがれるイニシャライザもある。(めんどくさい)

Rule 1:

- サブクラスにdesignated initializersない。　この場合すべてのdesignated initializersを引き継ぐ

Rule 2:

- Rule1をみたしているか、あるいはカスタム実装を用意していれば、 すべてのconvenience initializersを引き継ぐ


NOTE:

- サブクラスはスーパクラスのdesignated initializer を、自身の中でconvenience initializerとして実装できる。(Rule2)



## Required Initializers

Swift : required 修飾すると、サブクラスでは必須

~~~
  1> class Point { 
  2.     var x = 0 , y = 0 
  3.     required init(i: Int, j:Int) {  
  4.         x = i ; y = j 
  5.     } 
  6. } 
  7.  
  8. class PointEx: Point { 
  9.     init(pos: (Int, Int)){ 
 10.         super.init(i: pos.0, j: pos.1 ) 
 11.     } 
 12. }
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/18772/repl1.swift:13:1: error: 'required' initializer 'init(i:j:)' must be provided by subclass of 'Point'
}
^
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/18772/repl1.swift:4:14: note: 'required' initializer is declared in superclass here
    required init(i: Int, j:Int) { 
             ^
~~~


しかし Rule1があるので、以下はOK

~~~
  1> class Point { 
  2.     var x = 0 , y = 0 
  3.     required init(i: Int, j:Int) {  
  4.         x = i ; y = j 
  5.     } 
  6. } 
  7. class PointEx: Point {}    
  8> var p = PointEx(i: 5, j: 5)
p: PointEx = {
  __lldb_expr_1.Point = {
    x = 5
    y = 5
  }
}
~~~

required隔世遺伝しない

~~~
  1> class Point { 
  2.     var x = 0 , y = 0 
  3.     required init(i: Int, j:Int) {  
  4.         x = i ; y = j 
  5.     } 
  6. } 
  
  7. class PointEx: Point {} 

  9. class PointExEx: PointEx{ 
 10.     init(pos: (Int, Int)){ 
 11.         super.init(i: pos.0, j: pos.1 ) 
 12.     }  
 13. }
    
 14> var p = PointExEx(pos: (9,9))
p: PointExEx = {
  __lldb_expr_1.PointEx = {
    __lldb_expr_1.Point = {
      x = 140735556008464
      y = 0
    }
  }
}
 15> p.x
$R0: Int = 9
~~~


# Setting a Default Property Value with a Closure or Function


- stored propetiesの設定のカスタマイズをしたかったら、クロージャかグローバル関数使えとのこと

- クロージャ

~~~
 1> import Foundation
  2>        
  3. func getDayOfWeek(today: NSDate = NSDate.date()) -> Int { 
  4.     let cal = NSCalendar(calendarIdentifier: NSGregorianCalendar) 
  5.     let calcomp = cal.components( .WeekdayCalendarUnit, fromDate: today) 
  7.     let weekDay = calcomp.weekday 
  8.     return weekDay 
  9. }

 17> class ToDo { 
 18.   var day_of_week: String  = { 
 19.     return ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"][getDayOfWeek()-1]
 20.   }(); 
 21. } 

 22> var t = ToDo()
t: ToDo = {
  day_of_week = "Sat"
}
~~~

- Type Method

~~~
 23> class ToDo { 
 24.   class func get_day_of_week(today :  NSDate = NSDate.date()) -> String {
 25.         var w = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"] 
 26.         var i = getDayOfWeek(today:today)-1 
 27.         return w[i] 
 28.   } 
 29.   var day_of_week = ToDo.get_day_of_week() 
 30. }  
 31. 
 31> var t = ToDo()
t: ToDo = {
  day_of_week = "Sat"
}
~~~


# C# 

- C#: [プライベートコンストラクタ](http://msdn.microsoft.com/ja-jp/library/kcfb85a6.aspx)
- C#: [静的コンストラクタ](http://msdn.microsoft.com/ja-jp/library/k9x6w0hc.aspx)

## ベースクラスのコンストラクタ

- ベースクラスのコンストラクタは base(argslist)すればよい
- ベースクラスのコンストラクタがよばれたあとで、自分のコンスクタのブロックが処理される

~~~
public class Point {
   public int X ;
   public int Y ;
   public Point():this(9,9){ } 

   public Point(int x , int y)
   {
        X=x ; Y =y;
   }
}

public class PointEx: Point
{
   public PointEx(int x, int y): base(x*2, y*2)
   {
       _.Print("X ={0}, Y={1}", this.X, this.Y );
        
      this.X += 3 ; this.Y += 3;    
   }
}

var p2 = new PointEx(5,5);
_.Print("X ={0}, Y={1}", p2.X, p2.Y );

X =10, Y=10
X =13, Y=13
~~~

## デフォルトコンストラクタ以外は引き継がれない


~~~
public class Point {
   public int X ;
   public int Y ;
   public Point():this(9,9){ } 

   public Point(int x , int y)
   {
        X=x ; Y =y;
   }
}

public class PointEx: Point
{
}

var p2 = new PointEx(5,5);

(1,11): error CS1729: The type `PointEx' does not contain a constructor that takes `2' arguments

~~~
