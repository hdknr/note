Swift vs. C# : Functions

# Functions    

##Defining and Calling Functions


~~~
func echo(msg: String) -> String {
   return ">>> " + msg
}

for i in ["Hi", "Ora"] {
  println("\(echo(i))")
}

>>> Hi
>>> Ora
~~~

~~~
public class Sample {
    public static string echo(string msg){
            return ">>> " + msg;
    }
}

foreach(var i in new string[]{"Hi", "Ora"}){
  Console.WriteLine(Sample.echo(i));
}

>>> Hi
>>> Ora
~~~

# Function Parameters and Return Values


## Multiple Input Parameters

- カンマで並べろ、という普通の話

~~~
func Diff(start: Int, end: Int) -> Int {
    return end - start
}
println(Diff(3, 10))

7
~~~


## Functions Without Parameters

- () でいいよ、という普通の話

## Functions Without Return Values

- Swift

~~~
func Greeting(){
   println("Hello")
}
~~~

~~~
  1> func Greeting()->String{ return "Hello" }
  2> Greeting()
$R0: String = "Hello"

  1> func Greeting(){ println("Hello") }
  2> Greeting()
Hello
~~~

- C#

~~~
public class Sample {
    public static void Greeting(){
        Console.WriteLine("Hello");
    }
}

Sample.Greeting()
~~~

## Functions with Multiple Return Values

> You can use a tuple type as the return type for a function to return multiple values as part of one compound return value.

~~~
  3> func Double(i:Int, j:Int)->(x:Int, y:Int){ return (i*2, j*2)}
  4> Duble(3,4)
  
$R0: (x: Int, y: Int) = {
  x = 6
  y = 8
}
~~~

これはtupleなのか？(のようですが、tupleの比較が。。。。)

~~~
  7> Double(1,2) == (2, 4)
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/34199/repl14.swift:2:12: error: cannot invoke '==' with an argument list of type '((x: Int, y: Int), (IntegerLiteralConvertible, IntegerLiteralConvertible))'
Duble(1,2) == (2, 4)
~~~

ウーム...

~~~
  1> var i = (1, 1)
i: (Int, Int) = {
  0 = 1
  1 = 1
}
  2> var i:(x:Int, y:Int) = (1,1)
i: (x: Int, y: Int) = {
  x = 1
  y = 1
}
~~~

C# でも Tuple返せますが、私は嬉しさ良くわからないです。

~~~
public class Sample {
    public static Tuple<int,int> Double(int i, int j){ 
        return Tuple.Create(i * 2, j * 2); 
    }   
}


Console.WriteLine( Sample.Double(1,1));
~~~
~~~
(2,2)
~~~

C#はtupleの比較問題ない

~~~
System.Diagnostics.Debug.Assert(
  Sample.Double(1,1) == Tuple.Create(2,2)
);
~~~

## Optional Tuple Return Types

要するに nil を返したければ "?" を付けろとのこと

~~~
  7> func Inc(i: Int) -> Int { if i % 2 == 0 { return nil } else { return i*2}}
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/34683/repl5.swift:2:50: error: type 'Int' does not conform to protocol 'NilLiteralConvertible'
func Inc(i: Int) -> Int { if i % 2 == 0 { return nil } else { return i*2}}
                                                 ^

  7> func Inc(i: Int) -> Int? { if i % 2 == 0 { return nil } else { return i*2}} 
  
  8> Inc(2)
$R0: Int? = nil
  9> Inc(1)
$R1: Int? = 2
~~~

~~~
 11> func Double(i:Int, j:Int)->(x:Int, y:Int)? { if i%2 == 0 {return nil} else { return (i*2, j*2)}}  
 12. 
 12> Double(1,1)
$R2: (x: Int, y: Int)? = (x = 2, y = 2)
 13> Double(2,1)
$R3: (x: Int, y: Int)? = nil
~~~

C#だとTupleはオブジェクトなのでnull返せる

~~~
public class Sample {
    public static Tuple<int,int> Double(int i, int j){ 
        if ( i % 2 == 0 ) return null;
        return Tuple.Create(i * 2, j * 2); 
    }   
}


Console.WriteLine( Sample.Double(1,1));
System.Diagnostics.Debug.Assert(
  Sample.Double(2,1) == null);
~~~

ただし、intは値なのでnull返せない

~~~
    public static int Inc(int i ){
        return ( i % 2 == 0 ) ? null : i * 2;
    }
~~~
~~~
(8,33): error CS0173: Type of conditional expression cannot be determined because there is no implicit conversion between `null' and `int'
~~~

Nullable int

~~~
int? i = null;
System.Diagnostics.Debug.Assert(i == null);
~~~

return int? するにはnullをキャストする！

~~~
   public static int? Inc(int i ){
        return ( i % 2 == 0 ) ? (int?)null : i * 2;
    }
~~~

あるいは

~~~
    public static int? Inc(int i ){
        return ( i % 2 == 0 ) ? new System.Nullable<int>(): i * 2;
    }
