- JsonConverter属性のフィールドにすると例外なので、とりあえずJTokenで受ける

~~~csharp
using System;
using System.IO;
using System.Collections.Generic;

using GeoAPI.Geometries;

using NetTopologySuite;
using NetTopologySuite.IO;
using NetTopologySuite.IO.Converters;
using NetTopologySuite.Geometries;

using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json.Converters;
using Newtonsoft.Json.Serialization;


public class BusStop
{
    public int id {get;set; }
    public string name {get;set;}

    public JToken location {get;set;}
    public JToken bus_area {get;set;}

    public Point Location
    {
        get {
            return new GeoJsonReader ().Read<Point>(location.ToString());
        }
    }
    public Polygon BusArea
    {
        get {
            return new GeoJsonReader ().Read<Polygon>(bus_area.ToString());
        }
    }
}

var json = File.ReadAllText("jinnan_po.json");
var jinnan_po = JsonConvert.DeserializeObject<BusStop>(json);

Console.WriteLine(jinnan_po.Location.ToString());
Console.WriteLine(jinnan_po.BusArea.ToString());
~~~
