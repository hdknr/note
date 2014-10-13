Swift vs. C#: Control Flow

# Control Flow

- for , while
- if , switch
- break, continue

# For Loops


## For-In

~~~
  1> for i in 1...5 { print("\(i),") }; println() 
1,2,3,4,5,
~~~

~~~
csharp> foreach(var i in Enumerable.Range(1,5)){ Console.Write(string.Format("{0},",i));} ; Console.WriteLine();
1,2,3,4,5,
csharp>  
~~~

~~~
  5> for (k, v) in ["spider": 8, "ant": 6, "cat": 4]{ print("\(k)=\(v),") }; println() 
spider=8,cat=4,ant=6,
~~~

~~~
csharp> foreach(var i in new Dictionary<string,int>{{"spider", 8}, {"ant", 6},{ "cat", 4}}) 
      > { Console.Write(string.Format("{0}={1},",i.Key, i.Value));}                         
spider=8,ant=6,cat=4,
~~~

~~~
  7> for i in "Hello" {print("\(i)-")}; println() 
H-e-l-l-o-
~~~

~~~
csharp> foreach(var i in "Hello"){ Console.Write(string.Format("{0}-",i)); } ;Console.WriteLine();
H-e-l-l-o-
~~~ 


## For

~~~
  8> for var i = 0; i < 3; ++i { print("\(i),")};println();
0,1,2,
~~~

~~~
csharp> for(int i=0; i<3;i++){Console.Write(string.Format("{0}-",i)); } ;Console.WriteLine();
0-1-2-
~~~

# While Loops

~~~
  1> var i=0; while i < 3 { print("\(i)-"); i++; } ; println();
0-1-2-
i: Int = 3
~~~

~~~
csharp> int i=0; while(i < 3) {Console.Write(string.Format("{0}-",i)); i++; }; Console.WriteLine();
0-1-2-
~~~

~~~
  1> var i=0; while i < 3 { print("\(i)-"); i++; } ; println();
0-1-2-
i: Int = 3
~~~

~~~
csharp> int i=0; do {Console.Write(string.Format("{0}-",i)); i++; } while (i<3);Console.WriteLine();
0-1-2-
~~~

# Conditional Statements


## If

- 省略

## Switch

~~~
  2> var c = 'e'
  3> switch c { 
  4. case "a", "e", "i", "o", "u": println("\(c) is vowel")
  5. case "b", "c", "d", "f", "g", "h", "j", "k", "l", "m","n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z": println("\(c) is consonant")
  6. default: println("others") 
  7. } 
e is vowel
~~~

~~~
csharp> var c = 'e'; 
csharp> switch(c){                                                                                       
      > case  'a': case  'e': case  'i': case  'o': case  'u': Console.WriteLine(string.Format("{0} is vovel", c));break;  
      > default: Console.WriteLine("Other");break;                                                       
      > }
e is vovel
~~~

## No Implicit Fallthrough

- Swift : 条件のフォールスルーしない。1つのケースだけ実行。 

~~~
 24> switch c { 
 25. case "e": 
 26. case "E": 
 27.     println("Eeeeeee") 
 28. default: 
 29.     println("Other") 
 30. }    
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/24397/repl16.swift:3:1: error: 'case' label in a 'switch' should have at least one executable statement
case "e":
^~~~~~~~~
~~~

- case内でbreakすると、switchのブロックから抜ける。

~~~
 16> switch c { 
 17. case "e": 
 18.      println("Hi!")
 19.      if true{ break;} 
 20.      println("not here") 
 21. default: 
 22.      println("other") 
 23. } 
 24.
  
Hi!
~~~

- C# : breakしないといけません(コンパイルエラー)

~~~
csharp> switch(c){
      >   case 'e': case 'E': Console.WriteLine("Eeeeee"); break;
      >   default: Console.WriteLine("Other");break;
      > }
Eeeeee
~~~

## Range Matching


~~~
 24> var i=0;
i: Int = 0

 25> switch i { 
 26. case 0...9: println("less than 10") 
 27. default: println("other") 
 28. }    
less than 10
~~~

- C# : 出来ないので、　1) if else で判定式で判定 2) switch前に判定結果を出して結果で case 分岐させる

## Tuples

- Swift : Tupleをラベルにできる。 "_"(アンダースコア)をワイルドカード扱いできる

~~~
 29> var i = (0, 0)
i: (Int, Int) = {
  0 = 0
  1 = 0
}
 30> switch i { 
 31. case (_, 0): println("Y is the base") 
 32. default : println("others") 
 33. }    
Y is the base
~~~

- Swift : 順番関係ある

~~~
 34> switch i { 
 35. case (_, 0): println("Y is the base") 
 36. case(0,0): println("Point is the origin")
 37. default : println("others") 
 38. } 
 39. 

Y is the base

 39> switch i { 
 40. case(0,0): println("Point is the origin") 
 41. case (_, 0): println("Y is the base")  
 42. default : println("others")  
 43. }    

