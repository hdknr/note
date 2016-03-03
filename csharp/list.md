- http://stackoverflow.com/questions/4460106/how-do-access-previous-item-in-list-using-linq


# Skip, Zipをつかって、Location間の中間点のリストを作る

~~~csharp
using System.Collections.Generic;
using System.Linq;

public class Location
{
    public Location(int x, int y){
        X = x;
        Y = y;
    }   
    public int X {get; set; }
    public int Y {get; set; }
    public override string ToString(){
        return string.Format("({0}, {1})", X, Y);
    }   
}

var list = Enumerable.Range(1, 10)
    .Select(i => new Location(i * 100, i * 100))
    .ToList<Location>();

foreach(var i in list){
    Console.WriteLine(i.ToString());
}

var list2 = list.Skip(1)        // １つずらしたListを作る
    .Zip(list, (cur, prev)      // 元の配列とZipする
        => new Location(        // ２点の中間点を作る
            (prev.X + cur.X)/2,
            (prev.Y + cur.Y)/2))
    .ToList();

foreach(var i in list2){
    Console.WriteLine(i.ToString());
}
~~~
