Swift vs. C# : Nested Types

- struct, enum, class がネストできるということ
- C#: enumはネストできないとおもう。stuct, classはネストできる。


# Nested Types in Action

~~~
  1> struct BlackjackCard { 
  2.  
  3.     // nested Suit enumeration 
  4.     enum Suit: Character { 
  5.         case Spades = "♠", Hearts = "♡", Diamonds = "♢", Clubs = "♣" 
  6.     } 
  7.  
  8.     // nested Rank enumeration 
  9.     enum Rank: Int { 
 10.         case Two = 2, Three, Four, Five, Six, Seven, Eight, Nine, Ten 
 11.         case Jack, Queen, King, Ace 
 12.         struct Values { 
 13.             let first: Int, second: Int? 
 14.         } 
 15.         var values: Values { 
 16.             switch self { 
 17.             case .Ace: 
 18.                 return Values(first: 1, second: 11) 
 19.             case .Jack, .Queen, .King: 
 20.                 return Values(first: 10, second: nil) 
 21.             default: 
 22.                 return Values(first: self.toRaw(), second: nil) 
 23.             } 
 24.         } 
 25.     } 
 26.  
 27.     // BlackjackCard properties and methods 
 28.     let rank: Rank, suit: Suit 
 29.     var description: String { 
 30.          
 31.         var output = "suit is \(suit.toRaw())," 
 32.         output += " value is \(rank.values.first)" 
 33.         if let second = rank.values.second { 
 34.             output += " or \(second)" 
 35.         } 
 36.         return output 
 37.     } 
 38. }
~~~



# Referring to Nested Types

- ドットで参照

~~~
 39> var r = BlackjackCard.Rank.Jack 
r: BlackjackCard.Rank = Jack
~~~ 

- C#同じ
