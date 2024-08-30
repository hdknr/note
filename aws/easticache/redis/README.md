# Redis

- [C# や PowerShell から　Redis を直接操作する RespClient というクライアント](http://tech.guitarrapc.com/entry/2014/09/01/073504)
- [redisドキュメント日本語訳](http://redis.shibu.jp/)

## Windows

- [Redis-64](https://gist.github.com/hdknr/ecf1cb51339d7447a19e)

~~~ps
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

~~~
$ sudo apt-get install redis-server
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  redis-server
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 308 kB of archives.
After this operation, 873 kB of additional disk space will be used.
Get:1 http://security.debian.org/ jessie/updates/main redis-server amd64 2:2.8.17-1+deb8u1 [308 kB]
Fetched 308 kB in 6s (46.0 kB/s)                                                                                                                      
Selecting previously unselected package redis-server.
(Reading database ... 70513 files and directories currently installed.)
Preparing to unpack .../redis-server_2%3a2.8.17-1+deb8u1_amd64.deb ...
Unpacking redis-server (2:2.8.17-1+deb8u1) ...
Processing triggers for systemd (215-17+deb8u1) ...
Processing triggers for man-db (2.7.0.2-5) ...
Setting up redis-server (2:2.8.17-1+deb8u1) ...
adduser: Warning: The home directory `/var/lib/redis' does not belong to the user you are currently creating.
Processing triggers for systemd (215-17+deb8u1) ...
~~~

- サーバー起動

~~~
s$ redis-server
[4326] 23 Jul 05:54:02.855 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 2.8.17 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                   
 (    '      ,       .-`  | `,    )     Running in stand alone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 4326
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           http://redis.io        
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

[4326] 23 Jul 05:54:02.864 # Server started, Redis version 2.8.17
[4326] 23 Jul 05:54:02.864 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
[4326] 23 Jul 05:54:02.865 * The server is now ready to accept connections on port 6379
~~~

## 操作

- キーの一覧

~~~
> keys *
~~~

## CentOS

~~~
sudo rpm --import http://vault.centos.org/RPM-GPG-KEY-CentOS-6
~~~

~~~~
$ sudo rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm
http://rpms.famillecollet.com/enterprise/remi-release-6.rpm を取得中
警告: /var/tmp/rpm-tmp.FXV2fA: ヘッダ V3 DSA/SHA1 Signature, key ID 00f97f56: NOKEY
エラー: 依存性の欠如:
        epel-release >= 6 は remi-release-6.6-1.el6.remi.noarch に必要とされています
~~~

~~~
$ sudo rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm を取得中
警告: /var/tmp/rpm-tmp.IKUE9R: ヘッダ V3 RSA/SHA256 Signature, key ID 0608b895: NOKEY
準備中...                ########################################### [100%]
~~~

~~~
$ sudo rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm                                                 
http://rpms.famillecollet.com/enterprise/remi-release-6.rpm を取得中
警告: /var/tmp/rpm-tmp.xEpijT: ヘッダ V3 DSA/SHA1 Signature, key ID 00f97f56: NOKEY
準備中...                ########################################### [100%]
   1:remi-release           ########################################### [100%]
~~~     

~~~
$ sudo yum --enablerepo=remi install redis
....

パッケージをダウンロードしています:
(1/2): jemalloc-3.6.0-1.el6.x86_64.rpm                             | 100 kB     00:00     
(2/2): redis-3.0.5-1.el6.remi.x86_64.rpm                           | 438 kB     00:00     
------------------------------------------------------------------------------------------
合計                                                      577 kB/s | 538 kB     00:00     
警告: rpmts_HdrFromFdno: ヘッダ V3 RSA/SHA256 Signature, key ID 0608b895: NOKEY
Retrieving key from file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6
Importing GPG key 0x0608B895:
 Userid : EPEL (6) <epel@fedoraproject.org>
 Package: epel-release-6-8.noarch (installed)
 From   : /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6
これでいいですか? [y/N]y
warning: rpmts_HdrFromFdno: Header V3 DSA/SHA1 Signature, key ID 00f97f56: NOKEY
Retrieving key from file:///etc/pki/rpm-gpg/RPM-GPG-KEY-remi
Importing GPG key 0x00F97F56:
 Userid : Remi Collet <RPMS@FamilleCollet.com>
 Package: remi-release-6.6-1.el6.remi.noarch (installed)
 From   : /etc/pki/rpm-gpg/RPM-GPG-KEY-remi
これでいいですか? [y/N]y
rpm_check_debug を実行しています
トランザクションのテストを実行しています
トランザクションのテストを成功しました
トランザクションを実行しています
...
警告: RPMDB は yum 以外で変更されました。
  インストールしています  : jemalloc-3.6.0-1.el6.x86_64                               1/2
  インストールしています  : redis-3.0.5-1.el6.remi.x86_64                             2/2
  Verifying               : jemalloc-3.6.0-1.el6.x86_64                               1/2
  Verifying               : redis-3.0.5-1.el6.remi.x86_64                             2/2

インストール:
  redis.x86_64 0:3.0.5-1.el6.remi                                                         

依存性関連をインストールしました:
  jemalloc.x86_64 0:3.6.0-1.el6                                                           

完了しました!
~~~~

~~~
$ sudo /etc/init.d/redis start
redis-server を起動中:                                     [  OK  ]
~~~

~~~
]$ redis-cli
127.0.0.1:6379>
~~~

~~~
$ sudo lsof -i:6379
COMMAND     PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
redis-ser 41695 redis    4u  IPv4 315652      0t0  TCP localhost:6379 (LISTEN)
~~~~

## コマンド

- [コマンドリファレンス](http://redis.shibu.jp/commandreference/)

- キー一覧

~~~
127.0.0.1:6379> keys *
~~~

- 絞る

~~~
$ redis-cli keys "const*"
1) "constance:THE_ANSWER"
~~~

- 値

~~~
$ redis-cli get "constance:THE_ANSWER"
"I50\n."
~~~

## 記事

- [Redisでデータベースを切り替える方法](https://blog.shimar.me/2016/11/20/redis-select-database) (`-n` オプション, `SELECT {n}`)
