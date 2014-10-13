Swift vs. C#: Subscripts


> Classes, structures, and enumerations can define subscripts, 

> which are shortcuts for accessing the member elements of a collection, list, or sequence.


- C#: [インデクサ](http://msdn.microsoft.com/ja-jp/library/6x16t2tx.aspx)


# Subscript Syntax

Swift:

~~~
 19> struct Point { 
 20.     var i = 0
 21.     subscript(i: Int) -> Int { 
 22.        get { return i * 10 }
 23.     } 
 24. } 
 25>  
 26> var p1 = Point()
p1: Point = {
  i = 0
}
 27> p1[1]
$R0: Int = 10


 28> p1[2]
$R1: Int = 20
~~~

C#:

~~~
public struct Point{ 
  int i = 0;
  public Point(int i){ this.i = i; }
  public int this[int idx] { get { return idx * 10;} }
}

Point p;
Console.WriteLine(p[27]);

270
~~~

# Subscript Usage

- p[3] だけじゃなくて p["Cat"] などもできます (Swift/C#)
- プロパティ同様 get だけじゃなくて setもできます


# Subscript Options

Swift:

~~~
 36> Point()[3, 4]
$R2: Int = 7
 37>  struct Point {  
 38.      var i = 0  
 39.      subscript(x: Int, msg: String) -> String {
 40.          return "\(msg) \(x)"
 41.      }    
 42.  } 
 43. 
 43> Point()[3, "hoge"]
$R3: String = "hoge 3"
~~~

C#:

~~~
public struct Point{ 
  int i = 0;
  public Point(int i){ this.i = i; }
  public string this[int x, string msg] { 
        get { return string.Format("{0} {1}", msg, x);}
  }
}

Point p;
Console.WriteLine(p[3, "hoge"]);

hoge 3
~~~


