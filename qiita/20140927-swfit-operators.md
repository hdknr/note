Swift vs. C#: Basic Operators

# Terms

## Unary Operator

- Unary Prefix Operator

~~~
  9> var ret=true
ret: Bool = true
 10> !ret
$R2: (Bool) = false
~~~

~~~
csharp> var ret=false;
csharp> !ret
true
csharp>  
~~~

- Unary Postfix Operator

~~~
 12> var i=0
i: Int = 0
 13> i++
$R3: Int = 0
 14> i
$R4: Int = 1
~~~

~~~
csharp> var i=0;
csharp> i++;
0
csharp> i
1
~~~

## Binary Operator

~~~
 15> 2 + 3
$R5: Int = 5
~~~

~~~
csharp> 2 + 3;
5
~~~

## Ternary Operator


~~~
 16> ret
$R6: Bool = true
 17> ret ? 1 : 0
$R7: Int = 1
 18> !ret ? 1: 0
$R8: Int = 0
~~~

~~~~
csharp> ret ? 1 : 0;
0
csharp> !ret ? 1 : 0;
1
~~~

# Assignment Operator

- Swift: x = y は値を返さないので例外

~~~
 24> var x = false
x: Bool = false
 25> var y = true
y: Bool = true
 30> if x=y {println("Yes")}
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/5777/repl63.swift:2:5: error: type '()' does not conform to protocol 'BooleanType'
if x=y {println("Yes")}
    ^
 32> if x == y { println("Yes") }
 33> if x != y { println("Yes") } 
Yes
 34> x
$R14: Bool = false
~~~

- C# : x = y は 代入で変化したxの値を返す(C系)

~~~
csharp> var x = false;
csharp> var y = true;
csharp> if(x=y){ Console.WrinteLine("Yes"); }
Yes
csharp> x
true
~~~

# Arithmetic Operators

- +, - , * , / 

~~~
R14: Bool = false
 35> 1 + 2 
$R15: Int = 3
 36> 5 - 3 
$R16: Int = 2
 37> 2 * 3
$R17: Int = 6
 38> 10.0 / 2.5
$R18: Double = 4
~~~

~~~
csharp> 1 + 1
2
csharp> 1 + 2
3
csharp> 5 - 3
2
csharp> 2 * 3
6
csharp> 10.0 / 2.5
4
csharp> var v = 10.0 / 2.5
csharp> v.GetType()
System.Double
~~~

- Swift:キャラクタの連結は文字列

~~~
 40> var i:Character="I"
i: Character = "I"
 41> var j:Character="J"
j: Character = "J"
 42> i+j
$R19: String = "IJ"
~~~

- C#:キャラクタの連結は整数

~~~
csharp> var i='I';
csharp> var j='J';
csharp> i+j
147
csharp> i.GetType()
System.Char
csharp> (i+j).GetType()
System.Int32
~~~

# Remainder Operator

~~~
 44> 9 % 4
$R21: Int = 1
~~~

~~~
csharp> 9 % 4
1
~~~

## Floating-Point Remainder Calculations

~~~
 46> 8 % 2.5
$R23: Double = 0.5
~~~

~~~
csharp> 8 % 2.5
0.5
csharp> (8 % 2.5).GetType()
System.Double
~~~

# Increment and Decrement Operators


~~~
 48> var i = 0
i: Int = 0
 49> ++i
$R24: Int = 1
~~~

~~~
csharp> var i=0;
csharp> ++i
1
~~~

~~~
  1> var a=0, b=a++, c=a++
a: Int = 2
b: Int = 0
c: Int = 1
~~~

~~~
csharp> var a=0;
csharp> var b=a++;
csharp> var c=a++;
csharp> string.Format("{0} {1} {2}", a, b, c);
"2 0 1"
~~~


# Unary Minus/Plus Operator

~~~
  3> var i=3
i: Int = 3
  4> var j = -i
j: (Int) = -3
  5> var k = -j
k: (Int) = 3
  6> var l = +k
l: (Int) = 3
~~~

~~~
csharp> int i=3;
csharp> int j=-i;
csharp> int k=-j;
csharp> int l=+k;
csharp> string.Format("{0} {1} {2} {3}",i,j,k,l)
"3 -3 3 3"
~~~

