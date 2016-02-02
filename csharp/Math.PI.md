# PI
~~~csharp
using System;

// 180度 :  1π  
var n = Math.Atan(1.0);
Console.WriteLine(n);
Console.WriteLine(n * 180 / Math.PI);
~~~

~~~
0.785398163397448
45
~~~


# ある点を中心に指定した角度をずらしたところの点を求める

- [Rotate a point around another point](http://stackoverflow.com/questions/13695317/rotate-a-point-around-another-point)

~~~csharp
using System;

public class Point{

    public Point(){ X=0; Y = 0; }
    public Point(int x , int y) { X = x; Y = y; }

    public int X {get;set; }
    public int Y {get;set; }

    public override string ToString()
    {
        return string.Format("({0}, {1})", X, Y);
    }

    public Point RotatePoint(Point other, double angleInDegrees)
    {
        double angleInRadians = angleInDegrees * (Math.PI / 180);
        double cosTheta = Math.Cos(angleInRadians);
        double sinTheta = Math.Sin(angleInRadians);
        return new Point
        {
            X =
                (int)
                (cosTheta * (other.X - this.X) -
                sinTheta * (other.Y - this.Y) + this.X),
            Y =
                (int)
                (sinTheta * (other.X - this.X) +
                cosTheta * (other.Y - this.Y) + this.Y)
        };
    }
}

var center = new Point(0, 0);
var blue = new Point(100, 0);
Console.WriteLine(center.RotatePoint(blue, 45).ToString());
Console.WriteLine(center.RotatePoint(blue, 90).ToString());
Console.WriteLine(center.RotatePoint(blue, 180).ToString());
Console.WriteLine(center.RotatePoint(blue, 360).ToString());

~~~

~~~
(70, 70)
(0, 100)
(-100, 0)
(100, 0)
~~~
