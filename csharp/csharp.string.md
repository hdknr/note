# $ 補間文字列

- [Interpolated Strings (C# and Visual Basic Reference) ](https://msdn.microsoft.com/en-us/library/dn961160.aspx)
- [What's with the dollar sign ($“string”) [duplicate]](http://stackoverflow.com/questions/32878549/whats-with-the-dollar-sign-string)

~~~csharp
> var dt = DateTime.Now
> Console.WriteLine($"{dt.Hour}");  
15
> Console.WriteLine($"{DateTime.Now.Hour}");
15
~~~
