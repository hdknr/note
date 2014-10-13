Swift vs. C# : Closures

- [ref](https://developer.apple.com/library/prerelease/mac/documentation/Swift/Conceptual/Swift_Programming_Language/Closures.html#//apple_ref/doc/uid/TP40014097-CH11-XID_152)

# Closures

Swift:

> Closures are self-contained blocks of functionality that can be passed around and used in your code. 

> Closures in Swift are similar to blocks in C and Objective-C and to lambdas in other programming languages.

> Global and nested functions, as introduced in Functions, are actually special cases of closures.

3種類:


>        Global functions are closures that have a name and do not capture any values.

>        Nested functions are closures that have a name and can capture values from their enclosing function.

>        Closure expressions are unnamed closures written in a lightweight syntax that can capture values from their surrounding context.


C#:

- [What are 'closures' in .NET?](https://stackoverflow.com/questions/428617/what-are-closures-in-net)

2種類:

 - [anonymous methods](http://msdn.microsoft.com/ja-jp/library/0yw3tz5k.aspx)
- [lambda](http://msdn.microsoft.com/ja-jp/library/bb397687.aspx) 

# Closure Expressions


## The Sorted Function

Swiftのsortedの例:

~~~
10> let names = ["Chris", "Alex", "Ewa", "Barry", "Daniella"]
names: [String] = 5 values {
  [0] = "Chris"
  [1] = "Alex"
  [2] = "Ewa"
  [3] = "Barry"
  [4] = "Daniella"
}

 11> func backwards(s1: String, s2: String) -> Bool { return s1 > s2 }

 12> sorted(names, backwards) 
$R2: [String] = 5 values {
  [0] = "Ewa"
  [1] = "Daniella"
  [2] = "Chris"
  [3] = "Barry"
  [4] = "Alex"
}
~~~

## Closure Expression Syntax

Swiftの クロージャ:

~~~
 13> {(s1: String, S2: String) -> Bool in  return s1 > s2 }
$R3: (String, String) -> Bool = ($__lldb_expr18`__lldb_expr_17.(closure #1) at repl.swift:13)

~~~

~~~
 14> sorted(names,{(s1:String, s2:String)->Bool in return s1 > s2})
 
$R4: [String] = 5 values {
  [0] = "Ewa"
  [1] = "Daniella"
  [2] = "Chris"
  [3] = "Barry"
  [4] = "Alex"
}

~~~

C#:

~~~
csharp> Func<string, string, int> lambda = (i,j) => -1 * i.CompareTo(j);

csharp> lambda.GetType()

System.Func`3[System.String,System.String,System.Int32]
~~~

~~~
    var names = new string[]{"Chris", "Alex", "Ewa", "Barry", "Daniella"};
    
    foreach(var i in names ){ Console.Write(i);Console.Write(",");};Console.WriteLine();

Chris,Alex,Ewa,Barry,Daniella,
~~~

~~~    
    Array.Sort(names, (o1, o2 ) => -1 * o1.CompareTo(o2) ); 
    
    foreach(var i in names ){ Console.Write(i);Console.Write(",");};Console.WriteLine();

Ewa,Daniella,Chris,Barry,Alex,
~~~


## Inferring Type From Context

Swift: 型の推論

~~~
 15> sorted(names, { s1, s2 in return s1 > s2 } )
$R5: [String] = 5 values {
  [0] = "Ewa"
  [1] = "Daniella"
  [2] = "Chris"
  [3] = "Barry"
  [4] = "Alex"
}
~~~

C#: 同じく

~~~
Array.Sort(names, (o1, o2 ) => -1 * o1.CompareTo(o2) ); 
~~~

## Implicit Returns from Single-Expression Closures


Swift: 単一文だとreturnもいらない

~~~
 16> sorted(names, { s1, s2 in s1 > s2 } )
$R6: [String] = 5 values {
  [0] = "Ewa"
  [1] = "Daniella"
  [2] = "Chris"
  [3] = "Barry"
  [4] = "Alex"
}
~~~

C#: 同じ


## Shorthand Argument Names

Swift: "$引数の番号" で、引数リストも省略

~~~
 17> sorted(names, { $0 > $1 } )
$R7: [String] = 5 values {
  [0] = "Ewa"
  [1] = "Daniella"
  [2] = "Chris"
  [3] = "Barry"
  [4] = "Alex"
}
~~~

C#: これは無いと思う

## Operator Functions


Swift: Stringに ">" 演算子があって、引数２個とることまでわかっているので...

~~~
 18> sorted(names, >)
$R8: [String] = 5 values {
  [0] = "Ewa"
  [1] = "Daniella"
  [2] = "Chris"
  [3] = "Barry"
  [4] = "Alex"
}
~~~


# Trailing Closures

- 引数の最後にクロージャを取るならば、クロージャを関数呼び出しの外側における...

> A trailing closure is a closure expression that is written outside of (and after) the parentheses of the function call it supports

Swift:

~~~
 19> sorted(names) { $0 > $1 }
$R9: [String] = 5 values {
  [0] = "Ewa"
  [1] = "Daniella"
  [2] = "Chris"
  [3] = "Barry"
  [4] = "Alex"
}
~~~

~~~
 31> func my(i: Int, j: Int, closure: (Int, Int)->Int )->Int{ 
 32.     return 2 * closure(i,j) 
 33. } 
~~~

~~~    
 35> my(3,5){ $0 * $1 }
$R12: Int = 30
~~~

C# : ないと思う

# Capturing Values

> A closure can capture constants and variables from the surrounding context in which it is defined. 

 
~~~
 31> func my(i: Int, j: Int, closure: (Int, Int)->Int )->Int{ 
 32.     return 2 * closure(i,j) 
 33. } 
~~~
~~~
 36> var a=1
a: Int = 1

 37> my(3,5){ $0 * $1 + a }
$R13: Int = 32
~~~

> The closure can then refer to and modify the values of those constants and variables from within its body, 

~~~
 42> var b = 0
b: Int = 0
 43> my(3,5){ b = $0 * $1; return b + a} 
$R18: Int = 32
 44> b
$R19: Int = 15
~~~


> even if the original scope that defined the constants and variables no longer exists.

~~~
 53> func getinc(amount: Int)-> ()->Int { 
 54.     var grand_total=0 
 55.     func inc() -> Int { 
 56.         grand_total += amount 
 57.         return grand_total 
 58.     } 
 59.     return inc
 60. } 
~~~

~~~
 62> var x=getinc(10) 
 
x: () -> Int = ($__lldb_expr77`partial apply forwarder for __lldb_expr_76.(getinc (Swift.Int) -> () -> Swift.Int).(inc #1) (())Swift.Int at repl76.swift)

 68> x();x();x();x()
$R23: Int = 40

~~~

~~~
69> var y = getinc(1)

y: () -> Int = ($__lldb_expr77`partial apply forwarder for __lldb_expr_76.(getinc (Swift.Int) -> () -> Swift.Int).(inc #1) (())Swift.Int at repl76.swift)

 70> y();y();y();y()

$R24: Int = 4
~~~

C#: Func を返す Func を作成して呼び出すラッパーを用意。外側のFuncの定義にコンテキストを持たせる。

~~~
    public static Func<int> GetInc(int unit)
    {
        return (new Func<Func<int>>(() => { 
            int x = 0;  
            return new Func<int>(() => { x += unit; return x; }); 
        }))();
    }
~~~

~~~
     var x = GetInc(10);
     var y = GetInc(1);
     var i = 0;
     var j = 0;
     for( int k=0 ; k< 4; k++ ){
        i = x(); j=y(); 
     }   
     Console.WriteLine(string.Format("{0},{1}", i,j));
~~~
~~~
40,4
~~~
		

# Closures Are Reference Types


Swift: 参照型ということ

~~~
 72> var z = x
z: () -> Int = ($__lldb_expr77`partial apply forwarder for __lldb_expr_76.(getinc (Swift.Int) -> () -> Swift.Int).(inc #1) (())Swift.Int at repl76.swift)
 73> z()
$R26: Int = 60
~~~

C# : 同じく

~~~
var z = x;
Console.WriteLine(z()); 

50
~~~
