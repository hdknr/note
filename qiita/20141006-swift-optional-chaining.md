Swift vs. C# : Optional Chaining

> Optional chaining is a process for querying and calling properties, methods, and subscripts on an optional that might currently be nil. 

> If the optional contains a value, the property, method, or subscript call succeeds; 

> if the optional is nil, the property, method, or subscript call returns nil.

# Optional Chaining as an Alternative to Forced Unwrapping


~~~
  2> class Person { 
  3.     var residence: Residence? 
  4. } 
  5.   
  6. class Residence { 
  7.     var numberOfRooms = 1 
  8. }
  
  
  9> var p = Person()
p: Person = {
  residence = nil
}

 10> p.residence
$R2: Residence? = nil
~~~

- Optional Chaining : “?” 付ける

~~~
 12> p.residence?.numberOfRooms 
$R0: Int? = nil

~~~

- Forced Unwrapping 。この時点で optional な residenceはnilなのでvalueをunwrapできない

~~~
 19> p.residence!

fatal error: unexpectedly found nil while unwrapping an Optional value
Execution interrupted. 

Enter Swift code to recover and continue.
Enter LLDB commands to investigate (type :help for assistance.)
~~~

- p.residenceを作成

~~~
 20> p.residence = Residence()
~~~

- Forced Unwrapping

~~~ 
 21> p.residence!
$R6: Residence = {
  numberOfRooms = 1
}
~~~

- Optional Chaining

~~~
 22> p.residence?
$R7: Residence? = (numberOfRooms = 1)
~~~

- numberOfRoomsもInt? -> Chaining

~~~
 24> p.residence?.numberOfRooms 
$R9: Int? = 1
~~~

- Unwrap されると numberOfRoomsはInt

~~~
 25> p.residence!.numberOfRooms 
$R10: Int = 1
~~~

- resideneにインスタンス参照があろうとなかろうと numberOfRoomsを nil判定できる(Chaining)

~~~
 27> p.residence = nil
 28> p.residence?.numberOfRooms == nil
$R12: Bool = true
 29> p.residence = Residence()
 30> p.residence?.numberOfRooms == nil 
$R13: Bool = false
 31> p.residence?.numberOfRooms == 1
$R14: Bool = true
~~~


## C# ぬるぽ。以上。

~~~
csharp> public class Residence {
      >    public int numberOfRooms = 1;
      > }
csharp> public class Person {
      >    public Residence residence;
      > }
~~~

~~~
csharp> var p = new Person();
csharp> p.residence.numberOfRooms
System.NullReferenceException: Object reference not set to an instance of an object
~~~      


# Defining Model Classes for Optional Chaining

- 複雑なクラスのモデルでもさかのぼってchainできる

~~~
class Room {
    let name: String
    init(name: String) { self.name = name }
}

class Address {
    var buildingName: String?
    var buildingNumber: String?

    func buildingIdentifier() -> String? {
        if buildingName != nil {
            return buildingName
        } else if buildingNumber != nil {
            return buildingNumber
        } else {
            return nil
        }
    }
}

class Residence {
    var rooms = [Room]()
    var numberOfRooms: Int {
        return rooms.count
    }
    subscript(i: Int) -> Room {
        get { return rooms[i] }
        set { rooms[i] = newValue }
    }
    func printNumberOfRooms() {
        println("The number of rooms is \(numberOfRooms)")
    }
    var address: Address?
}


class Person {
    var residence: Residence?
}
~~~

# Accessing Properties Through Optional Chaining

- rootmCountがnilなので

~~~
 41> let john = Person() 
 42. if let roomCount = john.residence?.numberOfRooms { 
 43.     println("John's residence has \(roomCount) room(s).") 
 44. } else { 
 45.     println("Unable to retrieve the number of rooms.") 
 46. }
 
Unable to retrieve the number of rooms.
john: Person = {
  residence = nil
}

 47> john.residence?.numberOfRooms
$R0: Int? = nil
~~~



# Calling Methods Through Optional Chaining

~~~
 53>  john.residence?.printNumberOfRooms() != nil
$R6: Bool = false
 54>  john.residence?.printNumberOfRooms() 
$R7: ()? = nil
~~~

~~~
 57> if john.residence?.printNumberOfRooms() != nil { 
 58.     println("It was possible to print the number of rooms.") 
 59. } else { 
 60.     println("It was not possible to print the number of rooms.") 
 61. }
It was not possible to print the number of rooms.
~~~


# Accessing Subscripts Through Optional Chaining

- サブスクリプトアクセスしてもnil

~~~
 48> john.residence?[0]
$R1: Room? = nil
~~~

- 部屋名も nil

~~~
 49> john.residence?[0].name
$R2: String? = nil
~~~

- もちろん住所も

~~~
 52> john.residence?.address?.buildingName
$R5: String? = nil
~~~


## Accessing Subscripts of Optional Type

~~~
  1> var testScores = ["Dave": [86, 82, 84], "Bev": [79, 94, 81]]
testScores: [String : [Int]] = {
  [0] = {
    key = "Dave"
    value = 3 values {
      [0] = 86
      [1] = 82
      [2] = 84
    }
  }
  [1] = {
    key = "Bev"
    value = 3 values {
      [0] = 79
      [1] = 94
      [2] = 81
    }
  }
}
~~~

~~~
  2> testScores["Brian"]?[0] = 72
$R0: ()? = nil
~~~

C#:KeyNotFoundException

~~~
csharp> var score = new Dictionary<string, List<int>>{{"Dave", new List<int>{86, 82, 84}}, {"Bev", new List<int>{79, 94, 81}}};
~~~

~~~
csharp> score["Dave"][0]++;
86

csharp> score["Dave"][0] 
87
~~~

~~~
csharp> score["Brian"][0]
System.Collections.Generic.KeyNotFoundException: The given key was not present in the dictionary.
~~~

# Linking Multiple Levels of Chaining



> If the type you are trying to retrieve is not optional, it will become optional because of the optional chaining.

参照する型がオプショナルではない -> オプショナル化(chaing)

    Intを参照 -> Int? が返る


> If the type you are trying to retrieve is already optional, it will not become more optional because of the chaining.

参照する型がオプショナル -> オプショナルのオプショナルにならずオプショナルのまま

     Int? を参照 ->  Int?  が返る




# Chaining on Methods with Optional Return Values


~~~
 40> var john = Person()
john: Person = {
  residence = nil
}
 41> john.residence?.address?.buildingIdentifier() 
$R0: String? = nil
~~~

~~~
 42> john.residence?.address?.buildingIdentifier()?.hasPrefix("The")
$R1: Bool? = nil
~~~

Python:

~~~
print john.residence and john.residence.address and john.residence.address.buildingIdentifier()
~~~



