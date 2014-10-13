Swift vs. C#: Generics

Swift : [Generics](https://developer.apple.com/library/prerelease/mac/documentation/Swift/Conceptual/Swift_Programming_Language/Generics.html#//apple_ref/doc/uid/TP40014097-CH26-XID_277)

C#: [ジェネリック (C# プログラミング ガイド)](http://msdn.microsoft.com/ja-jp/library/512aeb7t.aspx)

# The Problem That Generics Solve

- 省略

# Generic Functions

~~~
  1> func swapThem<T>(inout a: T, inout b: T) { 
  2.     let t = a ;a = b; b = t  
  3. }
  4> var a = 0, b = 2 
a: Int = 0
b: Int = 2
~~~

~~~
  5> println("\(a) \(b)") 
  6. swapThem(&a, &b) 
  7. println("\(a) \(b)")
0 2
2 0

  8> var i = "Apple", j = "Banana"
  9> println("\(i) \(j)")

Apple Banana
  
 10> swapThem(&i,&j)
 11> println("\(i) \(j)")

Banana Apple

~~~

C#: 

~~~
public class Generic 
{
  public static void Swap<T>(ref T a , ref T b )
  {
     var t = a ;
     a = b ; b = t;
  }
}
~~~

~~~
var x  = 0;
var y  = 3;
Console.WriteLine(string.Format("{0} {1}", x, y ));
Generic.Swap(ref x , ref y );
Console.WriteLine(string.Format("{0} {1}", x, y ));

var  i = "Apple";
var  j = "Banana";
Console.WriteLine(string.Format("{0} {1}", i, j ));
Generic.Swap(ref i , ref j );
Console.WriteLine(string.Format("{0} {1}", i, j ));


0 3
3 0
Apple Banana
Banana Apple
~~~

# Type Parameters

- "T"のこと

Tが使えるのは

- 引数型
- 返り値型
- 型アノテーション(変数の型宣言)

C#: おなじ

# Naming Type Parameters


~~~
  6> func swapThem<TYPE1>(inout a: TYPE1, inout b: TYPE1) { 
  7.     let t = a ;a = b; b = t 
  8. }
~~~

~~~
  1> func print<T1, T2>(a : T1, b : T2 ){ 
  2.    println("\(a) \(b)") 
  3. }
~~~

C#: 同じ



# Generic Types

~~~
struct Stack<T> {
    var items = [T]()
    mutating func push(item: T) {
        items.append(item)
    }
    mutating func pop() -> T {
        return items.removeLast()
    }
}
~~~


C#: [Stack<T> Class](http://msdn.microsoft.com/en-us/library/3278tedw.aspx)


  
# Extending a Generic Type

~~~
extension Stack {
    var topItem: T? {
        return items.isEmpty ? nil : items[items.count - 1]
    }
}
~~~

C#: Exetnsion Method を定義する

~~~
	public static class Extensions 
	{
		public static T topItem<T>(this Stack<T> stack)
		{
			return stack.First ();
		}   
	}
~~~

~~~
var top = mystack.topItem();
~~~	

# Type Constraints


## Type Constraint Syntax


## Type Constraints in Action


~~~
 17> func Employ<T: Person>(person : T) 
 18. { 
 19.    println("\(person.name) is employed.")                                                                                                              
 20. }
~~~

~~~
 21> Employ(Student(name:"Bob"))
Bob is employed.
~~~

Type Method

~~~
 16. class Employee : Person {  
 17.   class func employ<T: Person>(p: T) -> Employee 
 18.   { 
 19.       return Employee(name:p.name)  
 20.   } 
 21. }  
~~~
~~~ 
 22> Employee.employ( Student(name:"Cindy") )
$R0: Employee = {
  __lldb_expr_1.Person = {
    name = "Cindy"
  }
}
~~~

C#: where。 

~~~
public class Company 
{
    public static Employee Employ<T>(T person) where T: Person
    {
        return new Employee(){name = person.name};
    }
}


var e = Company.Employ(new Student(){name="Bob"});
Console.WriteLine(e.GetType() );
~~~

~~~
Employee
~~~




# Associated Types

Associated Type = alias name + Type

> An associated type gives a placeholder name (or alias) to a type that is used as part of the protocol. 


typealias がキーワード

C#: Associated Type的な物はないと思います


## Associated Types in Action


- 要するにGenericの型指定のコンクリートクラスを定義するときに typealias を使えるっぽい

Swift:

~~~
protocol Container {
    typealias ItemType
    mutating func append(item: ItemType)
    var count: Int { get }
    subscript(i: Int) -> ItemType { get }
}

struct IntStack: Container {

    // original IntStack implementation
    var items = [Int]()
    mutating func push(item: Int) {
        items.append(item)
    }
    mutating func pop() -> Int {
        return items.removeLast()
    }

    typealias ItemType = Int
    mutating func append(item: Int) {
        self.push(item)
    }
    var count: Int {
        return items.count
    }
    subscript(i: Int) -> Int {
        return items[i]
    }
}
~~~


C#: Tに型を入れて実装/継承、でいいんじゃないでしょうか。

~~~
public interface IContainer<T> { 
    void append(T item);
    int count { get; }
    T this[int i] { get; }
}

public class IntStack : IContainer<int>
{
    public void append(int item) {}
    public int count { get { return 0; }}
    public int this[int i] { get { return 0; }}
}

~~~


## Extending an Existing Type to Specify an Associated Type

Swift: extensionでジェネリックタイプを注入

~~~
extension Array: Container {}
~~~

C#: Extension メソッドでやるか、継承したサブクラスを定義(ただしクラスは多重継承できない)


# Where Clauses

Swift: 型制約に加えて、 whereを使って、Associated Typeの制約を加えられるようです

~~~
func allItemsMatch<
    C1: Container, C2: Container
    where C1.ItemType == C2.ItemType, C1.ItemType: Equatable>
    (someContainer: C1, anotherContainer: C2) -> Bool {
        
        // check that both containers contain the same number of items
        if someContainer.count != anotherContainer.count {
            return false
        }
        
        // check each pair of items to see if they are equivalent
        for i in 0..<someContainer.count {
            if someContainer[i] != anotherContainer[i] {
                return false
            }
        }
        
        // all items match, so return true
        return true
        
}
~~~

# C# Generis

- [型パラメータ制約](http://msdn.microsoft.com/ja-jp/library/d5x73970.aspx)
- その他...

