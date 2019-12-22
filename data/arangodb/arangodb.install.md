# Install

## Ubuntu

- [How to Install ArangoDB on Ubuntu 18.04 Bionic Beaver](https://computingforgeeks.com/how-to-install-arangodb-on-ubuntu-18-04/)

~~~bash
$ echo 'deb https://download.arangodb.com/arangodb34/DEBIAN/ /' | sudo tee /etc/apt/sources.list.d/arangodb.list
.
~~~

~~~bash
$ wget -q https://download.arangodb.com/arangodb34/DEBIAN/Release.key -O- | sudo apt-key add -
.
~~~

~~~bash
$ sudo apt update
$ sudo apt -y install apt-transport-https arangodb3
.
password:...
~~~

Choose the database storage engine to use.: `auto`
パスワード忘れたたら:

~~~bash
$ arango-secure-installation
.
~~~

~~~bash
$ sudo systemctl start arangodb3
.
~~~

~~~bash
$ sudo systemctl enable arangodb3
Synchronizing state of arangodb3.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable arangodb3
~~~

~~~bash
$ systemctl status arangodb3
● arangodb3.service - ArangoDB database server
   Loaded: loaded (/lib/systemd/system/arangodb3.service; enabled; vendor preset: enabled)
   Active: active (running) since Sat 2019-10-12 23:14:34 JST; 5min ago
 Main PID: 12105 (arangod)
    Tasks: 19 (limit: 131072)
   CGroup: /system.slice/arangodb3.service
           └─12105 /usr/sbin/arangod --uid arangodb --gid arangodb --pid-file /var/run/arangodb3/arangod.pid --temp.path /var/tmp/ara
~~~

~~~bash
$ sudo lsof -c arango | grep TCP

arangod 12105 arangodb   28u     IPv4              79957      0t0    TCP localhost:8529 (LISTEN)
~~~

~~~bash
$ sudo arangosh
Please specify a password: graph*****

                                       _     
  __ _ _ __ __ _ _ __   __ _  ___  ___| |__  
 / _` | '__/ _` | '_ \ / _` |/ _ \/ __| '_ \ 
| (_| | | | (_| | | | | (_| | (_) \__ \ | | |
 \__,_|_|  \__,_|_| |_|\__, |\___/|___/_| |_|
                       |___/                 

arangosh (ArangoDB 3.4.8 [linux] 64bit, 
using jemalloc, build tags/v3.4.8-0-g0952837c2a, 
VPack 0.1.33, RocksDB 5.16.0, ICU 58.1, V8 5.7.492.77, OpenSSL 1.1.0k  28 May 2019)
Copyright (c) ArangoDB GmbH

Command-line history will be persisted when the shell is exited.
Connected to ArangoDB 'http+tcp://127.0.0.1:8529' version: 3.4.8 [SINGLE, server], 
database: '_system', username: 'root'

Type 'tutorial' for a tutorial or 'help' to see common examples
127.0.0.1:8529@_system> 
~~~