~~~

null で比較できる

~~~
System.Diagnostics.Debug.Assert(
    Sample.Double(2,1) == null);
~~~

System.Nullable

~~~
csharp> var i = new System.Nullable<int>();
csharp> i == null
true
csharp> i.GetType()
System.NullReferenceException: Object reference not set to an instance of an object
  at <InteractiveExpressionClass>.Host (System.Object& $retval) [0x00000] in <filename unknown>:0 
  at Mono.CSharp.Evaluator.Evaluate (System.String input, System.Object& result, System.Boolean& result_set) [0x00000] in <filename unknown>:0 
  at Mono.CSharpShell.Evaluate (System.String input) [0x00000] in <filename unknown>:0 
~~~
    
    
# Function Parameter Names


## External Parameter Names

Swift : 外部名で修飾(?)する

~~~
 14> func Inc(yours mine:Int) -> Int { return mine * 2 }

 15> Inc(2)
$R4: Int? = nil

 16> Inc(yours:2)
$R5: Int = 4
~~~    

C#: 普通に引数名が使える

~~~
    public static int? Inc(int i ){
        return ( i % 2 == 0 ) ? new System.Nullable<int>(): i * 2;
    }
~~~

~~~
Console.WriteLine( Sample.Inc(i:3));
6
~~~

## Shorthand External Parameter Names

頭に"#"をつければ外部名修飾いらない (> <)

