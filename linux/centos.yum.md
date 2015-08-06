## パッケージレポジトリの追加

- [Install php-mcrypt on CentOS 6](https://stackoverflow.com/questions/17109818/install-php-mcrypt-on-centos-6)

~~~bash
$ wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
$ wget http://rpms.famillecollet.com/enterprise/remi-release-6.rpm
$ sudo rpm -Uvh remi-release-6*.rpm epel-release-6*.rpm
$ sudo yum upgrade ca-certificates --disablerepo=epel
$ sudo yum update
~~~