# Compound Assignment Operators


~~~
  7> var a = 1
a: Int = 1
  8> a += 1
  9> a
$R0: Int = 2
~~~

~~~
csharp> var a = 1;
csharp> a += 1;
csharp> a
2
~~~

- Swift : a += 2 でaの値は増えるが、aの結果は返さない

~~~
 10> a = 2
 11> var b = a += 2
error: could not fetch result -- Couldn't apply expression side effects : Couldn't dematerialize b: corresponding symbol wasn't found

 12> a
$R1: Int = 4
~~~

- C# : a += 2 でaの値は増え、aの結果も返る

~~~
csharp> a = 2
csharp> b = a += 2
csharp> string.Format("{0} {1}", b , a)
"4 4"
~~~

# Comparison Operators


~~~
  6> (1==1, 2 != 1, 2 > 1, 1 < 2, 1 >= 1, 2 <= 1)
$R0: (Bool, Bool, Bool, Bool, Bool, Bool) = {
  0 = true
  1 = true
  2 = true
  3 = true
  4 = true
  5 = false
}
~~~

~~~
csharp> new List<bool>{1==1, 2!=1, 2>1, 1<2, 1>=1, 2<=1};
{ true, true, true, true, true, false }
~~~

# Ternary Conditional Operator

~~~
  9> var hasHeader = true
hasHeader: Bool = true
 10> (hasHeader ? 50 : 20)
$R2: (Int) = 50
~~~

~~~
csharp> var hasHeader = true;
csharp> hasHeader ? 50 : 20;
50
~~~


# Nil Coalescing Operator


~~~
 11> var a:String?
a: String? = nil
 12> var b = a ?? "a is nil"
b: String = "a is nil"
~~~

~~~
csharp> string a = null;
csharp> var b = a ?? "a is null";
csharp> b
"a is null"
~~~

# Range Operators


## Closed Range Operator

- Swift : from...to

~~~
 12> 1...5
$R3: Range<Int> = 1..<6

 13> for i in 1...5 { println("\(i)")}
1
2
3
4
5
~~~

- C# : Range(from, count)

~~~
csharp> Enumerable.Range(1,5)
{ 1, 2, 3, 4, 5 }
csharp> Enumerable.Range(1,5).GetType()
System.Linq.Enumerable+<CreateRangeIterator>c__IteratorD

csharp> foreach(var i in Enumerable.Range(1,5)){ Console.WriteLine(i);}
1
2
3
4
5
~~~


## Half-Open Range Operator


~~~
 16> var names = ["Anna", "Alex", "Brian", "Jack"]
names: [String] = 4 values {
  [0] = "Anna"
  [1] = "Alex"
  [2] = "Brian"
  [3] = "Jack"
}

 17> 0..<names.count
$R5: Range<Int> = 0..<4

 18> for i in 0..<names.count { println("\(names[i])")}
Anna
Alex
Brian
Jack
~~~


~~~
csharp> var names = new List<string>{ "Anna", "Alex", "Brian", "Jack" };                      

csharp> names
{ "Anna", "Alex", "Brian", "Jack" }
csharp> names.GetType()
System.Collections.Generic.List`1[System.String]

csharp> names.Count
4
csharp> Enumerable.Range(0, names.Count)
{ 0, 1, 2, 3 }

csharp> foreach(var i in Enumerable.Range(0, names.Count)){ Console.WriteLine(names[i]);} 
Anna
Alex
Brian
Jack
~~~

# Logical Operators

## Logical NOT Operator

~~~
 19> var a = true
a: Bool = true
 20> !a
$R6: (Bool) = false
~~~

~~~
csharp> var a = true;
csharp> !a
false
~~~

## Logical AND Operator

~~~
 21> var b = false
b: Bool = false
 22> a && b
$R7: Bool = false
 23> a && !b
$R8: Bool = true
~~~

~~~
csharp> var b = false;
csharp> a && b
false
csharp> a && !b
true
~~~

## Logical OR Operator


~~~
 24> a || b
$R9: Bool = true
 25> a || !b
$R10: Bool = true
~~~

~~~
csharp> a || b
true
csharp> a || !b
true
~~~

## Combining Logical Operators

- 同じ

## Explicit Parentheses

- 同じ



