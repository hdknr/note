foreach(var i in 
    Enumerable.Range(1, 10)
    .Where( x => x % 2 == 0)
    .Select( x => x * x )){

    Console.WriteLine(i);
}

using System.Reactive.Linq;

Observable.Range(1, 10)
    .Where( x => x % 2 == 0)
    .Select( x => x * x )
    .Subscribe( 
        i => { Console.WriteLine(i); },
        ex => { Console.WriteLine("Error {0}", ex.Message);},
        () => { Console.WriteLine("End");}
    );
