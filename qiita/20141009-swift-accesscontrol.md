Swift vs. C# : Access Control

# Modules and Source Files

Module: ビルド単位

> A module is a single unit of code distribution—a framework or application that is built and shipped as a single entity and that can be imported by another module with Swift’s import keyword.


Source File: *.swift 単位

> A source file is a single Swift source code file within a module (in effect, a single file within an app or framework). 

> Although it is common to define individual types in separate source files, a single source file can contain definitions for multiple types, functions, and so on.



# Access Levels


Public: 全解放

> Public access enables entities to be used within any source file from their defining module, and also in a source file from another module that imports the defining module. 

> You typically use public access when specifying the public interface to a framework.


Internal: モジュール内限定

> Internal access enables entities to be used within any source file from their defining module, but not in any source file outside of that module. 

> You typically use internal access when defining an app’s or a framework’s internal structure.

Private: 同じソースファイル限定

> Private access restricts the use of an entity to its own defining source file. 


> Use private access to hide the implementation details of a specific piece of functionality.


## Guiding Principle of Access Levels


Principal: より低いレベルのエンティティに関しては定義できない

> No entity can be defined in terms of another entity that has a lower (more restrictive) access level.

- private/inernalタイプは public で定義できない
- 引き数、返り値の型を上回るレベルの関数を定義できない




## Default Access Levels


- デフォルト internal 



## Access Levels for Single-Target Apps

- すべてinternal(デフォルト)で特に指定しなくていよい

## Access Levels for Frameworks

- public-facing interface == "API"

# Access Control Syntax


- クラス

~~~
public class SomePublicClass {}
internal class SomeInternalClass {}
private class SomePrivateClass {}
~~~


- グローバルスコープ変数&関数

~~~
public var somePublicVariable = 0
internal let someInternalConstant = 0
private func somePrivateFunction() {}
~~~

- public, private を指定しないと "internal"


# Custom Types

- 自前で定義したclassとか

~~~
public class SomePublicClass {          // explicitly public class
    public var somePublicProperty = 0    // explicitly public class member
    var someInternalProperty = 0         // implicitly internal class member
    private func somePrivateMethod() {}  // explicitly private class member
}
~~~

~~~
class SomeInternalClass {               // implicitly internal class
    var someInternalProperty = 0         // implicitly internal class member
    private func somePrivateMethod() {}  // explicitly private class member
}
~~~

~~~ 
private class SomePrivateClass {        // explicitly private class
    var somePrivateProperty = 0          // implicitly private class member
    func somePrivateMethod() {}          // implicitly private class member
}

~~~

- Profileはinternalなので、public のプロパティを定義できない

~~~
class Profile {
  public var name = ""
}
~~~
~~~
$ alias SWC='xcrun --sdk iphonesimulator8.0 swiftc'
$ SWC mymod.swift 
mymod.swift:2:3: warning: declaring a public var for an internal class
  public var name = ""
  ^~~~~~
  internal
~~~

- privateだったらOK

~~~
class Profile {
  private var name = ""
}
~~~

## Tuple Types

- Tupleの要素中、もっとも厳しい要素と同じアクセスレベル

~~~
class Profile {
  private var name = ""
}

public var admin: (Profile, Int) = ( Profile(), 1 )
~~~

~~~
$ SWC mymod.swift 

mymod.swift:5:12: error: variable cannot be declared public because its type uses an internal type
public var admin: (Profile, Int) = ( Profile(), 1 )
           ^       ~~~~~~~
