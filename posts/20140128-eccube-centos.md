Date: 2014-01-28  14:00
Title: EC-CUBE: CentOSに入れる  
Type: post  
Excerpt:   

    
apacheに仮想サーバー:
    
    <VirtualHost *:80>

        LogLevel debug
    
        ServerAdmin admin@hdknr.local
        ServerName  eccube

        DocumentRoot /home/hdknr/eccube/site/ec/html
  
        ErrorLog /home/hdknr/eccube/site/logs/errors.log
        CustomLog /home/hdknr/eccube/site/logs/access.log combined
  
    </VirtualHost>
    

ec-cubeをダウンロードして、/home/hdknr/eccube/site/ecに解凍した物をコピー

    $ ls -l ec
    total 48
    -rw-r--r--.  1 hdknr hdknr  1278 Dec 17  2012 build.xml
    -rw-r--r--.  1 hdknr hdknr    78 Jun  6  2013 composer.json
    -rw-r--r--.  1 hdknr hdknr 17987 Feb  9  2011 COPYING
    drwxr-xr-x. 15 hdknr hdknr  4096 Nov 18 08:34 data
    drwxr-xr-x.  2 hdknr hdknr  4096 Nov 18 08:34 docs
    drwxrwxrwx. 25 hdknr hdknr  4096 Jan 28 04:45 html
    drwxr-xr-x.  4 hdknr hdknr  4096 Nov 18 08:34 test
    drwxr-xr-x.  3 hdknr hdknr  4096 Nov 18 08:34 tests

追加でyumパッケージ入れる
    
    $ sudo yum groupinstall "Web Server" "MySQL Database client" "MySQL Database server" "PHP Support" -y
    $ sudo yum install php-gd freetype-devel php-mbstring php-xml libcurl-devel php-mcrypt -y
    
pear でMDB2:

    $ sudo pear install MDB2
    
MDB2のMySQLドライバ:

    $ sudo  pear install MDB2_Driver_mysql
    WARNING: channel "pear.php.net" has updated its protocols, use "pear channel-update pear.php.net" to update
    pear/MDB2_Driver_mysql requires PHP extension "mysql"
    No valid packages found
    install failed

php-mysql が足りなかった
    
    $ sudo yum install php-mysql
    
これでいける:

    $ sudo  pear install MDB2_Driver_mysql
    
    $ sudo pear list
    Installed packages, channel pear.php.net:
    =========================================
    Package           Version State
    Archive_Tar       1.3.7   stable
    Console_Getopt    1.2.3   stable
    MDB2              2.4.1   stable
    MDB2_Driver_mysql 1.4.1   stable
    PEAR              1.9.4   stable
    Structures_Graph  1.0.4   stable
    XML_RPC           1.5.4   stable
    XML_Util          1.2.1   stable
    
DB作成:
    
    $ more ../createdb.sql
    CREATE DATABASE eccube DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    GRANT ALL on eccube.* to 'eccube'@'localhost' identified by 'eccube' WITH GRANT OPTION; 

    $ mysql -u root --password=root_no_password < ../createdb.sql

あとは、 http://eccube/install/ にアクセスして進める。
