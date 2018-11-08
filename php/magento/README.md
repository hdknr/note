- [Install by cloning repositories | Magento 2 Developer Documentation](https://devdocs.magento.com/guides/v2.0/install-gde/install/web/install-web-sample-data-clone.html)
- [nginx | Magento 2 Developer Documentation](https://devdocs.magento.com/guides/v2.0/install-gde/prereq/nginx.html)
- [Magento2 インストール(開発者向け) - とみぞーノート](http://wiki.bit-hive.com/tomizoo/pg/Magento2%20%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%28%E9%96%8B%E7%99%BA%E8%80%85%E5%90%91%E3%81%91%29)

## その他

- [EC-CUBE1系・2系・3系・4系の違い - Qiita](https://qiita.com/nanasess/items/dc8407c48a3dcf982ea2)
- [EC-CUBE 4.0（旧3.n）インストール - Qiita](https://qiita.com/nekyo/items/0c9d5b57390cd9a029ec)

## tarball からインストール

~~~bash 
$ wget https://github.com/magento/magento2/archive/2.2.6.tar.gz
$ tar xfz 2.2.6.tar.gz
$ cd magento2-2.2.6
$ php -v
7.0.30
$ curl -sS https://getcomposer.org/installer | php
$ php composer.phar install
~~~