Point is the origin
~~~

- C# : Tupleをラベルに使うの無理でしょう

~~~
csharp> var i = Tuple.Create(0,0)
csharp> var j = Tuple.Create(0,0)
csharp> i == j
false
~~~

- Swift: rangeのタプルつかえるっぽい

~~~
  2> switch (3, 5) { 
  3. case (0...9, 0...9): println("Here!!!") 
  4. default:println("Other") 
  5. } 
  6. 
  
Here!!!
~~~

## Value Bindings

> A switch case can bind the value or values it matches to temporary constants or variables, for use in the body of the case. This is known as value binding, because the values are “bound” to temporary constants or variables within the case’s body.


- let(var) で評価に渡された値をブロック内で受け取れる

~~~
 12> switch (2, 0) {
 13. case (let x, 0): println("X軸 上 \(x)") 
 14. case (0, let y) :println("Y軸 上 \(y)") 
 15. case let (x, y): println("軸以外の以以外 \(x), \(y)") 
 16. } 
X軸 上 2
 17> switch (0, 3) {
 18. case (let x, 0): println("X軸 上 \(x)") 
 19. case (0, let y) :println("Y軸 上 \(y)") 
 20. case let (x, y): println("軸以外の以以外 \(x), \(y)") 
 21. } 
 22. 
Y軸 上 3
 22>  
 23> switch (2, 3) { 
 24. case (let x, 0): println("X軸 上 \(x)") 
 25. case (0, let y) :println("Y軸 上 \(y)") 
 26. case let (x, y): println("軸以外の以以外 \(x), \(y)") 
 27. } 
 28. 
軸以外の以以外 2, 3)
~~~

# Control Transfer Statements

Swifth

- continue
- break
- fallthrough 
- return

C# だと [Jump Statement](http://msdn.microsoft.com/en-us/library/d96yfwee.aspx)

- break
- continue
- goto
- return
- throw

## Continue

~~~
 16> for i in "great minds think alike" { 
 17.     switch i { 
 18.     case "a", "e", "i", "o", "u" : continue 
 19.     default: print("\(i)") 
 20.     } 
 21. }; println() 
grt mnds thnk lkgrt mnds thnk lk
~~~

- C# 似たようなものなので省略


## Break

### Break in a Loop Statement

- Swift : 実行されているforループ自体を終了
- C# : 同じ

~~~
 30> for i in 1...3 { 
 31.     for c in "apple" { 
 32.         if c == "l" { continue } 
 33.         print("\(i) \(c),")
 34.     } 
 35. }; println()
1 a,1 p,1 p,1 e,2 a,2 p,2 p,2 e,3 a,3 p,3 p,3 e,
~~~

### Break in a Switch Statement

- Swift : 実行されている switchブロックを終了
- C# : 同じ。 caseにステートメントがあれば breakで終わらないとコンパイルエラー

~~~
csharp> switch(i){                       
      > case 1: Console.Write("Here!");
      > case 2: Console.Write("There!"); break;
      > default: Console.Write("Other");break;
      > }
(2,1): error CS0163: Control cannot fall through from one case label `case 1:' to another
(3,1): warning CS0162: Unreachable code detected
~~~


## Fallthrough

- Swift : case のラベルをフォールスルーできる

~~~
 36> switch 1 { 
 37. case 0...5: print("Here!") ; fallthrough 
 38. case 6...9: print("There!") 
 39. default : print("other")
 40. }; println()

Here!There!
~~~

- C#: goto をつかえば出来てしまう(> <)

~~~
csharp> var i=1;

csharp> switch(i){                                        
      > case 1: Console.Write("Here!");goto case 2;break; 
      > case 2: Console.Write("There!"); break;           
      > default: Console.Write("Other");break;            
      > }; Console.WriteLine();
(2,44): warning CS0162: Unreachable code detected
Here!There!
~~~


## Labeled Statements

- Swifth : break, continue を指定したブロックに対して実行できる

~~~
var i=0
LOOP: while i < 10 {
   switch i {
      case 3:
        println("\(i) is a magic number")
        i += 2 
        continue LOOP
      case 8:
        println("\(i) is the end.")
        break LOOP
      default:
        println("\(i) ....")
   } 
   i += 1
}
~~~

~~~
$ ./test.swift 

0 ....
1 ....
2 ....
3 is a magic number
5 ....
6 ....
7 ....
8 is the end.
~~~

- C#: goto とか例外とかを使う
- goto:csharp インタプリタを通すと、Endラベルが先に存在しないとシンボルエラーなので

~~~
var gate=true;

LOOP:; for (int i = 0; i < 10 && gate ; i++) {
    for (int j = 0; j < 10; j++) {
        if (i + j > 10){
             gate=false;
             goto LOOP;
        }
        Console.WriteLine (
        string.Format ("{0} {1}", i, j));
    }
}
~~~









                                                  
                                         

