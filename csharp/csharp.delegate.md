## delegate

~~~csharp
public class Sample 
{
   public delegate int Sum( int x, int y );

   public int RightSum(int x ,int y ){
        return x + y;
   }
   public int WrongSum(int x ,int y ){
        return x + y + 1;
   }
}

Sample.Sum s1 = (new Sample()).RightSum;
Sample.Sum s2 = (new Sample()).WrongSum;
Console.WriteLine(s1(3,4));
Console.WriteLine(s2(3,4));

7
8
~~~


## Action

Action 返り値がvoidのdelegate 

~~~ csharp
public class Machine
{
  public Action<string> trace {get;set;}

  public void Run(string data )
  {
     if(trace!=null) {
        trace(string.Format(
            "{0} {1}", data, DateTime.Now.ToString()));
     }   
  }
}

public class Man 
{
  string _job = "job";
  public Man(string job){ 
    _job = job;
  }
  
  public void Logger(string msg)
  {
    Console.WriteLine(string.Format(
        "{0}: {1}", _job, msg  )); 
  }
  public void Work()
  {
    var machine = new Machine{trace=this.Logger};
    for(int i=0; i < 5; i++ ){
        machine.Run(i.ToString());
    }   
  }
}

(new Man("Cook lunch")).Work();

~~~

~~~ csharp
$ csharp  sample.cs

Cook lunch: 0 id=7bc95ac9-cf46-4da2-bfbc-2f4633d02d7b
Cook lunch: 1 id=d8be8de4-6812-49af-8e76-78a57c916706
Cook lunch: 2 id=90378900-4ff8-4fd4-9bbb-4604c3f4ceab
Cook lunch: 3 id=a84a9558-4110-474f-bb0e-9b37a2b306ad
Cook lunch: 4 id=8a5dbdb4-1717-45fb-9a08-105c2dd87cb5
~~~

## Func

引数と返り値を定義できるデリゲート

~~~ csharp
Func<int,int,int> Sum =(int i, int j) => { return i + j ; }

var x = Sum;

Console.WriteLine( x(4,4) );

8
~~~


##  Predicate  

返り値がbooleanのデリゲート

~~~ csharp
public class PredicateSample
{
  public bool CanDrink(int age){
    return age >= 20;  
  }
}

Predicate<int>  a = (new PredicateSample()).CanDrink;
Console.WriteLine( a(19) );

False
~~~