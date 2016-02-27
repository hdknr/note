- [JavaScript の Date は罠が多すぎる](http://qiita.com/labocho/items/5fbaa0491b67221419b4)
- Date.parse が返すのは Date でなく整数

~~~js
> var a = "2016-01-01T03:00:00Z";
undefined
> Date.parse(a)
1451617200000
> new Date(a)
Fri Jan 01 2016 03:00:00 GMT+0000 (UTC)
~~~
