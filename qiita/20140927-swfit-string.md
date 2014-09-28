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


~~~


