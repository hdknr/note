C#: Lambda

#  C#: delegate

[MS](http://msdn.microsoft.com/ja-jp/library/ms173171.aspx)

> デリゲートは、特定のパラメーター リストおよび戻り値の型を使用して、メソッドへの参照を表す型です。 

> デリゲートは、他のメソッドへの引数としてメソッドを渡すために使用されます。 

~~~
public class Calc 
{
    public delegate int Sum(int x, int y);

    public static int Do(int x, int y, Sum func)
    { return func(x, y); }

}
~~~

- [デリゲート分散](http://msdn.microsoft.com/ja-jp/library/ms173174.aspx)


# C# 1.0 : Named Methods

[MS](http://msdn.microsoft.com/en-us/library/98dc08ac.aspx)

~~~

public class Cs1 {

    // C# 1.0 Named Method
    public static int DoSome(int x, int y)
    {
        return x + y;
    }

    public static void Run()
    {
        Console.WriteLine( 
            Calc.Do(3, 4, DoSome) );
    }
}
~~~

# C# 2.0 : Anonymous Methods 

[MS](http://msdn.microsoft.com/ja-jp/library/0yw3tz5k.aspx)


> 匿名メソッドを使用すると、別のメソッドを作成する必要がないため、デリゲートをインスタンス化する際のコーディングのオーバーヘッドを削減できます。

~~~
public class Cs2 
{
    public static void Run()
    {
        // C# 2.0 Anonymous Method
        Console.WriteLine( 
            Calc.Do(3, 4, 
                delegate(int x, int y){ return x + y ; }
            ) );
    }
}
~~~


> 匿名メソッドは、外部スコープの ref パラメーターや out パラメーターにアクセスできません。
> 匿名メソッド ブロック内のアンセーフ コードにはアクセスできません。

> 匿名メソッドは、is 演算子の左辺では使用できません。

~~~
(6,60): error CS0837: The `is' operator cannot be applied to a lambda expression, anonymous method, or method group
~~~

# C# 3.0 : Lambda Expression

[MS](http://msdn.microsoft.com/ja-jp/library/bb397687.aspx)


Syntax:

~~~
(input parameters) => expression
~~~

~~~
(input parameters) => {statement; statement;....; return result;}
~~~

~~~
public class Cs3{

    public static void Run()
    {
        // C# 3.0 Lambda
        var funcs = new List<Calc.Sum>{
            { (x, y) => x + y },
            { (x, y) => x - y },
            { (x, y) => x * y },
            { (x, y) => x / y },
            { (x, y) => {var z = 2 * x +  2 * y ; return z; }},
        }; 
        
        int i = 12;
        int j =  4;
        foreach(var f in funcs ){
            Console.WriteLine(
                string.Format("{0}, {1} => {2}",
                    i, j, Calc.Do(i,j, f)));
        }
    }
}
~~~


