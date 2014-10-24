F#: 型推論

# Type Inference : 型推論

## Type Annotation(型アノテーション)しなくても型が推論される（時がある)

~~~
> 1.0 / 2.0;;
val it : float = 0.5
> 4 / 2;;
val it : int = 2
> "a" + "b" ;;
val it : string = "ab"
~~~

~~~
> "a" + 2;;

  "a" + 2;;
  ------^

/Users/hide/Dropbox/アプリ/scriptogram/fsharp/stdin(4,7): error FS0001: The type 'int' does not match the type 'string'
~~~


~~~
> let add x y = x + y;;

val add : x:int -> y:int -> int

> add 3 4;;
val it : int = 7

> add 3.0 4.0;;

  add 3.0 4.0;;
  ----^^^

/Users/hide/Dropbox/アプリ/scriptogram/fsharp/stdin(12,5): error FS0001: This expression was expected to have type
    int    
but here has type
    float  
~~~

~~~
> let add (x : float) (y : float) = x + y;;

val add : x:float -> y:float -> float

> add 3.0 4.0;;
val it : float = 7.0

> add 3 4;;

  add 3 4;;
  ----^

/Users/hide/Dropbox/アプリ/scriptogram/fsharp/stdin(21,5): error FS0001: This expression was expected to have type
    float    
but here has type
    int    

~~~

