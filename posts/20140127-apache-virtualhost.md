Date: 2014-01-27  11:00
Title: apache 2.4: NameVitualHostはdepreciated  
Type: post  
Excerpt:   


mod_macro で２つのVirtulaHostを定義しているが、１つ(abop)がアクセスできない:

    <VirtualHost *:80>
        LogLevel debug
        Use Main abrp.deb /home/ubuntu/php rp 
    </VirtualHost>
    
    <VirtualHost *:80>
        LogLevel debug
        Use Main abop.deb /home/ubuntu/php op
        Use WellKnown /home/ubuntu/php 
    </VirtualHost>


    $ curl -I http://abrp.deb/abrp/
    HTTP/1.1 200 OK
    Date: Mon, 27 Jan 2014 02:56:02 GMT
    Server: Apache/2.4.6 (Ubuntu)
    X-Powered-By: PHP/5.5.3-1ubuntu2.1
    Set-Cookie: PHPSESSID=3hpet5j5ntpcitm5jnpbrr4ra1; path=/
    Expires: Thu, 19 Nov 1981 08:52:00 GMT
    Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
    Pragma: no-cache
    Content-Type: text/html; charset=utf-8
    
    $ curl -I http://abop.deb/abop/
    HTTP/1.1 404 Not Found
    Date: Mon, 27 Jan 2014 02:56:09 GMT
    Server: Apache/2.4.6 (Ubuntu)
    Content-Type: text/html; charset=iso-8859-1
    
404だからサイトは建っているっぽい。ようは、abop.debの方がデフォルトサイトを観ている:

    $ sudo apachectl -S
    
    VirtualHost configuration:
    *:80                   is a NameVirtualHost
             default server abop.deb (/etc/apache2/sites-enabled/000-default.conf:1)
             port 80 namevhost abop.deb (/etc/apache2/sites-enabled/000-default.conf:1)
             port 80 namevhost abop.deb (/etc/apache2/sites-enabled/000-default.conf:1)
             port 80 namevhost abrp.deb (/etc/apache2/sites-enabled/ab.conf:31)
             port 80 namevhost abrp.deb (/etc/apache2/sites-enabled/ab.conf:31)
             port 80 namevhost abop.deb (/etc/apache2/sites-enabled/ab.conf:40)
             port 80 namevhost abop.deb (/etc/apache2/sites-enabled/ab.conf:40)
    ServerRoot: "/etc/apache2"
    Main DocumentRoot: "/var/www"
    Main ErrorLog: "/var/log/apache2/error.log"
    Mutex default: dir="/var/lock/apache2" mechanism=fcntl 
    Mutex mpm-accept: using_defaults
    Mutex watchdog-callback: using_defaults
    PidFile: "/var/run/apache2/apache2.pid"
    Define: DUMP_VHOSTS
    Define: DUMP_RUN_CFG
    User: name="www-data" id=33
    Group: name="www-data" id=33

ので、サイトルートはいける:

    $ curl  http://abop.deb/
    <html><body><h1>It works!</h1>
    <p>This is the default web page for this server.</p>
    <p>The web server software is running but no content has been added, yet.</p>
    </body></html>

Debian Wheezyみたいに /etc/apache/ports.conf に NameVirtualHostいれればいいいなじゃいの？:

    $ sudo /etc/init.d/apache2 restart
     * Restarting web server apache2
    AH00548: NameVirtualHost has no effect and will be removed in the next release /etc/apache2/ports.conf:5
       ...done.
        

ということで、もどして、 000-default.conf に ServerName入れる：

    $ curl -I http://abop.deb/abop/
    HTTP/1.1 200 OK
    Date: Mon, 27 Jan 2014 03:00:40 GMT
    Server: Apache/2.4.6 (Ubuntu)
    X-Powered-By: PHP/5.5.3-1ubuntu2.1
    Set-Cookie: PHPSESSID=brol9rgi994pe6dbl9g30uv1v3; path=/
    Expires: Thu, 19 Nov 1981 08:52:00 GMT
    Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
    Pragma: no-cache
    Content-Type: text/html
    
    $ sudo apachectl -S
    VirtualHost configuration:
    *:80                   is a NameVirtualHost
             default server localhost (/etc/apache2/sites-enabled/000-default.conf:1)
             port 80 namevhost localhost (/etc/apache2/sites-enabled/000-default.conf:1)
             port 80 namevhost localhost (/etc/apache2/sites-enabled/000-default.conf:1)
             port 80 namevhost abrp.deb (/etc/apache2/sites-enabled/ab.conf:31)
             port 80 namevhost abrp.deb (/etc/apache2/sites-enabled/ab.conf:31)
             port 80 namevhost abop.deb (/etc/apache2/sites-enabled/ab.conf:40)
             port 80 namevhost abop.deb (/etc/apache2/sites-enabled/ab.conf:40)
    ServerRoot: "/etc/apache2"
    Main DocumentRoot: "/var/www"
    Main ErrorLog: "/var/log/apache2/error.log"
    Mutex watchdog-callback: using_defaults
    Mutex default: dir="/var/lock/apache2" mechanism=fcntl 
    Mutex mpm-accept: using_defaults
    PidFile: "/var/run/apache2/apache2.pid"
    Define: DUMP_VHOSTS
    Define: DUMP_RUN_CFG
    User: name="www-data" id=33
    Group: name="www-data" id=33
