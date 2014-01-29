Date: 2014-01-28  11:00
Title:  Azure:CentOS(Openlogic)でのyum 
Type: post  
Excerpt:   



yum update でエラー:

    $ sudo yum update
     :
     :
    [---> Package zlib.x86_64 0:1.2.3-29.el6 will be an update
    --> Finished Dependency Resolution
    Skip-broken could not solve problems
    Error: Package: glibc-headers-2.12-1.132.el6.x86_64 (base)
               Requires: kernel-headers >= 2.2.1
    Error: Package: glibc-headers-2.12-1.132.el6.x86_64 (base)
               Requires: kernel-headers
    Error: Package: 2:irqbalance-1.0.4-8.el6_5.x86_64 (updates)
               Requires: kernel >= 2.6.32-358.2.1
               Installed: kernel-2.6.32-279.14.1.el6.openlogic.x86_64 (@openlogic)
                   kernel = 2.6.32-279.14.1.el6.openlogic
                   kernel = 2.6.32-279.14.1.el6.openlogic
     You could try running: rpm -Va --nofiles --nodigest

[こちらの写経](http://tech.guitarrapc.com/entry/2013/05/07/210540) でヘッダーがはいった:

    $ sudo yum --disableexcludes=main install kernel-headers
 
パッケージ更新:
    
    $ sudo yum --disableexcludes=main update

ビルドツール入った:
    
    $ sudo yum install gcc gcc-c++  autoconf automake kernel-devel ncurses-devel
