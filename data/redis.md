# Redis


- [C# や PowerShell から　Redis を直接操作する RespClient というクライアント](http://tech.guitarrapc.com/entry/2014/09/01/073504)
- [redisドキュメント日本語訳](http://redis.shibu.jp/)

## Windows

- [Redis-64](https://gist.github.com/hdknr/ecf1cb51339d7447a19e)

~~~
C:¥> choco install redis-64
~~~

## StackExchange.Redis

- [github](https://github.com/StackExchange/StackExchange.Redis)

- [Azure Redis Cache でのデータのキャッシュ](https://msdn.microsoft.com/ja-jp/library/azure/dn690521.aspx)

### 組み込み

- [NuGet](https://www.nuget.org/packages/StackExchange.Redis/)
- packages.config

~~~xml
<?xml version="1.0" encoding="utf-8"?>
<packages>
  <package id="StackExchange.Redis" 
  	version="1.0.414" targetFramework="net45" />
</packages>
~~~

- サンプル

~~~csharp
namespace AppSupport
{
    public class State
    {
        public static StackExchange.Redis.IDatabase Database(string connection)
        {
            var connect = StackExchange.Redis.ConnectionMultiplexer.Connect(connection);
            var cb = connect.GetDatabase();  // StackExchange.Redis.IDatabase
            return cb;
        }
        public static void Set(string key, string value, string connection="localhost")
        {
            Database(connection).StringSet(key, value);
        }

        public static string Get(string key, string connection="localhost")
        {
            return Database(connection).StringGet(key);
        }

        public static void Add(string key, string value
            string connection="localhost")
        {
        	  // Set
            Database(connection).SetAdd(key, value);
        }
    }
}
~~~

### BookSleeve

- [C#のRedisライブラリ「BookSleeve」の利用法](http://www.buildinsider.net/small/rediscshap/01)
- [RxとRedisを用いたリモートPub/Sub通信](http://neue.cc/2013/04/24_404.html)


## Debian

~~~
vagrant@jessie:~$ sudo apt-get install redis-tools
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following extra packages will be installed:
  libjemalloc1
The following NEW packages will be installed:
  libjemalloc1 redis-tools
0 upgraded, 2 newly installed, 0 to remove and 0 not upgraded.
Need to get 168 kB of archives.
After this operation, 543 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
~~~

## 操作

- キーの一覧

~~~
> keys *
~~~
