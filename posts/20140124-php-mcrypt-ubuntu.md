Date: 2014-01-24  
Title: PHP:Ubuntu 13.10 : Call to undefined function mcrypt_create_iv()
Type: post  
Excerpt:   


Ubuntu にaptで php5-mcrypt 入れたはずなのにエラー:

    $ lsb_release -a
    No LSB modules are available.
    Distributor ID: Ubuntu
    Description:    Ubuntu 13.10
    Release:        13.10
    Codename:       saucy

認識されていないっぽい:

    $ php --ini
    Configuration File (php.ini) Path: /etc/php5/cli
    Loaded Configuration File:         /etc/php5/cli/php.ini
    Scan for additional .ini files in: /etc/php5/cli/conf.d
    Additional .ini files parsed:      /etc/php5/cli/conf.d/05-opcache.ini,
    /etc/php5/cli/conf.d/10-pdo.ini,
    /etc/php5/cli/conf.d/20-gmp.ini,
    /etc/php5/cli/conf.d/20-json.ini,
    /etc/php5/cli/conf.d/20-readline.ini,
    /etc/php5/cli/conf.d/20-xdebug.ini

Debian Wheezyだと 20-mcrypt.ini ある:

    $ php --ini
    Configuration File (php.ini) Path: /etc/php5/cli
    Loaded Configuration File:         /etc/php5/cli/php.ini
    Scan for additional .ini files in: /etc/php5/cli/conf.d
    Additional .ini files parsed:      /etc/php5/cli/conf.d/10-pdo.ini,
    /etc/php5/cli/conf.d/20-curl.ini,
    /etc/php5/cli/conf.d/20-gd.ini,
    /etc/php5/cli/conf.d/20-gmp.ini,
    /etc/php5/cli/conf.d/20-mcrypt.ini,
    /etc/php5/cli/conf.d/20-mysql.ini,
    /etc/php5/cli/conf.d/20-mysqli.ini,
    /etc/php5/cli/conf.d/20-pdo_mysql.ini

Ubuntu にcurlを入れてみると:
    
    $ sudo aptitude install php5-curl 
    The following NEW packages will be installed:
      php5-curl 
    0 packages upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
    Need to get 33.3 kB of archives. After unpacking 138 kB will be used.
    Get: 1 http://ap-northeast-1.ec2.archive.ubuntu.com/ubuntu/ saucy-updates/main php5-curl amd64 5.5.3+dfsg-1ubuntu2.1 [33.3 kB]
    Fetched 33.3 kB in 0s (74.4 kB/s)
    Selecting previously unselected package php5-curl.
    (Reading database ... 107991 files and directories currently installed.)
    Unpacking php5-curl (from .../php5-curl_5.5.3+dfsg-1ubuntu2.1_amd64.deb) ...
    Processing triggers for libapache2-mod-php5 ...
    Setting up php5-curl (5.5.3+dfsg-1ubuntu2.1) ...
    
    Creating config file /etc/php5/mods-available/curl.ini with new version
    php5_invoke: Enable module curl for apache2 SAPI
    php5_invoke: Enable module curl for cli SAPI
    Processing triggers for libapache2-mod-php5 ...
    
クライアント設定にcurl追加された: 
    
    $ php --ini
    Configuration File (php.ini) Path: /etc/php5/cli
    Loaded Configuration File:         /etc/php5/cli/php.ini
    Scan for additional .ini files in: /etc/php5/cli/conf.d
    Additional .ini files parsed:      /etc/php5/cli/conf.d/05-opcache.ini,
    /etc/php5/cli/conf.d/10-pdo.ini,
    /etc/php5/cli/conf.d/20-curl.ini,
    /etc/php5/cli/conf.d/20-gmp.ini,
    /etc/php5/cli/conf.d/20-json.ini,
    /etc/php5/cli/conf.d/20-readline.ini,
    /etc/php5/cli/conf.d/20-xdebug.ini
    
再度インストール :

    $ sudo apt-get --reinstall install php5-mcrypt
    Reading package lists... Done
    Building dependency tree       
    Reading state information... Done
    0 upgraded, 0 newly installed, 1 reinstalled, 0 to remove and 0 not upgraded.
    Need to get 0 B/18.3 kB of archives.
    After this operation, 0 B of additional disk space will be used.
    (Reading database ... 107998 files and directories currently installed.)
    Preparing to replace php5-mcrypt 5.4.6-0ubuntu3 (using .../php5-mcrypt_5.4.6-0ubuntu3_amd64.deb) ...
    Unpacking replacement php5-mcrypt ...
    Setting up php5-mcrypt (5.4.6-0ubuntu3) ...
    
/etc/php5/conf.d/mcrypto.ini がある:

    ubuntu@ip-10-0-0-117:~/php/code/connect$ dpkg -L php5-mcrypt
    /.
    /usr
    /usr/share
    /usr/share/doc
    /usr/share/doc/php5-mcrypt
    /usr/share/doc/php5-mcrypt/copyright
    /usr/share/doc/php5-mcrypt/changelog.Debian.gz
    /usr/lib
    /usr/lib/php5
    /usr/lib/php5/20121212
    /usr/lib/php5/20121212/mcrypt.so
    /etc
    /etc/php5
    /etc/php5/conf.d
    /etc/php5/conf.d/mcrypt.ini
    
[StackOverflow](https://stackoverflow.com/questions/19446679/mcrypt-not-present-after-ubuntu-upgrade-to-13-10)  に載ってた
    
    $ sudo ln -s /etc/php5/conf.d/mcrypt.ini /etc/php5/mods-available
    $ sudo php5enmod mcrypt
    
確認したらOK:

    $ php --ini
    Configuration File (php.ini) Path: /etc/php5/cli
    Loaded Configuration File:         /etc/php5/cli/php.ini
    Scan for additional .ini files in: /etc/php5/cli/conf.d
    Additional .ini files parsed:      /etc/php5/cli/conf.d/05-opcache.ini,
    /etc/php5/cli/conf.d/10-pdo.ini,
    /etc/php5/cli/conf.d/20-curl.ini,
    /etc/php5/cli/conf.d/20-gmp.ini,
    /etc/php5/cli/conf.d/20-json.ini,
    /etc/php5/cli/conf.d/20-mcrypt.ini,
    /etc/php5/cli/conf.d/20-readline.ini,
    /etc/php5/cli/conf.d/20-xdebug.ini
    
使えそう:

    $ php -a
    Interactive mode enabled
    
    php > echo function_exists('mcrypt_create_iv')."\n";
    1
    
    
