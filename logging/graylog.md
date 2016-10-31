gralylog

## 導入

- [インストール](http://docs.graylog.org/en/latest/pages/installation/operating_system_packages.html)
- [Debian](http://docs.graylog.org/en/latest/pages/installation/os/debian.html)
- [Ubuntu](http://docs.graylog.org/en/latest/pages/installation/os/ubuntu.html)
- [Javaのバージョン/mongodbのジャーナルスペース](https://github.com/hdknr/scriptogr.am/issues/22)


### 準備

~~~bash
$ sudo  apt-get install mongodb-server
~~~

~~~bash
$ dpkg -l | grep elas
ii  elasticsearch                        2.4.0                                all          Elasticsearch is a distributed RESTful search engine built for the cloud. Reference documentation can be found at https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html and the 'Elasticsearch: The Definitive Guide' book can be found at https://www.elastic.co/guide/en/elasticsearch/guide/current/index.html
~~~

~~~bash
$ sudo grep cluster.name /etc/elasticsearch/elasticsearch.yml
# cluster.name: my-application
$ sudo vim /etc/elasticsearch/elasticsearch.yml
$ sudo grep cluster.name /etc/elasticsearch/elasticsearch.yml
# cluster.name: my-application
cluster.name: graylog

~~~

~~~bash
$ sudo systemctl daemon-reload
$ sudo systemctl enable elasticsearch.service
$ sudo systemctl restart elasticsearch.service
~~~

### インストール

~~~bash
$ sudo apt-get install apt-transport-https
$ wget https://packages.graylog2.org/repo/packages/graylog-2.1-repository_latest.deb
$ sudo dpkg -i graylog-2.1-repository_latest.deb
$ sudo apt-get update
$ sudo apt-get install graylog-server
~~~


~~~bash
[WARNING] uuidgen not available! Please execute 'uuidgen > /etc/graylog/server/node-id' once its installed.
################################################################################
Graylog does NOT start automatically!

Please run the following commands if you want to start Graylog automatically on system boot:

    sudo systemctl daemon-reload
    sudo systemctl enable graylog-server.service

    sudo systemctl start graylog-server.service

################################################################################
systemd (215-17+deb8u4) のトリガを処理しています ...
~~~

~~~bash
$ ls /etc/graylog/server
log4j2.xml  server.conf
~~~

~~~bash
$ sudo apt-get install uuid-runtime -y

$ uuidgen  | sudo tee /etc/graylog/server/node-id
14c45bab-7447-4d94-88d3-64f3fc28f37f
~~~

~~~bash
$ sudo systemctl daemon-reload

$ sudo systemctl enable graylog-server.service
Synchronizing state for graylog-server.service with sysvinit using update-rc.d...
Executing /usr/sbin/update-rc.d graylog-server defaults
Executing /usr/sbin/update-rc.d graylog-server enable
Created symlink from /etc/systemd/system/multi-user.target.wants/graylog-server.service to /usr/lib/systemd/system/graylog-server.service.

$ sudo systemctl start graylog-server.service

$ sudo /etc/init.d/graylog-server start
[ ok ] Starting graylog-server (via systemctl): graylog-server.service.
~~~


- パスワード最低16文字

~~~bash
$ echo -n graylog2016@localhost | sha256sum
227864b78a71a79cc93aada69319624908487a5231bee80f802cae24c6d5f348  -
~~~

~~~bash
$ sudo grep pass /etc/graylog/server/server.conf | grep -v "^#"
password_secret = graylog2016@localhost
root_password_sha2 = 227864b78a71a79cc93aada69319624908487a5231bee80f802cae24c6d5f348
~~~


## 管理

~~~bash
$ sudo lsof -i:9000
COMMAND   PID    USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
java    22915 graylog   65u  IPv6 532677      0t0  TCP localhost:9000 (LISTEN)
~~~

~~~bash
$ sudo vim /etc/graylog/server/server.conf
$ grep ^web_listen_uri /etc/graylog/server/server.conf
web_listen_uri = http://0.0.0.0:9000/

~~~
