# F# #


- [Wikipedia](https://en.wikipedia.org/wiki/F_Sharp_(programming_language)


# 構文

- [Verbose Syntax](http://msdn.microsoft.com/ja-jp/library/dd233199.aspx)
- Lightweight Syntax

# インポート宣言(open)
- C# でいったら using
- [open](http://msdn.microsoft.com/en-us/library/dd393787.aspx)([JP](http://msdn.microsoft.com/ja-jp/library/dd393787.aspx))

~~~
> open System;;
> Console.WriteLine("Hello, F#\n");;
Hello, F#

val it : unit = ()
~~~


# 束縛(let)

"let expression"により識別子を値(Value)もしくは関数(Function)に関連づけします:

> A binding associates an identifier with a value or function. 

> You use the let keyword to bind a name to a value or function.


~~~
> let add = 3;;

val add : int = 3
~~~

~~~
> let add i j = i + j;;

val add : i:int -> j:int -> int
~~~

## 型推論

- [Type Inference](http://msdn.microsoft.com/en-us/library/dd233180.aspx)([JP](http://msdn.microsoft.com/ja-jp/library/dd233180.aspx)) : Type Annotation(型アノテーション)しなくても型が推論される（時がある)
 
 
## 式本体

body-expression::

> The body-expression is the expression in which the names are used. 
> 
> The body expression appears on its own line, 
> 
> indented to line up exactly with the first character in the let keyword:


~~~
val result : int = 14

> let result = 
-     let i, j, k = (1, 2, 3)
-     i + 2 * j + 3 * k;;

val result : int = 14

~~~

~~~
> let i, j, k = (1, 2, 3) 
- i + 2 * j + 3 * k ;;

val k : int = 3
val j : int = 2
val i : int = 1
val it : int = 14
~~~

~~~
> let result =
-     let function3 (a, b) = a + b
-     100 * function3 (1, 2);;

val result : int = 300

~~~

## 型の注釈
Type Annotations::

> You can specify types for parameters by including a colon (:) followed by a type name, all enclosed in parentheses. 


~~~
> let a : int = 3;;

val a : int = 3
~~~

~~~
> let add (i: int) (j: int):int = i + j;;

val add : i:int -> j:int -> int

> add 3 4;;
val it : int = 7

~~~
 
# Values

- [Value](http://msdn.microsoft.com/en-us/library/dd233185.aspx)

## Null Values

> The null value is not normally used in F# for values or variables

- [Null Value](http://msdn.microsoft.com/en-us/library/dd233197.aspx)
- C#とか他の.NETコードとの互換の為にあるだけ

> If a type is defined in some other .NET language, null is a possible value, and when you are interoperating with such types, 

> your F# code might encounter null values.

# Types

- [F# Types](http://msdn.microsoft.com/en-us/library/dd233230.aspx)


- [Primitive Types](http://) (bool, byte, sbyte,.....)