~~~
$ curl http://europa.eu/rapid/conf/RSS20.xsd -o rss.xsd
$ xsd rss.xsd /c:Rss
Written file ./rss.cs
$ mv rss.cs rss.csx
~~~

~~~
$ scriptcs -i FubarCoder.RestSharp.Portable.HttpClient
~~~
