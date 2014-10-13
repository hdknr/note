Swift vs. C# : Deinitialization

> A deinitializer is called immediately before a class instance is deallocated. 

> You write deinitializers with the deinit keyword, similar to how intializers are written with the init keyword. 

> Deinitializers are only available on class types.

# How Deinitialization Works

Swift:

- deinit{}

> You are not allowed to call a deinitializer yourself.

> Superclass deinitializers are inherited by their subclasses

> and the superclass deinitializer is called automatically at the end of a subclass deinitializer implementation

> Superclass deinitializers are always called, even if a subclass does not provide its own deinitializer.

C#:

- [デストラクタ](http://msdn.microsoft.com/ja-jp/library/66x5fx1b.aspx)
- [Object.Finalize()](http://msdn.microsoft.com/ja-jp/library/system.object.finalize.aspx) (デストラクタと同じ)

> Destructor implicitly calls the Finalize method, they are technically same. Dispose is available with those object which implements IDisposable interface.


- [Dispose()](http://msdn.microsoft.com/ja-jp/library/fs2xkftw.aspx)


> The programmer has no control over when the destructor is called because this is determined by the garbage collector. 

- GC対象ではないシステムリソースをホールドしているのであれば、クラスにIDisposeを実装して、解放する機会を得る事ができます。



# Deinitializers in Action

- スクリプトで実行

~~~
class Employee{ 
   var name: String?
   init(){ println("Hello");}
   deinit{ println("Good Bye") }
}

Employee()
~~~

~~~
Hello
Good Bye
~~~

- REPL

~~~
  7> var e : Employee? = Employee() 
Hello
e: Employee? = Some {
  name = nil
}
  8> e = nil
Good Bye
~~~

- ちなみにオプショナル変数は "!" が必要

~~~
 10> e!.name
$R0: String? = nil

 11> e!.name = "Bill Gates"
 
 12> e!.name
$R1: String? = "Bill Gates"

 13> e.name
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/24300/repl24.swift:2:1: error: 'Employee?' does not have a member named 'name'
e.name
^ ~~~~
~~~


C#:

~~~
public class Point {
   public int X ;
   public int Y ;
   public Point():this(9,9){ } 

   public Point(int x , int y)
   {
        X=x ; Y =y;
   }

   ~Point()
   {
        _.Print("destructed X ={0}, Y={1}", X, Y );
   }
}

Point x = new Point();

destructed X =9, Y=9
~~~
