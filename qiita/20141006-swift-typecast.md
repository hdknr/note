Swift vs. C#: Type Casting

- is(type check operator) & as(type cast operator)


# Defining a Class Hierarchy for Type Casting

~~~
  1> class MediaItem { 
  2.     var name: String 
  3.     init(name: String) { 
  4.         self.name = name 
  5.     }    
  6. } 
  7.  
  8. class Movie: MediaItem { 
  9.     var director: String 
 10.     init(name: String, director: String) { 
 11.         self.director = director 
 12.         super.init(name: name) 
 13.     }    
 14. } 
 15.   
 16. class Song: MediaItem { 
 17.     var artist: String 
 18.     init(name: String, artist: String) { 
 19.         self.artist = artist 
 20.         super.init(name: name) 
 21.     }    
 22. }
~~~

C#:

~~~
public class MediaItem {
    public string name;
}

public class Movie: MediaItem {
    public string director;
}   
 
public class Song: MediaItem {
    public string artist;
} 
~~~

# Checking Type

~~~
 25> var m = Movie(name:"Star Wars", director:"Lucas") 
m: Movie = {
  __lldb_expr_1.MediaItem = {
    name = "Star Wars"
  }
  director = "Lucas"
}
~~~

~~~
 26> var s = Song(name:"Let it be", artist:"Beatles")
s: Song = {
  __lldb_expr_1.MediaItem = {
    name = "Let it be"
  }
  artist = "Beatles"
}
~~~

~~~
 28> var i = MediaItem(name:"iPod") 

i: MediaItem = {
  name = "iPod"
}
~~~

- Any に入れないと is で判定できない

~~~
  9> let a: Any = MediaItem(name:"digital")
a: MediaItem = {
  name = "digital"
}
 10> a is MediaItem
$R0: Bool = true
~~~

~~~
 11> let m = MediaItem(name: "analog")
m: MediaItem = {
  name = "analog"
}
 12> m is MediaItem
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/77665/repl18.swift:2:3: error: 'is' test is always true
m is MediaItem
~~~


~~~
 19> var x :Any = Movie(name:"Jaws", director:"Spielberg")
x: Movie = {
  __lldb_expr_1.MediaItem = {
    name = "Jaws"
  }
  director = "Spielberg"
}

 20> x is Movie
$R1: Bool = true

 21> x is MediaItem
$R2: Bool = true

 30> x is Song
$R3: Bool = false
~~~

C#:  is = 指定した型との間に互換性があるかどうかをチェック

~~~
csharp> var m = new Movie{name="Star Wars", director="Lucas"}; 
~~~

