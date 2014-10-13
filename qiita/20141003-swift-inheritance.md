Swift vs. C# : Inheritance

- superclass/subclass (Swift/C#)



# Defining a Base Class

Swift:

~~~
class Vehicle {

    var currentSpeed : Double = 0.0 {
         willSet(v) { println("Seeting \(v)") }
         didSet {  println("Now \(currentSpeed)") }
    }
    var speed: Double {
         get { return currentSpeed ; }
         set { currentSpeed = newValue; }
    }
    
    func makeNoise() {
        println("")
    }
}
~~~

C# 

~~~
public class Vehicle {

    protected double currentSpeed = 0.0;

    public double Speed{
         get { return currentSpeed ; }
         set { 
            Console.Write("Setting"); Console.WriteLine(value);
            currentSpeed = value; 
            Console.Write("now "); Console.WriteLine(currentSpeed);
         }
    }
    
    public void MakeNoise() {
        Console.WriteLine("");
    }
}

~~~


# Subclassing

Swift:

~~~
class Bicycle: Vehicle {
    var hasBasket = false
}
~~~

~~~
Bicycle().speed = 2.0

Seeting 2.0
Now 2.0
~~~

C#

~~~
public Bicycle : Vehcle {
   public bool hasBasket = false;
}
~~~

~~~
(new Bicycle()).Speed = 10.0


Setting10
now 10
~~~

# Overriding

Swift:

- override キーワード

C#:

- new
- virtual / override



## Accessing Superclass Methods, Properties, and Subscripts

Swift:

- super

C#:

- base


## Overriding Methods

Swift:

~~~
class Bicycle: Vehicle {
    var hasBasket = false
    override func makeNoise(){
       println("Choo Choo");  
    }   
}

Bicycle().makeNoise() 

Choo Choo

~~~

C#

~~~
public class Bicycle : Vehicle {
   public bool hasBasket = false;
    public new void MakeNoise() {
        Console.WriteLine("Choo Choo");
    }
}

(new Bicycle()).MakeNoise();

Choo Choo

~~~


## Overriding Properties


### Overriding Property Getters and Setters


Swift: get/setともにoverride必要

~~~
class Bicycle: Vehicle {
    override var speed: Double { 
        get { return currentSpeed + 0.1; }
        set { super.speed = newValue; }
    }
}

println(Bicycle().speed)
Bicycle().speed = 10.9


0.1
Seeting 10.9
Now 10.9
~~~

C#:

~~~
public class Bicycle : Vehicle {
   public bool hasBasket = false;
   public new double Speed {
         get { return currentSpeed + 0.1; }
         set { base.Speed = value ; }
   }
}

Console.WriteLine( (new Bicycle()).Speed );
(new Bicycle()).Speed  = 10.9

0.1
Setting10.9
now 10.9
~~~

C#: superclassでvirtual宣言するとsetをoverrideしなくていよい

~~~
public class Vehicle {

    public virtual double Speed{
         get { return currentSpeed ; }
         set { 
            Console.Write("Setting"); Console.WriteLine(value);
            currentSpeed = value; 
            Console.Write("now "); Console.WriteLine(currentSpeed);
         }
    }
}

public class Bicycle : Vehicle {
   public override double Speed {
         get { return currentSpeed + 0.1; }
   }
}

Console.WriteLine( (new Bicycle()).Speed );
(new Bicycle()).Speed  = 10.9

0.1
Setting10.9
now 10.9
~~~



### Overriding Property Observers


Swift:

~~~
class Car : Vehicle{
    override var currentSpeed: Double  {
         didSet {  println("Take care. \(currentSpeed)") }
    }   
}

Car().speed = 100.9
~~~

~~~
Seeting 100.9
Now 100.9
Take care. 100.9
~~~


# Preventing Overrides

Swift: final

- overrideしようとするとコンパイルエラー

    - final var
    - final func
    - final class func
    - final subscript
    
~~~
class Car : Vehicle{

    final override func makeNoise() {
        println("*****")
    }
}

final class ImportCar: Car { 
    override func makeNoise() {
        println("@@@@@@")
    }
} 

./test2.swift:38:19: error: instance method overrides a 'final' instance method
    override func makeNoise() {
~~~        
    
- サブクラスできない

    - final class
 
~~~
final class ImportCar: Car { } 
class AmericanCar: ImportCar { }


./test2.swift:35:7: error: inheritance from a final class 'ImportCar'
class AmericanCar: ImportCar { }
~~~ 

C# : sealed 

~~~
public class Car : Vehicle {
    sealed public override double Speed{
        get { return base.Speed ; }
    }
}

public class AutomaticCar: Car{
    public override double Speed{
        get { return base.Speed ; }
    }
}


(2,28): error CS0239: `AutomaticCar.Speed': cannot override inherited member `Car.Speed' because it is sealed
~~~

~~~
sealed public class Car : Vehicle {}

public class AutomaticCar: Car{}

(1,15): error CS0509: `AutomaticCar': cannot derive from sealed type `Car'
~~~
