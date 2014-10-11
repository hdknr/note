Swift vs C# : Strings and Characters

# String Literals

~~~
 26> var a =  "Swift" + 
 27.          "\nMultiline Literal"
a: String = "Swift\nMultiline Literal"
 28> println(a)
Swift
Multiline Literal
~~~

~~~
csharp> var x = "C#\nLiteral";
csharp> x
"C#
Literal"
csharp> var y = @"C#\nLiteral";
csharp> y
"C#\nLiteral"
csharp> var y = @"C#
      > Literal";
csharp> y
"C#
Literal"
~~~

~~~
csharp> var a = @"  
      > C# 
      > Multiline
      > Literals
      > "
csharp> a
"
C# 
Multiline
Literals
"
~~~


# Initializing an Empty String


~~~
 29> var s=String()
s: String = ""
 30> s.isEmpty
$R11: Bool = true
~~~

~~~
csharp> var s="";
csharp> string.IsNullOrEmpty(s);
true
~~~

# String Mutability

- ここで言っているのは let の変数は変更出来ないよということでしょう
- C# : String は immutable, StringBuilderはmutable
- Objective-C : [NSString](https://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSString_Class/Reference/NSString.html)(immutable), NSMutableString(mutable)
- Swift: StringはNSString APIにバインドされているようだからimmutableなんじゃないんでしょうか。。。

# Strings Are Value Types

Swift:

- ひょっとして、Stringは実はmutableなのか？
- 関数呼び出しの際にも "copy-by-default" する
- "copy-by-default"というのはコピーしないこともある、ということ。オプティマイザがコピーするかしないかを判断する模様


C#:

- [String オブジェクト](http://msdn.microsoft.com/ja-jp/library/system.string.aspx)は、文字列を表す System.Char オブジェクトのシーケンシャル コレクションです。 
- String オブジェクトの値はシーケンシャル コレクションの内容であり、この値は変更できません (つまり、読み取り専用です)。 
- 文字列の不変性に関する詳細については、このトピックの 不変性と Stringbuilder クラス セクションを後で参照します。 
- メモリの String オブジェクトの最大サイズは 2 GB、約 10億文字です。

# Working with Characters


~~~
  7> for i in "Funkadelic" { print("\(i)-") }; println("")
F-u-n-k-a-d-e-l-i-c-
~~~

~~~
csharp> foreach(var i in "Funkadelic"){ Console.Write(String.Format("{0}-",i));}; Console.WriteLine();
F-u-n-k-a-d-e-l-i-c-
~~~

- Swift: StringをArrayに変換しないと...

~~~
  9> Array("Funkadlic")[0]
$R2: Character = "F"
~~~

- C#: もともと Array of System.Char

~~~
csharp> "Funkadelic"[0] 
'F'
~~~

# Concatenating Strings and Characters

~~~
 21> var msg = "Good Morning"
msg: String = "Good Morning"
~~~

- Swift: Character をappendできる(mutable?)

~~~
 25> msg.append(Array("!")[0])
 26> msg
$R7: String = "Good Morning!"
~~~

- UnicodeScalarとCharacterはappendできるけど、"!"だとどっちの型かわからん、ということ (> <)

~~~
 27> msg.append("!")
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/6778/repl63.swift:2:1: error: ambiguous use of 'append'
msg.append("!")
^
Swift.String:3:17: note: found this candidate
  mutating func append(x: UnicodeScalar)
                ^
Swift.String:7:17: note: found this candidate
  mutating func append(c: Character)
                ^
~~~

~~~
 27> UnicodeScalar("!")
$R8: (UnicodeScalar) = U+0x00000021 U'!'
 28> msg.append(UnicodeScalar("!"))
 29> msg
$R9: String = "Good Morning!!"
~~~

- C#: String はimmutableなので、追加というのは別途連結したString作成してそれに参照を変えるという事
- StringBuilderで固定のバッファに処理をできる(mutable)

~~~
csharp> var msg = new StringBuilder(100);
csharp> msg.Append("Good Morning")
Good Morning
csharp> msg.Append("!")
Good Morning!
csharp> msg.ToString()
"Good Morning!"
~~~


# String Interpolation

~~~
 30> var x=0, y=1, z=2
x: Int = 0
y: Int = 1
z: Int = 2
 31> "\(x) + \(y) + \(z) = \(x+y+z)"
$R10: String = "0 + 1 + 2 = 3"
~~~

~~~
 32> func sum(i:Int,j:Int,k:Int)->Int{ return i + j + k }
 33> sum(1,2,3)
$R11: Int = 6
~~~

~~~
 34> "\(x) + \(y) + \(z) = \(sum(x,y,z))"
$R12: String = "0 + 1 + 2 = 3"
~~~

~~~
csharp> Func<int,int,int,int> sum = (i,j,k) => { return i + j + k; }
csharp> sum(0,1,2)
3

csharp> var i=0; var j=1; var k=2;
csharp> String.Format("{0} + {1} + {2} = {3}", i,j,k,sum(i,j,k)); 
"0 + 1 + 2 = 3"
~~~

# Unicode

## Unicode Scalars


~~~
 40> "\u{0061}"
$R15: String = "a"
~~~

~~~
 41> "\u{1F496}" 
$R16: String = "💖"
~~~

~~~
csharp> "\u0061"    
"a"
csharp> '\u0061'
'a'
~~~

~~~
csharp> "\u1f496" 
"Ὁ6"
~~~


~~~
 42> println("\"Apple\"")
"Apple"
~~~

~~~
csharp> Console.WriteLine("\"Apple\"");
"Apple"
csharp> Console.WriteLine(@"""Apple""");
"Apple"
~~~

## Extended Grapheme Clusters

- 拡張書記素クラスタ

> An extended grapheme cluster is a sequence of one or more Unicode scalars that (when combined) produce a single human-readable character.

- Unicode標準附属書29 [UAX #29] ?

- [Unicode::GCString::JA_JP](http://search.cpan.org/~nezumi/Unicode-LineBreak-1.011/lib/Unicode/GCString/JA_JP.pod)

> 書記素クラスタ〔grapheme cluster〕は、Unicode文字の列で、ひとつの書記素基底〔grapheme base〕と、付加的な書記素エキステンダ〔grapheme extender〕および/または「前置」文字〔“prepend” character〕から成る。これは人が「文字」とみなすものに近い。

- [Surrogate Pair](http://vividcode.hatenablog.com/entry/unicode/surrogate-pair)

- [Characters and Grapheme Clusters](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/Strings/Articles/stringsClusters.html)

> In general, these combinations—surrogate pairs, base characters plus combining marks, Hangul jamo, and Indic consonant clusters—are referred to as grapheme clusters. 



# Counting Characters


~~~
 43> countElements("Supergroovalisticprosifunkstication")
$R17: Int = 35
~~~

~~~
csharp> "Supergroovalisticprosifunkstication".Length
35
~~~


# Comparing Strings


## String and Character Equality

- Swift : == , != 

~~~
csharp> var a = "Funky"
csharp> var b = "Funky"
csharp> a == b
true
csharp> a != b
false
csharp> a.CompareTo(b)
0
csharp> string.CompareOrdinal(a,b)
0
csharp> a.SequenceEqual(b)
true
~~~

## Prefix and Suffix Equality


~~~
 44> "Act 2 Scene 2: Capulet's orchard".hasPrefix("Act 2")
$R18: Bool = true

 45> "Act 2 Scene 2: Capulet's orchard".hasSuffix("orchard") 
$R19: Bool = true
~~~

~~~
csharp> "Act 2 Scene 2: Capulet's orchard".StartsWith("Act 2")
true

csharp> "Act 2 Scene 2: Capulet's orchard".EndsWith("orchard") 
true
~~~


# Unicode Representations of Strings


## UTF-8, UTF-16 Representation


~~~
 46> "Supergroovalisticprosifunkstication".utf8
$R20: String.UTF8View = {
  _core = {
    _baseAddress = 0x0000000102876b60
    _countAndFlags = 9223372036854775843
    _owner = nil
  }
}
 47> "Supergroovalisticprosifunkstication".utf16
$R21: String.UTF16View = {
  _offset = 0
  _length = 35
  _core = {
    _baseAddress = 0x0000000102876d60
    _countAndFlags = 9223372036854775843
    _owner = nil
  }
}
~~~

~~~
csharp> System.Text.Encoding.UTF8.GetBytes("Supergroovalisticprosifunkstication")
{ 83, 117, 112, 101, 114, 103, 114, 111, 111, 118, 97, 108, 105, 115, 116, 105, 99, 112, 114, 111, 115, 105, 102, 117, 110, 107, 115, 116, 105, 99, 97, 116, 105, 111, 110 }

csharp> System.Text.Encoding.GetEncoding("UTF-16").GetBytes("Supergroovalisticprosifunkstication")
{ 83, 0, 117, 0, 112, 0, 101, 0, 114, 0, 103, 0, 114, 0, 111, 0, 111, 0, 118, 0, 97, 0, 108, 0, 105, 0, 115, 0, 116, 0, 105, 0, 99, 0, 112, 0, 114, 0, 111, 0, 115, 0, 105, 0, 102, 0, 117, 0, 110, 0, 107, 0, 115, 0, 116, 0, 105, 0, 99, 0, 97, 0, 116, 0, 105, 0, 111, 0, 110, 0 }
~~~

## Unicode Scalar Representation


~~~
 49> "Supergroovalisticprosifunkstication".unicodeScalars
$R23: String.UnicodeScalarView = {
  _core = {
    _baseAddress = 0x00000001028791b0
    _countAndFlags = 9223372036854775843
    _owner = nil
  }
}

 51> for i in "Supergroovalisticprosifunkstication".unicodeScalars { print("\(i.value)-")} ; println(""); 
83-117-112-101-114-103-114-111-111-118-97-108-105-115-116-105-99-112-114-111-115-105-102-117-110-107-115-116-105-99-97-116-105-111-110-

~~~

~~~
csharp> System.Text.Encoding.UTF8.GetBytes("Supergroovalisticprosifunkstication")
{ 83, 117, 112, 101, 114, 103, 114, 111, 111, 118, 97, 108, 105, 115, 116, 105, 99, 112, 114, 111, 115, 105, 102, 117, 110, 107, 115, 116, 105, 99, 97, 116, 105, 111, 110 }

csharp> foreach(var i in "Supergroovalisticprosifunkstication"){ Console.Write(string.Format("{0}-",(byte)i));}
83-117-112-101-114-103-114-111-111-118-97-108-105-115-116-105-99-112-114-111-115-105-102-117-110-107-115-116-105-99-97-116-105-111-110-
~~~