~~~
csharp> m is Movie
true
csharp> m is MediaItem
true
csharp> m is Song
(1,4): warning CS0184: The given expression is never of the provided (`Song') type
false
~~~

objectで受けていれば is でwarningでません

~~~
csharp> object m = new Movie{name="Star Wars", director="Lucas"};  
csharp> m is Song
false
~~~

# Downcasting

- Downcast 

~~~
 31> x as MediaItem
$R4: Movie = {
  __lldb_expr_1.MediaItem = {
    name = "Jaws"
  }
  director = "Spielberg"
}

 32> x as? MediaItem
$R5: MediaItem? = (name = "Jaws")
~~~

- 失敗することもあるので、 as? をつかったほうがいい。asは必ず成功する場合のみ使う。

~~~
 33> x as? Song
$R6: Song? = nil
 34> x as Song
Execution interrupted. Enter Swift code to recover and continue.
Enter LLDB commands to investigate (type :help for assistance.)
~~~

C#:as 演算子はキャスト操作とよく似ています。 ただし、変換可能でない場合、as は、例外は発生せず、null を返します

~~~
csharp> object m = new Movie{name="Star Wars", director="Lucas"}; 
csharp> m as Song
null
csharp> m as MediaItem
Movie
~~~

object で受けていないと変換例外

~~~
csharp> var m = new Movie{name="Star Wars", director="Lucas"};     
csharp> m as Song

(1,4): error CS0039: Cannot convert type `Movie' to `Song' via a built-in conversion
~~~

C#: cast は (type)variable で、 as は以下のキャストの式に等しい

~~~
csharp> object x = m is Song ? (Song)m : (Song)null;
csharp> x
null
~~~

型チェックしないとSystem.InvalidCastException例外になるからです:

~~~
csharp> (Song)m

System.InvalidCastException: Cannot cast from source type to destination type.
~~~


# Type Casting for Any and AnyObject

AnyObject:

> AnyObject can represent an instance of any class type.


Any:

> Any can represent an instance of any type at all, apart from function types.


## AnyObject

~~~
 26> let someObjects: [AnyObject] = [ 
 27.     Movie(name: "2001: A Space Odyssey", director: "Stanley Kubrick"), 
 28.     Movie(name: "Moon", director: "Duncan Jones"), 
 29.     Movie(name: "Alien", director: "Ridley Scott") 
 30. ]
someObjects: [AnyObject] = 3 values {
  [0] = {
    __lldb_expr_1.MediaItem = {
      name = "2001: A Space Odyssey"
    }
    director = "Stanley Kubrick"
  }
  [1] = {
    __lldb_expr_1.MediaItem = {
      name = "Moon"
    }
    director = "Duncan Jones"
  }
  [2] = {
    __lldb_expr_1.MediaItem = {
      name = "Alien"
    }
    director = "Ridley Scott"
  }
}
~~~

~~~
 31> someObjects[0] is Movie 
$R0: Bool = true
 32> someObjects[0] as?  Movie 
$R1: Movie? = Some {
  __lldb_expr_1.MediaItem = {
    name = "2001: A Space Odyssey"
  }
  director = "Stanley Kubrick"
}
 33> someObjects[0] as  MediaItem
$R2: Movie = {
  __lldb_expr_1.MediaItem = {
    name = "2001: A Space Odyssey"
  }
  director = "Stanley Kubrick"
}
 34> someObjects[0] as? Song
$R3: Song? = nil
 35> someObjects[0] as Song
Execution interrupted. Enter Swift code to recover and continue.
Enter LLDB commands to investigate (type :help for assistance.)
~~~~

## Any

- Anyは値型でもOK

~~~
 36> var thins = [Any]()
thins: [(Any)] = 0 values
 37> var things = [Any]() 
things: [(Any)] = 0 values
 38> things.append(Movie(name: "Alien", director: "Ridley Scott"))
 39> things[0] is Movie
$R4: Bool = true
 40> things.append("32")
 41> things[1] is String
$R5: Bool = true
 42> things[1] as? Int
$R6: Int? = nil
~~~

- AnyObjectは 参照型しか入れられない

~~~
 43> var objs = [AnyObject]()
objs: [(AnyObject)] = 0 values

 44> objs.append(0) 
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/78623/repl39.swift:2:6: error: type 'AnyObject' does not conform to protocol 'IntegerLiteralConvertible'
objs.append(0)
     ^
 44> objs.append("32")
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/78623/repl40.swift:2:6: error: type 'AnyObject' does not conform to protocol 'StringLiteralConvertible'
objs.append("32")
     ^

 44> objs.append(Movie(name: "Alien", director: "Ridley Scott"))
 45> objs[0] is Movie
$R7: Bool = true
~~~~

C#: object = Any + AnyObject

~~~
csharp> object i ; 
csharp> i = 3
csharp> public class MediaItem {
      >     public string name;
      > }
csharp>  
csharp> i = new MediaItem()
csharp> i.GetType()
MediaItem
csharp> i = 3
csharp> i.GetType()
System.Int32
~~~

# C# :[キャストと型変換](http://msdn.microsoft.com/ja-jp/library/ms173105.aspx)

- [暗黙の型変換](http://msdn.microsoft.com/ja-jp/library/y5b434w4.aspx)
- [明示的な型変換](http://msdn.microsoft.com/ja-jp/library/yht2cx7b.aspx) (キャスト) 
- ユーザー定義変換([変換演算子](http://msdn.microsoft.com/ja-jp/library/09479473.aspx))
- ヘルパー クラス( [System.BitConverter](http://msdn.microsoft.com/ja-jp/library/system.bitconverter.aspx) , [System.Convert](http://msdn.microsoft.com/ja-jp/library/system.convert.aspx), Type.Parse([Int32.Parse](http://msdn.microsoft.com/ja-jp/library/system.int32.parse.aspx) など)) 
