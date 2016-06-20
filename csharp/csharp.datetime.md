## 文字列書式

- [カスタム時間間隔書式指定文字列](https://msdn.microsoft.com/ja-jp/library/ee372287(v=vs.110).aspx)

~~~
> DateTime.Now.ToString()
2016/03/30 16:10:15

> DateTime.Now.ToString("F")
2016年3月30日 16:09:55
~~~


## ParseExact

~~~cs
csharp> DateTime.ParseExact("10:00:00", "HH:mm:ss", System.Globalization.CultureInfo.InvariantCulture, System.Globalization.DateTimeStyles.AdjustToUniversal)         

2016/06/13 10:00:00  
~~~
