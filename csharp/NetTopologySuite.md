NetTopologySuite: GeoJSONを読んでみる


- [scriptcs](http://bitly.com/hdknr_scriptcs) インストールされていること

## NetTopologySuite

- NetTopologySuite (+GeoAPI)

~~~bash
$ scriptcs  -install  NetTopologySuite
Installing packages...
Installed: NetTopologySuite
Package installation succeeded.
Saving packages in scriptcs_packages.config...
Creating scriptcs_packages.config...
Added GeoAPI (v1.7.4, .NET 4.5) to scriptcs_packages.config
Added NetTopologySuite (v1.14, .NET 4.5) to scriptcs_packages.config
Successfully updated scriptcs_packages.config.
~~~

- NetTopologySuite.IO.GeoJSON

~~~bash
$ scriptcs  -install  NetTopologySuite.IO.GeoJSON
Installing packages...
Installed: NetTopologySuite.IO.GeoJSON
Package installation succeeded.
Saving packages in scriptcs_packages.config...
Updating scriptcs_packages.config...
Skipped GeoAPI because it already exists.
Skipped NetTopologySuite because it already exists.
Added NetTopologySuite.IO.GeoJSON (v1.14, .NET 4.5) to scriptcs_packages.config
Added Newtonsoft.Json (v8.0.2, .NET 4.5) to scriptcs_packages.config
Successfully updated scriptcs_packages.config.
~~~

## GeoJSON

- test.cs (Point)

~~~csharp
using System;

using NetTopologySuite.IO;
using NetTopologySuite.Geometries;

var reader = new GeoJsonReader ();
var json = @"{""type"": ""Point"", ""coordinates"": [-122.402, 37.7976983333333]}";
var obj = reader.Read<Point> (json);
Console.WriteLine(obj.ToString());
~~~

~~~bash
$ scriptcs test.cs
POINT (-122.402 37.7976983333333)
~~~

- PolygonにPointが入っているか判定

~~~csharp
var reader = new GeoJsonReader ();

var area = reader.Read<Polygon> (
    File.ReadAllText("shibuya.json"));

var locations = new Dictionary<string, string>{
  {"西日暮里", @"{""type"": ""Point"", ""coordinates"": [139.7691960797771, 35.73323451860732]}" },
  {"ハチ公前", @"{""type"": ""Point"", ""coordinates"": [139.7003236463392, 35.65870361613276]}" },
};

foreach(var location in locations){
    Console.Write(location.Key + ":");
    Console.WriteLine(
        area.Contains(reader.Read<Point> (location.Value)));
}
~~~

~~~bash
$ scriptcs test.cs 
西日暮里:False
ハチ公前:True
~~~


## GeometryConverter: デシリアライズ


~~~bash
using NetTopologySuite.IO.Converters;
using NetTopologySuite.Geometries;

using Newtonsoft.Json;
using Newtonsoft.Json.Converters;


namespace WalkAround.Droid
{	
	
	public class BusStop
	{
		public int id {get;set; }
		public string name {get;set;}

		[JsonConverter(typeof(GeometryConverter))]
		public Point location {get;set;}

		[JsonConverter(typeof(GeometryConverter))]
		public Polygon bus_area {get;set;}

		public static BusStop Deserialize(string json)
		{
			return JsonConvert.DeserializeObject<BusStop> (json);
		}
	}
}
~~~

### iOS, scriptcs で動かない

- Androidエミュレータでは動いているが、scriptcs だとエラーになっている

~~~
ERROR: Script execution failed. [JsonException] Error creating 'NetTopologySuite.IO.Converters.GeometryConverter'.

=== INNER EXCEPTION ===
[System.InvalidCastException] Specified cast is not valid.
  at Newtonsoft.Json.Serialization.JsonTypeReflector+<>c__DisplayClass18_0.<GetJsonConverterCreator>b__0 (System.Object[] parameters) <0x40173d0 + 0x0025f> in <filename unknown>:0 

~~~

- iOSでも例外

~~~
System.TypeLoadException: 
  Could not load type NetTopologySuite.IO.Converters.GeometryConverter, 
    NetTopologySuite.IO.GeoJSON, Version=1.14.0.0, Culture=neutral, PublicKeyToken=null while decoding custom attribute
~~~

- とりあえず動かす

~~~csharp

	public class Station
	{
		public int id {get;set; }
		public string name {get;set;}
		public JToken location {get;set; }
		public JToken area {get;set; }

		public static Station Deserialize(string json)
		{
			return JsonConvert.DeserializeObject<Station> (json);
		}
			
		[JsonIgnore]
		public Point Location 
		{
			get{
				var reader = new GeoJsonReader ();
				eturn reader.Read<Point> (location.ToString ());
			}
		}

		[JsonIgnore]
		public Polygon Area 
		{
			get{
				var reader = new GeoJsonReader ();
				return reader.Read<Polygon> (area.ToString ());
			}
		}
	}
~~~
