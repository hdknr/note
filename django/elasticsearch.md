# Elasticsearch

- https://www.elastic.co/

## インストール

- [Repositories](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-repositories.html)

### Debian Jessie

~~~bash
$ wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
OK

$ echo "deb https://packages.elastic.co/elasticsearch/2.x/debian stable main" | sudo tee -a /etc/apt/sources.list.d/elasticsearch-2.x.list
deb https://packages.elastic.co/elasticsearch/2.x/debian stable main
~~~

~~~bash
$ sudo apt-get install apt-transport-https
$ sudo apt-get update
$ sudo apt-get install elasticsearch
~~~

#### Java

- [Easy install for elasticsearch on Ubuntu 14.04](https://gist.github.com/Globegitter/662713f90d5af5b4269d)
- [How to install OpenJDK 8 on 14.04 LTS?](http://askubuntu.com/questions/464755/how-to-install-openjdk-8-on-14-04-lts)

~~~bash
$ sudo apt-get install openjdk-8-jre-headless -y
~~~

#### SysVInit

~~~bash
$ sudo update-rc.d elasticsearch defaults 95 10
~~~

~~~bash
$ sudo /etc/init.d/elasticsearch restart
[ ok ] Restarting elasticsearch (via systemctl): elasticsearch.service.
~~~

~~~bash
$ sudo lsof -u elasticsearch | grep TCP
java    2106 elasticsearch   90u  IPv6            1742943      0t0     TCP localhost:9300 (LISTEN)
java    2106 elasticsearch   92u  IPv6            1742946      0t0     TCP localhost:9300 (LISTEN)
java    2106 elasticsearch  102u  IPv6            1743003      0t0     TCP localhost:9200 (LISTEN)
java    2106 elasticsearch  103u  IPv6            1743004      0t0     TCP localhost:9200 (LISTEN)
~~~

~~~bash
$ curl -XGET http://localhost:9200/
{
  "name" : "Coach",
  "cluster_name" : "elasticsearch",
  "version" : {
    "number" : "2.3.2",
    "build_hash" : "b9e4a6acad4008027e4038f6abed7f7dba346f94",
    "build_timestamp" : "2016-04-21T16:03:47Z",
    "build_snapshot" : false,
    "lucene_version" : "5.5.0"
  },
  "tagline" : "You Know, for Search"
}
~~~

## head プラグイン

- A web front end for an elastic search cluster http://mobz.github.io/elasticsearch-head/
- https://github.com/mobz/elasticsearch-head

~~~bash
$ sudo /usr/share/elasticsearch/bin/plugin install mobz/elasticsearch-head

-> Installing mobz/elasticsearch-head...
Trying https://github.com/mobz/elasticsearch-head/archive/master.zip ...
Downloading .............. DONE
Verifying https://github.com/mobz/elasticsearch-head/archive/master.zip checksums if available ...
NOTE: Unable to verify checksum for downloaded plugin (unable to find .sha1 or .md5 file to verify)
Installed head into /usr/share/elasticsearch/plugins/head
~~~

- [基本設定](http://sebrain.web.fc2.com/document/0064.html)

~~~bash
$ sudo vi /etc/elasticsearch/elasticsearch.yml
$ sudo grep ^network.host /etc/elasticsearch/elasticsearch.yml

network.host: 0.0.0.0
~~~


~~~bash
$ sudo /etc/init.d/elasticsearch restart
[ ok ] Restarting elasticsearch (via systemctl): elasticsearch.service.
~~~

~~~bash
$ sudo lsof -u elasticsearch | grep TCP                                                                           
java    3829 elasticsearch   90u  IPv6            1749725      0t0     TCP *:9300 (LISTEN)
java    3829 elasticsearch  101u  IPv6            1749766      0t0     TCP *:9200 (LISTEN)
~~~

- ブラウザでフロントエンドUIにアクセス

~~~bash
$ curl http://wp.deb:9200/_plugin/head/
<!DOCTYPE html>

<html>
        <head>
                <meta charset="UTF-8">
                <title>elasticsearch-head</title>
                <link rel="stylesheet" href="base/reset.css">
                <link rel="stylesheet" href="vendor.css">
                <link rel="stylesheet" href="app.css">
                <script src="i18n.js" data-baseDir="lang" data-langs="en,fr,pt,zh"></script>
                <script src="vendor.js"></script>
                <script src="app.js"></script>
                <script>
                        window.onload = function() {
                                if(location.href.contains("/_plugin/")) {
                                        var base_uri = location.href.replace(/_plugin\/.*/, '');
                                }
                                var args = location.search.substring(1).split("&").reduce(function(r, p) {
                                        r[decodeURIComponent(p.split("=")[0])] = decodeURIComponent(p.split("=")[1]); return r;
                                }, {});
                                new app.App("body", {
                                        id: "es",
                                        base_uri: args["base_uri"] || base_uri,
                                        auth_user : args["auth_user"] || "",
                                        auth_password : args["auth_password"],
                                        dashboard: args["dashboard"]
                                });
                        };
                </script>
                <link rel="icon" href="base/favicon.png" type="image/png">
        </head>
        <body></body>
</html>
~~~

## kuromoji プラグイン

- [Japanese (kuromoji) Analysis Plugin](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-kuromoji.html)
- [Haystack + Elasticsearch + kuromoji コトハジメ](https://gist.github.com/voluntas/6739918)
- [Elasticsearch に kuromoji を入れて日本語全文検索をする](http://qiita.com/mserizawa/items/8335d39cacb87f12b678)
- [Elasticsearchとkuromojiでちゃんとした日本語全文検索をやるメモ](http://tech.gmo-media.jp/post/70245090007/elasticsearch-kuromoji-japanese-fulltext-search)

~~~bash
$ sudo /usr/share/elasticsearch/bin/plugin install analysis-kuromoji

-> Installing analysis-kuromoji...
Trying https://download.elastic.co/elasticsearch/release/org/elasticsearch/plugin/analysis-kuromoji/2.3.2/analysis-kuromoji-2.3.2.zip ...
Downloading ............DONE
Verifying https://download.elastic.co/elasticsearch/release/org/elasticsearch/plugin/analysis-kuromoji/2.3.2/analysis-kuromoji-2.3.2.zip checksums if available ...
Downloading .DONE
Installed analysis-kuromoji into /usr/share/elasticsearch/plugins/analysis-kuromoji
~~~

~~~bash
$ sudo /etc/init.d/elasticsearch restart
~~~

~~~bash
$ curl -X GET 'http://localhost:9200/_nodes/plugins' | jq ".nodes[].plugins[]"
~~~

~~~javascript
{
  "name": "analysis-kuromoji",
  "version": "2.3.2",
  "description": "The Japanese (kuromoji) Analysis plugin integrates Lucene kuromoji analysis module into elasticsearch.",
  "jvm": true,
  "classname": "org.elasticsearch.plugin.analysis.kuromoji.AnalysisKuromojiPlugin",
  "isolated": true,
  "site": false
}
{
  "name": "head",
  "version": "master",
  "description": "head - A web front end for an elastic search cluster",
  "url": "/_plugin/head/",
  "jvm": false,
  "site": true
}
~~~

~~~bash 
$ sudo vi /etc/elasticsearch/elasticsearch.yml

$ sudo tail  /etc/elasticsearch/elasticsearch.yml

# ########
# Kuromoji
index.analysis.analyzer.default.type: custom
index.analysis.analyzer.default.tokenizer: kuromoji_tokenizer

~~~

~~~bash
$ sudo /etc/init.d/elasticsearch restart
[ ok ] Restarting elasticsearch (via systemctl): elasticsearch.service.
~~~

- データ投入

~~~bash
$ curl -X POST http://localhost:9200/wine/sample/_bulk --data-binary @wine.json  
~~~

- クエリ

~~~bash
$ curl -X GET http://localhost:9200/wine/sample/_search -d '{"query":{"match":{"description":"渋め"}}}' 
~~~

## python / Django

- [Django から Elasticsearch を使う](http://qiita.com/Fq4X/items/81ba2f234e9611546025)
- [Django + Haystack + Elasticsearch コトハジ](https://gist.github.com/voluntas/21759d5c45aacc0e6656/)
- [pythonクライアントで始める「はじめてのElasticsearch」](http://qiita.com/ikawaha/items/c654f746cfe76b888a27)

### PYPI elasticsearch :Python Elasticsearch Client

- https://pypi.python.org/pypi/elasticsearch/2.3.0
- http://elasticsearch-py.readthedocs.io/en/master/

~~~bash
$ pip install elasticsearch
~~~

~~~python
In [1]: from elasticsearch import Elasticsearch
In [2]: es = Elasticsearch("localhost:9200")
In [4]: es
Out[4]: <Elasticsearch([{u'host': u'localhost', u'port': 9200}])>
In [5]: res = es.search(index='wine', body={"query": {"match":{"description":"渋め"}}})
In [8]: for hit in res['hits']['hits']:
   ...:     print hit['_source']['name']
   ...:     
カベルネ・ソーヴィニヨン
ピノ・ノワール
~~~

# AWS

- [Amazon Elasticsearch Service](https://aws.amazon.com/jp/elasticsearch-service/)
- [Amazon Elasticsearch Serviceでkuromojiを使って日本語全文検索する](http://dev.classmethod.jp/cloud/aws/using-kuromoji-on-amazon-es/)

- Amazon ESとしてはプラグインの追加機能が提供されていないため、最初からKuromojiが含まれているのは、日本においてはすごく重要です。