~~~
 17> func Inc(#mine:Int) -> Int { return mine * 2 } 
 18> Inc(mine:3)
$R6: Int = 6
~~~

## Default Parameter Values

Swift

~~~
  2> func join(a: String, b: String, sep: String=" ") -> String { return "\(a)\(sep)\(b)" } 
  3> join("Good", "Morning") 
$R0: String = "Good Morning"
  4> join("Good", "Morning", "-")
$R1: String = "Good-Morning"
~~~

C#

~~~
    public static string Join(string a, string b , string sep=" " ){
        return string.Format("{0}{1}{2}", a, sep, b );
    }
~~~
~~~
Console.WriteLine(Sample.Join("Good", "Morning") );
Good Morning
~~~


## External Names for Parameters with Default Values


Swift: デフォルト値がある引数は外部名を使える

~~~
  5> func join(a: String, b: String, sep: String=" ") -> String { return "\(a)\(sep)\(b)" } 
  6> join("Good", "Night", sep: "-----")
  
$R2: String = "Good-----Night"
~~~

デフォルト変数は順番変えられる:

~~~
  8> func join(a: String, b: String, sep: String=" ", end:String="!") -> String { return "\(a)\(sep)\(b)\(end)" } 

  9> join("Give up", "the Funk", end:"!!!!", sep:",")
$R4: String = "Give up,the Funk!!!!"
~~~

C# : もちろん。順もかえられるよ。

~~~
Console.WriteLine(Sample.Join(sep:"@", b:"ms.com", a:"billg"));

billg@ms.com
~~~

## Variadic Parameters

Swift: 可変長引数

~~~
 19> func total(vals: Int...)->Int {  
 20.     var ret=0 
 21.     for i in vals {  
 22.         ret += i  
 23.     } 
 24.     return ret  
 25. } 
 
 26> total(1,2,3,4,5)

$R6: Int = 15
~~~

C#  

~~~
    public static int Total(params int[] vals ){
        return vals.Sum();         // using System.Linq   
    }
~~~

~~~
Console.WriteLine( Sample.Total(1,2,3,4,5) );

15
~~~

- 必ず最後のパラメータであること (Swift/C#)
- デフォルト値があるパラメータよりも最後(Swift/C#)

## Constant and Variable Parameters

Swift : 引数は let 

~~~
  5> func echo(msg: String) -> String 
  6. { 
  7.     msg = msg + " " + msg 
  8.     return msg 
  9. } 
 10. 
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/38118/repl5.swift:4:9: error: cannot assign to 'let' value 'msg'
    msg = msg + " " + msg
    ~~~ ^

~~~

varで定義

~~~
  5> func echo(var msg: String) -> String 
  6. { 
  7.     msg = msg + " " + msg 
  8.     return msg 
  9. }
   
 10> echo("Hi")
$R0: (String) = "Hi Hi"
~~~

C#: 引数は"var"

~~~
    public static string Echo(string msg){
        msg = msg + " " + msg;
        return msg;
    }
~~~

~~~
Console.WriteLine( Sample.Echo("Hi") );

Hi Hi
~~~

## In-Out Parameters


Swift: inout / "&"

~~~
 11> func side_effect(inout msg: String) -> String { 
 12.     msg = msg + " " + msg
 13.     return msg 
 14. } 
 15. 
~~~
~~~  
 15> var x = "Hi"
x: String = "Hi"
 16> side_effect(x)
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/38118/repl15.swift:2:13: error: passing value of type 'String' to an inout parameter requires explicit '&'
side_effect(x)
            ^
            &
~~~
~~~
 16> side_effect(&x)
$R1: String = "Hi Hi"
 17> x
$R2: String = "Hi Hi"
~~~
    
    
C# : ref / ref

~~~
    public static string SideEffect(ref string msg){
        msg = msg + " " + msg;
        return msg;
    }
~~~

~~~
var x = "Hi";
Console.WriteLine( Sample.SideEffect(ref x) );
Console.WriteLine( x );

Hi Hi
Hi Hi
~~~

~~~
C# : out / out

    public static string SideEffect(string msg, out int len){
       msg = msg + " " + msg;
       len = msg.Length;
       return msg; 
    }
~~~

~~~
int len;
Console.WriteLine( Sample.SideEffect("Hi", out len));
Console.WriteLine( len );

Hi Hi
5
~~~

# Function Types


## Using Function Types

Swift : (Int, Int) -> Int が関数の型

~~~
 22> func sum(i: Int, j: Int) -> Int { return i+j } 
~~~
~~~
 20> var x: (Int,Int) -> Int = sum
x: (Int, Int) -> Int = ($__lldb_expr24`__lldb_expr_23.sum (Swift.Int, Swift.Int) -> Swift.Int at repl.swift:19)

 21> x(1,2)
$R3: Int = 3
~~~

C# : delegate

~~~
public class Sample 
{
   public delegate int Sum( int x, int y );

   public int RightSum(int x ,int y ){
        return x + y;
   }
   public int WrongSum(int x ,int y ){
        return x + y + 1;
   }
}

Sample.Sum s1 = (new Sample()).RightSum;
Sample.Sum s2 = (new Sample()).WrongSum;
Console.WriteLine(s1(3,4));
Console.WriteLine(s2(3,4));

7
8
~~~


C#: Action 返り値がvoidのdelegate 

~~~
public class Sample1
{
  public void Run() { Console.WriteLine("Aciton1"); }
}
public class Sample2
{
  public void Run() { Console.WriteLine("Aciton2"); }
}

Action a1 = (new Sample1()).Run;
Action a2 = (new Sample2()).Run;

a1();
a2();

Aciton1
Aciton2
~~~

C# : Func 引数と返り値を定義できるデリゲート

~~~
Func<int,int,int> Sum =(int i, int j) => { return i + j ; }

var x = Sum;

Console.WriteLine( x(4,4) );

8
~~~

C# : Predicate  返り値がbooleanのデリゲート

~~~
public class PredicateSample
{
  public bool CanDrink(int age){
    return age >= 20;  
  }
}

Predicate<int>  a = (new PredicateSample()).CanDrink;
Console.WriteLine( a(19) );

False
~~~

## Function Types as Parameter Types

Swift

~~~
 26> func calc(mf: (Int, Int) -> Int, i:Int, j:Int) -> Int { 
 27.     return mf(i,j) 
 28. }    
 29>  
 30> calc(sum, 3, 4)
$R4: Int = 7
~~~

C#

~~~
public class DelegateSample
{
  public int Sum(int i, int j){
    return i + j;
  }
  public int Calc(Func<int,int,int> mf, int i, int j)
  {
     return mf(i,j);
  }
}
~~~
~~~
var sample = new DelegateSample();
Console.WriteLine(
    sample.Calc(sample.Sum, 3, 4 ) );

7
~~~

## Function Types as Return Types


Swift

~~~
  1> func sum(i: Int, j:Int) -> Int { return i + j }
  2> func Procedure() -> (Int, Int)->Int { 
  3.     return sum 
  4. }    
~~~
~~~  
  5> Procedure()(3, 4)
$R0: Int = 7
~~~

C#

~~~
public class DelegateSample
{
  public int Sum(int i, int j){
    return i + j;
  }
  public Func<int,int,int> Procedure() 
  {
     return this.Sum;
  }
}  
~~~

~~~  
    Console.WriteLine(
      (new DelegateSample()).Procedure()(3, 8) 
    );
    
    11
~~~

# Nested Functions


Swift:

~~~
  1> func calc(i: Int, j:Int) -> (Int, Int)->Int {  
  2.     func sum(i: Int, j:Int) -> Int { return i + j }  
  3.     func sub(i: Int, j:Int) -> Int { return i - j }  
  4.     return i > j ? sub : sum 
  5. }    
~~~

~~~
  8> calc(8, 5)(11, 7)
$R1: Int = 4
~~~

C#: 

~~~
public class DelegateSample
{
  public Func<int,int,int> InnerProcedure(int x, int y)
  {
    return (x > y)
        ? new Func<int,int,int>((i,j)=>{ return j - i ; })
        : new Func<int,int,int>((i,j)=>{ return j + i ; }) ;
  }
 }  
~~~
~~~
    Console.WriteLine(
      (new DelegateSample()).InnerProcedure(3, 4)(11, 7)
    );
    
    18
~~~  
