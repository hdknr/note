Swift vs. C# : Protocols

Protocol:

> A protocol defines a blueprint of methods, properties, and other requirements that suit a particular task or piece of functionality.

- C#: [Interface](http://msdn.microsoft.com/ja-jp/library/87d83y5b.aspx)。ただし、inerfaceのメソッドはすべて実装する必要あり





# Protocol Syntax

- 定義

~~~
protocol SomeProtocol {
    // protocol definition goes here
}

~~~

- 実装(struct)

~~~
struct SomeStructure: FirstProtocol, AnotherProtocol {
    // structure definition goes here
}
~~~

- class

~~~
class SomeClass: SomeSuperclass, FirstProtocol, AnotherProtocol {
    // class definition goes here
}
~~~

C#:

~~~
interface SomeProtocol {
    void Do (); 
}

public struct SomeStructure :SomeProtocol
    //, AnotherProtocol
{
    public void Do(){
        Console.WriteLine ("struct do");
    }   
}
public class SomeClass: SomeProtocol
    //,SomeSuperclass, FirstProtocol, AnotherProtocol 
{
    public void Do(){
        Console.WriteLine ("class do");
    }   
}
~~~

# Property Requirements

~~~
  1> protocol FullyNamed { 
  2.     var fullName: String { get } 
  3. }

  4>  
  5> struct Person: FullyNamed { 
  6.     var fullName: String 
  7. } 
  8.  
  8> let john = Person(fullName: "John Appleseed")                                                                                                          
john: Person = {
  fullName = "John Appleseed"
}
~~~

C#:

~~~
interface FullyNamed 
{
    string fullName { 
        get;
    }
}

public struct Person: FullyNamed {

    public Person(string fullName)
    { _fullName = fullName; }

    public string fullName { 
        get{ return _fullName;}
    }
   
    public string _fullName;    // public はあまり意味ないけど
}

var john = new Person("John Appleseed") 
Console.WriteLine(john.fullName);

~~~


# Method Requirements

- プロトコル

~~~
  2> protocol RandomNumberGenerator { 
  3.     func random() -> Double 
  4. }
~~~


- 実装

~~~
  6> class LinearCongruentialGenerator: RandomNumberGenerator { 
  7.     var lastRandom = 42.0 
  8.     let m = 139968.0 
  9.     let a = 3877.0 
 10.     let c = 29573.0 
 11.     func random() -> Double { 
 12.         lastRandom = ((lastRandom * a + c) % m) 
 13.         return lastRandom / m 
 14.     } 
 15. }
~~~

# Mutating Method Requirements

- 破壊メソッド要件 = mutatin func

~~~
protocol Togglable {
    mutating func toggle()
}
~~~

# Initializer Requirements

- イニシャライザ

~~~
protocol Togglable {
    mutating func toggle()
}
~~~

## Class Implementations of Protocol Initializer Requirements


- サブクラスへの required 強制 (designated initializer/convenience initializer)

