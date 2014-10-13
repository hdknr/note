Swift: 俺の謎リスト

- 始めたばっかりでよくわからない
- 随時更新

# 型の名前がわからない

- Tupleの型は？

~~~
  1> _stdlib_getDemangledTypeName(1)
$R0: String = "Swift.Int"
~~~

~~~
  2> _stdlib_getDemangledTypeName((1,1))
$R1: String = ""

  3> var tuple = (1,1)
tuple: (Int, Int) = {
  0 = 1
  1 = 1
}
  4> _stdlib_getDemangledTypeName(tuple)
$R2: String = ""
~~~

# Tupleの比較

- swich/case でtuple判定できる

~~~
  9> var i = (1, 2)
i: (Int, Int) = {
  0 = 1
  1 = 2
}
 10> switch i { 
 11. case (1, 2): println("Yes") 
 12. default : println("No") 
 13. }    
Yes
~~~

- "==" だと比較できない

~~~

 14> if i == (1, 2) { println("Yes") }
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/34199/repl26.swift:2:6: error: cannot invoke '==' with an argument list of type '(@lvalue (Int, Int), (IntegerLiteralConvertible, IntegerLiteralConvertible))'
if i == (1, 2) { println("Yes") }
   ~~^~~~~~~~~
~~~

- python

~~~
>>> (1,2) == (1,2)
True
~~~

- [オーバーロード関数(?) つくればいいって言う人が](https://stackoverflow.com/questions/24487519/how-to-elegantly-compare-tuples-in-swift)。
- 判定できますが、これでいいのか？

~~~
func == <T:Equatable> (tuple1:(T,T),tuple2:(T,T)) -> Bool
{
   return (tuple1.0 == tuple2.0) && (tuple1.1 == tuple2.1)
}

var i = (1, 2) == (1, 2)

println("\(i)")
~~~