mymod.swift:1:7: note: type declared here
class Profile {
      ^
~~~

~~~
private class Profile {
  private var name = ""
}

var admin: (Profile, Int) = ( Profile(), 1 )
~~~
~~~
$ SWC mymod.swift 

mymod.swift:5:5: error: variable must be declared private because its type uses a private type
var admin: (Profile, Int) = ( Profile(), 1 )
    ^       ~~~~~~~
mymod.swift:1:15: note: type declared here
private class Profile {
              ^
~~~

              
## Function Types

- 関数の引数と、返り値のアクセスレベルでもっとも厳しいものと同じアクセスレベル

~~~
private class Profile {
  private var name = ""
  init(name: String){ self.name = name }
}

public func get_admin() -> Profile { return Profile(name:"Admin") }
~~~

~~~
$ SWC mymod.swift 
mymod.swift:6:13: error: function cannot be declared public because its result uses a private type
public func get_admin() -> Profile { return Profile(name:"Admin") }
            ^              ~~~~~~~
mymod.swift:1:15: note: type declared here
private class Profile {
              ^
~~~

## Enumeration Types

- enumの要素はすべて同じレベルであること

### Raw Values and Associated Values

- enumのRaw Valueにはenum自身より厳しい制限を設定できない

## Nested Types

- private タイプ内のネストタイプは自動的に private
- public/internalタイプ内のネストタイプは自動的にinternal
- public内のネストタイプをpublicにしたいのであれば、必ず明示的にpublic修飾すること

~~~
class Cube {
    public class Point {
        var i = 0
        var j = 0       
    }
}

~~~

~~~
$ SWC mymod.swift 
mymod.swift:2:5: warning: declaring a public class for an internal class
    public class Point {
    ^~~~~~
    internal
~~~


# Subclassing

- サブクラスはスーパークラス以上のアクセスレベルは設定できません

~~~
  1> internal class X { private func someMethod() {} }
  2> public class Y: X { override internal func someMethod() {} }
  
  
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/44406/repl3.swift:2:44: error: overriding instance method must be as accessible as the declaration it overrides
public class Y: X { override internal func someMethod() {} }
                             ~~~~~~~~      ^
                             public
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/44406/repl1.swift:2:33: note: overridden declaration is here
internal class X { private func someMethod() {} }
                                ^

~~~


# Constants, Variables, Properties, and Subscripts

- 型のアクセスレベルよりパブリックには出来ない

~~~
class Profile {    // internal
    var name = ""
    init(name: String) {self.name = name }
}

public var Admin = Profile(name:"Admin")
~~~

~~~
$ SWC mymod.swift 

mymod.swift:6:12: error: variable cannot be declared public because its type 'Profile' uses an internal type
public var Admin = Profile(name:"Admin")
           ^
~~~

~~~
private class Profile {
    var name = ""
    init(name: String) {self.name = name }
}

var Admin = Profile(name:"Admin")
~~~



## Getters and Setters

~~~
import Foundation

struct TrackedString {
    private(set) var numberOfEdits = 0
    var value: String = "" {
        didSet {
            numberOfEdits++
        }
    }
}
~~~

~~~
var x = TrackedString()
x.value = "xxx"
x.value = "yyy"
println(x.numberOfEdits)   // 2
x.numberOfEdits = 3        // Can't assign to "numberOfEdits" in "x"
~~~        

# Initializers

- required initializerはclassと同じレベル
- custom initializersはclassのレベル以下に設定できる
- initializerのパラメータレベルはinitializerよりプライベートには出来ない

## Default Initializers

- initializeするタイプと同じレベル

## Default Memberwise Initializers for Structure Types

- structureのstored propertyのどれかがprivateだとdefault memberwise initializerは private
- これ以外の場合internal
- 別モジュールでmemberwise initializerで初期化するpubic structureを定義したかったら、 public memberwise initializerを定義しろ


# Protocols

- protocol requirementは protocolと同じレベル
- 個別にprotocol requirementに異なるレベルを設定できない

## Protocol Inheritance

- 継承元のプロトコルのレベルと同じ

~~~
protocol HumanProtocol {
    var name: String { get set  }
}

public protocol AdultProtocol: HumanProtocol {
}
~~~

~~~
$ SWC mymod.swift 
mymod.swift:5:17: error: public protocol cannot refine an internal protocol
public protocol AdultProtocol: HumanProtocol {
                ^              ~~~~~~~~~~~~~
mymod.swift:1:10: note: type declared here
protocol HumanProtocol {
         ^
~~~



## Protocol Conformance


# Extensions

## Adding Protocol Conformance with an Extension


# Generics

# Type Aliases




