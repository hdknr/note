
- [Doc](http://glances.readthedocs.org/en/latest/glances-doc.html)

## install

~~~
$ pip install glances

Collecting glances
  Downloading Glances-2.5.1.tar.gz (5.8MB)
    100% |████████████████████████████████| 5.8MB 30kB/s
Collecting psutil>=2.0.0 (from glances)
  Downloading psutil-3.2.2.tar.gz (253kB)
    100% |████████████████████████████████| 253kB 549kB/s
Building wheels for collected packages: glances, psutil
  Running setup.py bdist_wheel for glances
  Stored in directory: /home/vagrant/.cache/pip/wheels/cd/fa/0d/53fab06a888b6b7a22a629a3ccfc3ef6dfa3265adc77c63733
  Running setup.py bdist_wheel for psutil
  Stored in directory: /home/vagrant/.cache/pip/wheels/e8/0b/67/398f808676bf695cc083cf7237ef4499bd8fd27dbd3f3a07fe
Successfully built glances psutil
Installing collected packages: psutil, glances
Successfully installed glances-2.5.1 psutil-3.2.2
~~~

## Web Server Mode

~~~
$ glances -w
Bottle module not found. Glances cannot start in web server mode.
~~~

~~~
$ pip install bottle
Collecting bottle
  Downloading bottle-0.12.9.tar.gz (69kB)
    100% |████████████████████████████████| 69kB 1.5MB/s
Building wheels for collected packages: bottle
  Running setup.py bdist_wheel for bottle
  Stored in directory: /home/vagrant/.cache/pip/wheels/0f/bd/f7/21e856551fa937e3c8a9d9592fd74a50714af336b8ee4f42c7
Successfully built bottle
Installing collected packages: bottle
Successfully installed bottle-0.12.9
~~~

~~~
$ glances -w
Glances web server started on http://0.0.0.0:61208/
~~~

##　Graphite

- [graphite-project/graphite-web](https://github.com/graphite-project/graphite-web)
- [Graphite](http://graphite.readthedocs.org/en/latest/index.html)
- [Python Statds](http://statsd.readthedocs.org/en/v3.1/index.html)
- [Getting Started with Monitoring using Graphite](http://www.infoq.com/articles/graphite-intro)
- [graphite, grafana, sitespeed.io, diamond で継続 Web パフォーマンスモニタリング](http://qiita.com/Jxck_/items/abfa9f3dd15c5572cbfd)
- [Mackerelを支える時系列データベース技術](http://yuuki.hatenablog.com/entry/high-performance-graphite)
- [dstat + fluentd + Graphite + Grafana でサーバモニタリングする](http://blog.nomadscafe.jp/2014/04/dstat-fluentd-graphite-grafana.html)
- [検証環境をささっと構築する](http://blog.wnotes.net/blog/article/graphite-grafana-sitespeedio-perf-monitoring)

### 関連

- [Diamond](https://github.com/python-diamond/Diamond) (DiamondデーモンでメトリックスをGraphiteに集めて、Grapfana 使って表示させる)
- [collectd](http://collectd.org/)
- [sensu](https://github.com/sensu)
