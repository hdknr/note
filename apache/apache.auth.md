# Apache Auth関連

## libpam-mysql

~~~bash
# apt-get install libpam-mysql
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  libpam-mysql
0 upgraded, 1 newly installed, 0 to remove and 9 not upgraded.
Need to get 34.3 kB of archives.
After this operation, 60.4 kB of additional disk space will be used.
Get:1 http://ftp.uk.debian.org/debian/ jessie/main libpam-mysql amd64 0.7~RC1-4+b3 [34.3 kB]
Fetched 34.3 kB in 0s (40.8 kB/s) 
Preconfiguring packages ...
Selecting previously unselected package libpam-mysql.
(Reading database ... 64632 files and directories currently installed.)
Preparing to unpack .../libpam-mysql_0.7~RC1-4+b3_amd64.deb ...
Unpacking libpam-mysql (0.7~RC1-4+b3) ...
Setting up libpam-mysql (0.7~RC1-4+b3) ...
~~~

~~~bash
# dpkg -L libpam-mysql
/.
/etc
/etc/pam-mysql.conf
/lib
/lib/security
/lib/security/pam_mysql.so
/usr
/usr/share
/usr/share/doc
/usr/share/doc/libpam-mysql
/usr/share/doc/libpam-mysql/CREDITS
/usr/share/doc/libpam-mysql/README.Debian
/usr/share/doc/libpam-mysql/TODO.Debian
/usr/share/doc/libpam-mysql/copyright
/usr/share/doc/libpam-mysql/NEWS.gz
/usr/share/doc/libpam-mysql/README.gz
/usr/share/doc/libpam-mysql/changelog.Debian.gz
/usr/share/doc/libpam-mysql/changelog.gz
~~~

## libapache2-mod-authnz-pam

~~~bash
# apt-get install libapache2-mod-authnz-pam
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following extra packages will be installed:
  apache2-bin libaprutil1-dbd-sqlite3 libaprutil1-ldap
Suggested packages:
  apache2-doc apache2-suexec-pristine apache2-suexec-custom
The following NEW packages will be installed:
  apache2-bin libapache2-mod-authnz-pam libaprutil1-dbd-sqlite3 libaprutil1-ldap
0 upgraded, 4 newly installed, 0 to remove and 9 not upgraded.
Need to get 1,073 kB of archives.
After this operation, 3,932 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
~~~

~~~bash
# dpkg -L libapache2-mod-authnz-pam
/.
/etc
/etc/apache2
/etc/apache2/mods-available
/etc/apache2/mods-available/authnz_pam.conf
/etc/apache2/mods-available/authnz_pam.load
/usr
/usr/share
/usr/share/doc
/usr/share/doc/libapache2-mod-authnz-pam
/usr/share/doc/libapache2-mod-authnz-pam/changelog.Debian.gz
/usr/share/doc/libapache2-mod-authnz-pam/copyright
/usr/share/doc/libapache2-mod-authnz-pam/README
/usr/lib
/usr/lib/apache2
/usr/lib/apache2/modules
/usr/lib/apache2/modules/mod_authnz_pam.so
~~~

~~~bash
# a2enmod authnz_pam
Enabling module authnz_pam.
To activate the new configuration, you need to run:
  service apache2 restart
~~~
  
## libpam-python

~~~bash
# apt-get install libpam-python
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Suggested packages:
  libpam-python-doc
The following NEW packages will be installed:
  libpam-python
0 upgraded, 1 newly installed, 0 to remove and 9 not upgraded.
Need to get 28.7 kB of archives.
After this operation, 129 kB of additional disk space will be used.
Get:1 http://ftp.uk.debian.org/debian/ jessie/main libpam-python amd64 1.0.4-1 [28.7 kB]
Fetched 28.7 kB in 1s (19.9 kB/s)        
Selecting previously unselected package libpam-python.
(Reading database ... 65296 files and directories currently installed.)
Preparing to unpack .../libpam-python_1.0.4-1_amd64.deb ...
Unpacking libpam-python (1.0.4-1) ...
Setting up libpam-python (1.0.4-1) ...
~~~  
  
  
## pwauth

~~~bash
# apt-get install pwauth
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following extra packages will be installed:
  libapache2-mod-authnz-external
The following NEW packages will be installed:
  libapache2-mod-authnz-external pwauth
0 upgraded, 2 newly installed, 0 to remove and 9 not upgraded.
Need to get 36.2 kB of archives.
After this operation, 117 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://ftp.uk.debian.org/debian/ jessie/main libapache2-mod-authnz-external amd64 3.3.2-0.1+b1 [25.4 kB]
Get:2 http://ftp.uk.debian.org/debian/ jessie/main pwauth amd64 2.3.11-0.1 [10.9 kB]
Fetched 36.2 kB in 1s (20.0 kB/s)
Selecting previously unselected package libapache2-mod-authnz-external.
(Reading database ... 65302 files and directories currently installed.)
Preparing to unpack .../libapache2-mod-authnz-external_3.3.2-0.1+b1_amd64.deb ...
Unpacking libapache2-mod-authnz-external (3.3.2-0.1+b1) ...
Selecting previously unselected package pwauth.
Preparing to unpack .../pwauth_2.3.11-0.1_amd64.deb ...
Unpacking pwauth (2.3.11-0.1) ...
Processing triggers for man-db (2.7.0.2-5) ...
Setting up libapache2-mod-authnz-external (3.3.2-0.1+b1) ...
apache2_invoke: Enable module authnz_external
Setting up pwauth (2.3.11-0.1) ...

~~~  

~~~bash
# dpkg -L pwauth
/.
/etc
/etc/pam.d
/etc/pam.d/pwauth
/usr
/usr/share
/usr/share/lintian
/usr/share/lintian/overrides
/usr/share/lintian/overrides/pwauth
/usr/share/doc
/usr/share/doc/pwauth
/usr/share/doc/pwauth/FORM_AUTH
/usr/share/doc/pwauth/changelog.Debian.gz
/usr/share/doc/pwauth/copyright
/usr/share/doc/pwauth/changelog.gz
/usr/share/doc/pwauth/README.Debian
/usr/share/man
/usr/share/man/man8
/usr/share/man/man8/pwauth.8.gz
/usr/sbin
/usr/sbin/pwauth
~~~
