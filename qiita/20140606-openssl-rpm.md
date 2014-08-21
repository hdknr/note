OpenSSL祭り : CentOS 5.5

[CVE-2014-0224](http://lepidum.co.jp/blog/2014-06-05/CCS-Injection/)とかいろいろ対応

http://www.openssl.org/ からアプデートを入手:


    $ wget https://www.openssl.org/source/openssl-0.9.8za.tar.gz
    

rpmbuild, [入っていますか](http://qiita.com/IK12_info/items/bcf695460363bae87eb9)？:

    $ sudo yum install rpm-build    

RPM作る:

    $ sudo rpmbuild -ta openssl-0.9.8za.tar.gz

インストール:

    $ sudo rpm -Uvh --nodeps /usr/src/redhat/RPMS/x86_64/*.rpm
    