~~~
class SomeClass: SomeProtocol {
    required init(someParameter: Int) {
        // initializer implementation goes here
    }
}
~~~
( [Required Initializers](https://developer.apple.com/library/prerelease/mac/documentation/Swift/Conceptual/Swift_Programming_Language/Initialization.html#//apple_ref/doc/uid/TP40014097-CH18-XID_341) )


- プロトコルイニシャライザinit()

~~~
protocol SomeProtocol {
    init()
}
~~~

-  スーパークラスで init()を定義済み

~~~ 
class SomeSuperClass {
    init() {
        // initializer implementation goes here
    }
}
 
~~~

- よって、サブクラスでは override 必要

~~~ 
class SomeSubClass: SomeSuperClass, SomeProtocol {
    // "required" from SomeProtocol conformance; "override" from SomeSuperClass
    required override init() {
        // initializer implementation goes here
    }
}
~~~

# Protocols as Types

- プロパティ(メンバー)の型を Protocolで宣言できる

~~~
  1> protocol PersonProtocol {  
  2.     var name: String { get set }  
  3.     init(name: String)  
  4. }  
~~~

~~~
  7. class Person: PersonProtocol {  
  8.     var name: String  
  9.     required init(name: String ) { self.name = name }  
 10. } 
~~~

~~~
 12. class Student : Person { }  

 15. class Employee : Person { }  
~~~

~~~
 18. class Circle {  
 19.     var members : [PersonProtocol] = [] 
 20.     init(members: [PersonProtocol]) { self.members = members } 
 21. } 
~~~

~~~
 22> var c = Circle(members:[Student(name:"Alice"), Employee(name:"Bob")])

c: Circle = {
  members = 2 values {
    [0] = {
      __lldb_expr_1.Person = {
        name = "Alice"
      }
    }
    [1] = {
      __lldb_expr_1.Person = {
        name = "Bob"
      }
    }
  }
}

~~~   
      
~~~
 23> c.members[0] is PersonProtocol
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/43277/repl14.swift:2:14: error: 'is' test is always true
c.members[0] is PersonProtocol
             ^

 23> c.members[0] is Employee
$R0: Bool = false
 24> c.members[0] is Student
$R1: Bool = true
 25> c.members[0] is Person
$R2: Bool = true

~~~      

C#:

~~~
public interface IPerson
{
    string name {get;set;}
}

public class Person: IPerson{
    public string name {get;set;}
}

public class Student: Person {}
public class Employee: Person {}

public class Circle 
{
   public List<IPerson>  members {get;set; }
}
~~~

C#

~~~
var c = new Circle{ members = new List<IPerson>{
        new  Student{name="Alice"},
        new  Employee{name="Bob"},
    }};

foreach(var p in c.members){
   Console.WriteLine(p.name + "********");
   Console.Write(p is IPerson); Console.Write(",");
   Console.Write(p is Person);Console.Write(",");
   Console.Write(p is Student);Console.Write(",");
   Console.Write(p is Employee);Console.WriteLine(",");
~~~

~~~
Alice********
True,True,True,False,
Bob********
True,True,False,True,
~~~

# Delegation

"**[Delegation Pattern](https://en.wikipedia.org/wiki/Delegation_pattern)**":

> , the delegation pattern is a design pattern in object-oriented programming where an object, instead of performing one of its stated tasks, delegates that task to an associated helper object. 

> There is an Inversion of Responsibility in which a helper object, known as a delegate, is given the responsibility to execute a task for the delegator. 


Apple "**Delegation**"

> Delegation is a design pattern that enables a class or structure to hand off (or delegate) some of its responsibilities to an instance of another type.

> This design pattern is implemented by defining a protocol that encapsulates the delegated responsibilities, such that a conforming type (known as a delegate) is guaranteed to provide the functionality that has been delegated. 

~~~
  1> protocol MonotonousDelegate 
  2. { 
  3.    func send_fax() 
  4.    func check_mail() 
  5. } 
  6.  
  7. protocol MamagementDelegate 
  8. { 
  9.    func allocate() 
 10.    func review() 
 11. } 
 12.  
 13. class Employee 
 14. { 
 15.    var name : String 
 16.    init(name: String){ self.name = name } 
 17. } 
 18.  
 19. class Secretary : Employee, MonotonousDelegate 
 20. { 
 21.   func send_fax(){ println("\(name) is sending a fax.") } 
 22.   func check_mail(){ println("\(name) is checking mails .") } 
 23. } 
 24. class Manager: Employee, MonotonousDelegate, MamagementDelegate 
 25. { 
 26.     var secretary : Secretary? 
 27.     init (name: String, secretary: Secretary? = nil ) 
 28.     { super.init(name: name) ; self.secretary = secretary } 
 29.  
 30.     func send_fax(){ secretary?.send_fax() } 
 31.     func check_mail() { secretary?.check_mail() } 
 32.     func allocate(){ println("\(name) is allocation a tast.") } 
 33.     func review(){ println("\(name) is review outcome.") } 
 34. } 
 ~~~
 
 ~~~
  38> var bob = Manager(name: "Bob")
bob: Manager = {
  __lldb_expr_1.Employee = {
    name = "Bob"
  }
  secretary = nil
}
~~~

~~~
 39> var dave = Manager(name: "Dave", secretary: Secretary(name:"Alice")) 
dave: Manager = {
  __lldb_expr_1.Employee = {
    name = "Dave"
  }
  secretary = Some {
    __lldb_expr_1.Employee = {
      name = "Alice"
    }
  }
}
~~~

~~~
 40> bob.check_mail()
 41> dave.check_mail()
Alice is checking mails .
~~~




# Adding Protocol Conformance with an Extension

- 既存クラス(別人が作ったクラス)に"Extensions"の仕組みでプロトコルを追加できる

~~~
 36. public protocol CleanerProtocol{ 
 37.     func clean_desk() 
 38. } 
~~~

~~~ 
 41. extension Manager: CleanerProtocol  
 42. { 
 43.     public func clean_desk () { println("\(name) is clearing hes/her desk.") } 
 44. } 
~~~

~~~
 47> edit.clean_desk()
Edie is clearing hes/her desk.
 48> var edie = Manager(name:"Edie")
edie: Manager = {
  __lldb_expr_1.Employee = {
    name = "Edie"
  }
  secretary = nil
}
~~~

~~~
 49> edit.clean_desk()
Edie is clearing hes/her desk.
~~~

これでいいような気もするんですが

~~~
 40> class ManagerEx: Manager, CleanerProtocol 
 41. { 
 42.     func clean_desk () { println("\(name) is clearing hes/her desk.") } 
 43. }
~~~

~~~ 
 44> var fred = ManagerEx(name:"Fred")
fred: ManagerEx = {
  __lldb_expr_1.Manager = {
    __lldb_expr_1.Employee = {
      name = ""
    }
    secretary = nil
  }
}
 45> fred.clean_desk()
Fred is clearing hes/her desk.
~~~

## Declaring Protocol Adoption with an Extension

~~~
 40> class Student 
 41. { 
 42.    var name : String 
 43.    func clean_desk() { println("Of cource, \(name) can clean hes/her desk.") } 
 44.    init(name: String) { self.name = name } 
 45. }
~~~

~~~ 
 46> var angie = Student(name:"Angie")
angie: Student = {
  name = "Angie"
}
 47> angie is CleanerProtocol


/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/44365/repl11.swift:2:7: error: cannot downcast from 'Student' to non-@objc protocol type 'CleanerProtocol'
angie is CleanerProtocol
~~~~~ ^  ~~~~~~~~~~~~~~~

~~~

- Studentは clean_desk()できるが、 プロトコル拡張してみる

~~~
 47> extension Student: CleanerProtocol {}
~~~

~~~
 49> var bill = Student(name:"Bill")
bill: Student = {
  name = "Bill"
}
 50> bill is CleanerProtocol
 
 
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/44365/repl16.swift:2:5: error: 'is' test is always true
bill is CleanerProtocol
     ^
     ~~~
~~~
     

# Collections of Protocol Types

~~~
 18> var members : [PersonProtocol] = [Student(name:"Angie"), Employee(name:"Bill")] 
 
 
members: [PersonProtocol] = 2 values {
  [0] = {
    __lldb_expr_1.Person = {
      name = "Angie"
    }
  }
  [1] = {
    __lldb_expr_1.Person = {
      name = "Bill"
    }
  }
}
~~~

# Protocol Inheritance

- 継承できる

~~~
 13. protocol BossProtocol: MonotonousDelegate, MamagementDelegate 
 14. { 
 15. }
~~~

C#:

~~~
public interface IMonotonous
{
   void send_fax();
   void check_mail();
}

public interface IMamagement
{
   void allocate();
   void review();
}

public interface IBoss: IMonotonous, IMamagement
{
}


//public class DivisionManager : IBoss
//{
//    (1,15): error CS0535: `DivisionManager' does not implement interface member `IMonotonous.send_fax()'
//    (1,15): error CS0535: `DivisionManager' does not implement interface member `IMonotonous.check_mail()'
//    (1,15): error CS0535: `DivisionManager' does not implement interface member `IMamagement.allocate()'
//    (1,15): error CS0535: `DivisionManager' does not implement interface member `IMamagement.review()'
//}

~~~
 
# Class-Only Protocols

- "class" 制約で、クラスのみ実行可能なプロトコルを定義

~~~
  1> protocol Speakable : class { 
  2.     func speak() 
  3. } 
~~~

~~~
  5. struct Animan: Speakable { 
  6.     func speak() { println("Can't speak") } 
  7. }
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/44627/repl1.swift:6:1: error: non-class type 'Animan' cannot conform to class protocol 'Speakable'
struct Animan: Speakable {
^
~~~


# Protocol Composition

> It can be useful to require a type to conform to multiple protocols at once. 

> You can combine multiple protocols into a single requirement with a protocol composition. 


~~~
  1> protocol Named { 
  2.     var name: String { get } 
  3. }    
  4. protocol Aged { 
  5.     var age: Int { get } 
  6. }    
  7. struct Person: Named, Aged { 
  8.     var name: String 
  9.     var age: Int 
 10. }
~~~

~~~
 18> func wishHappyBirthday(celebrator: protocol<Named, Aged>) { 
 19.     println("Happy birthday \(celebrator.name) - you're \(celebrator.age)!") 
 20. } 
~~~

~~~
 22. let p = Person(name: "Malcolm", age: 21)

p: Person = {
  name = "Malcolm"
  age = 21
}
~~~ 

~~~
 23> wishHappyBirthday(p)
Happy birthday Malcolm - you're 21!
~~~

~~~
 24> struct Animal: Named { 
 25.     var name: String 
 26.     var age: Int 
 27. }

 28> let a = Animal(name: "Genie", age:7 )


a: Animal = {
  name = "Genie"
  age = 7
} 
~~~

~~~
 29> wishHappyBirthday(a)
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/44710/repl14.swift:2:19: error: type 'Animal' does not conform to protocol 'Aged'
wishHappyBirthday(a)
                  ^
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/44710/repl6.swift:2:24: note: in initialization of parameter 'celebrator'
func wishHappyBirthday(celebrator: protocol<Named, Aged>) {
~~~
                       
 

# Checking for Protocol Conformance

Type Casting 参考。


is で型確認

> The is operator returns true if an instance conforms to a protocol and returns false if it does not.

as? でダウンキャスト。型が合わなければnil

>The as? version of the downcast operator returns an optional value of the protocol’s type, and this value is nil if the instance does not conform to that protocol.


asだとダウンキャストが失敗するとエラー

> The as version of the downcast operator forces the downcast to the protocol type and triggers a runtime error if the downcast does not succeed.



~~
 47> alice as MonotonousDelegate 
$R1: Secretary = {
  __lldb_expr_1.Employee = {
    name = "Alice"
  }
}
~~~

ん？

~~~
 48> alice as? MamagementDelegate
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/44843/repl38.swift:2:7: error: cannot downcast from 'Secretary' to non-@objc protocol type 'MamagementDelegate'
alice as? MamagementDelegate
~~~~~ ^   ~~~~~~~~~~~~~~~~~~
~~~

@obj 修飾: 

> You can check for protocol conformance only if your protocol is marked with the @objc attribute,....

え？NOTEに書く事なんですかね。

>  This attribute indicates that the protocol should be exposed to Objective-C code and is described in Using Swift with Cocoa and Objective-C. 

> Even if you are not interoperating with Objective-C, you need to mark your protocols with the @objc attribute if you want to be able to check for protocol conformance.

そしてクラスのみ

> Note also that @objc protocols can be adopted only by classes, and not by structures or enumerations. 


~~~
import Foundation

@objc protocol MonotonousDelegate
{
   func send_fax()
   func check_mail()
}

@objc protocol MamagementDelegate
{
   func allocate()
   func review()
}

~~~



~~~
 43> alice as MonotonousDelegate 
$R0: Secretary = {
  __lldb_expr_10.Employee = {
    name = "Alice"
  }
}
 44> alice as? MamagementDelegate
$R1: MamagementDelegate? = nil
~~~



# Optional Protocol Requirements

オプション要求できます。Object-cのプロトコルが、C#のインターフェースとちがってすべてのメソッドを実装しなくてもよい、ので互換性の為にあるような気がしますが、よくわかりません。:

>These requirements do not have to be implemented by types that conform to the protocol. 

>Optional requirements are prefixed by the optional modifier as part of the protocol’s definition.

~~~
  1> import Foundation
  2> @objc protocol MonotonousDelegate 
  3. { 
  4.    func send_fax() 
  5.    func check_mail() 
  6.    optional func make_money() 
  7.    optional var bonus : Int {get set}                                                                                                                  
  8. } 
~~~


~~~
  1> import Foundation  
  2.  
  3. @objc protocol MonotonousDelegate 
  4. { 
  5.    func send_fax() 
  6.    func check_mail() 
  7.    optional func make_money() 
  8.    optional var bonus : Int {get set}  
  9. } 
~~~

~~~
 21. @objc class Employee 
 22. {   
 23.    var name : String 
 24.    init(name: String){ self.name = name } 
 25. } 
 26.  
 27. @objc class Secretary : Employee, MonotonousDelegate 
 28. {  
 29.   func send_fax(){ println("\(name) is sending a fax.") } 
 30.   func check_mail(){ println("\(name) is checking mails .") } 
 31. }
~~~

~~~
 33> var alice: MonotonousDelegate? = Secretary(name:"Alice")
alice: MonotonousDelegate? = (instance_type = Builtin.RawPointer = 0x0000000100604490 -> 0x00000001003bfc70 direct type metadata for __lldb_expr_1.Secretary + 16)
~~~


~~~
 35> alice?.make_money?()
$R1: ()? = nil
~~~

~~~
 36> alice?.make_money()
/var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/lldb/45126/repl15.swift:2:8: error: value of optional type '(() -> ())?' not unwrapped; did you mean to use '!' or '?'?
alice?.make_money()
       ^
                 !
~~~


