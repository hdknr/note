Swift vs. C# : Classes and Structures


# Comparing Classes and Structures

Class & Structure:

- Define properties to store values(プロパティ)
- Define methods to provide functionality(メソッド)
- Define subscripts to provide access to their values using subscript syntax(サブスクリプト)
- Define initializers to set up their initial state(イニシャライザー)
- Be extended to expand their functionality beyond a default implementation(拡張可能)
- Conform to protocols to provide standard functionality of a certain kind(プロトコル)

Classのみ:

- Inheritance enables one class to inherit the characteristics of another(継承).
- Type casting enables you to check and interpret the type of a class instance at runtime(キャスト).
- Deinitializers enable an instance of a class to free up any resources it has assigned(解放/Dispose/ファイナライザ).
- Reference counting allows more than one reference to a class instance.(参照カウンタ)(Structureは参照カウントされずに必ず複製)

## Definition Syntax

Swift:

~~~
 39> struct Resolution { 
 40.     var width = 0 
 41.     var height = 0 
 42. }
 43> class VideoMode { 
 44.     var resolution = Resolution() 
 45.     var interlaced = false 
 46.     var frameRate = 0.0 
 47.     var name: String? 
 48. }
 ~~~
 
 C#:
 
~~~
struct Resolution { 
    public int width ;
    public int height ;
    public Resolution(int w, int h ){
        this.width =w; 
        this.height =h; 
    }   
}

class VideoMode { 
    public Resolution resolution = new Resolution() ;
    public bool interlaced = false ;
    public float frameRate = 0.0f ;
    public string name ;
}
~~~			
			
			
## Class and Structure Instances

Swift:

~~~

 49> var r = Resolution()
r: Resolution = {
  width = 0
  height = 0
}


 50> var v = VideoMode()
v: VideoMode = {
  resolution = {
    width = 0
    height = 0
  }
  interlaced = false
  frameRate = 0
  name = nil
}			
~~~

C#:

~~~
var r = new Resolution ();
var v = new VideoMode ();
~~~			

## Accessing Properties

Swift:

~~~
 52> r.width
$R21: Int = 0
 53> v.resolution.width
$R22: Int = 0
 54> v.resolution.width = 10
 55> v.resolution.width 
$R23: Int = 10
~~~

C#:

~~~
var v = new VideoMode();
v.name = "4K";
    
Assert(v.resolution.width == 0 );
Assert(v.name == "4K" );
~~~


## Memberwise Initializers for Structure Types


Swift: デフォルトで使える

~~~~

 56> Resolution(width: 640, height: 480)
$R24: Resolution = {
  width = 640
  height = 480
}

~~~~

C#: プロパティをオブジェクト初期化子で初期化

~~~
	struct Resolution { 
			public int width  { get; set ;}
			public int height {get;set; }
    }
~~~
~~~
var r = new Resolution (){ width = 100, height=80 };
Assert.AreEqual (r.width, 100);
~~~		


# Structures and Enumerations Are Value Types

>> All structures and enumerations are value types in Swift.

- 値型はいつもコピーされる
- enum も値型
- Swift, C# ともに
- 値型なのでinitial/newしなくてもよい

Swift:

~~~
  1>  struct Resolution {  
  2.    var width: Int 
  3.    var height: Int  
  4.  }

  5> var r: Resolution
r: Resolution = {
  width = 0
  height = 0
}

  6> assert(r.width == 0)
~~~


C#: 

~~~
csharp> struct Resolution { 
      >     public int width ;
      >     public int height ;
      >     public Resolution(int w, int h ){
      >         this.width =w; 
      >         this.height =h; 
      >     }   
      > }
csharp> Resolution r;
csharp> r.width++;
0
csharp> r.width 
1
~~~

Swift/C# ともに 型のデフォルト値で初期化(Int/int : 0 )

# Classes Are Reference Types

> Unlike value types, reference types are not copied when they are assigned to a variable or constant, or when they are passed to a function. Rather than a copy, a reference to the same existing instance is used instead.

- 参照型

Swift:

~~~
  9> class Profile { 
 10.    var age = 0 
 11. }    
 12>  
 13> var p1 = Profile()
p1: Profile = {
  age = 0
}
 14> var p2 = p1
p2: Profile = {
  age = 0
}
 15> p1.age = 200
 16> p2
$R1: Profile = {
  age = 200
}
~~~  
  
C# :

~~~
csharp> public class Profile {
      >    public int age = 0;
      > }
csharp> var p1 = new Profile();
csharp> var p2 = p1;
csharp> p1.age = 200;
csharp> p2.age
200
~~~  

## Identity Operators


Swift:


- "===", "!==" (注意！ 参照の比較と値の比較は違うよ)


~~~
 17> p1 === p2
$R2: Bool = true
~~~

C#:	

- "=="  "!=", Equals, ReferenceEquals

- 演算子 : 2 つの参照が同じオブジェクトを示すかどうかを確認して参照の等価をテスト

~~~
csharp> p1 == p2
true
~~~

- 値等価

~~~
csharp> p1.Equals(p2)
true
~~~

- 参照等価

~~~
csharp> System.Object.ReferenceEquals(p1, p2)
true
~~~

## Pointers

- 参照型はCのポインタみたいだけど実際のアドレスをさすんじゃないよ

# Choosing Between Classes and Structures


- ClassとStructureの使い分けの話

# Assignment and Copy Behavior for Strings, Arrays, and Dictionaries



Stucture:

- String, Array, Dictionary はStructureで実装されている
- つまりコピーで渡される
- 実際にコピーされるかどうかはオプティマイザが判断

Class:

- NSString, NSArray,  NSDictionary はClassで実装されている
- つまり参照で渡される






