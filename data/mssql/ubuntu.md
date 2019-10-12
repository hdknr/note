# Ubuntu

## FreeTDS on Ubuntu

- [sql server - How to install freetds in Linux? - Stack Overflow](https://stackoverflow.com/questions/33341510/how-to-install-freetds-in-linux)

~~~bash
$ sudo apt update && sudo apt install unixodbc unixodbc-dev freetds-dev freetds-bin tdsodbc -y
.

$ dpkg -L freetds-common | grep etc
/etc
/etc/freetds
.

$ tree /etc/freetds/

/etc/freetds/
└── freetds.conf

~~~

~~~bash
$ dpkg -L tdsodbc | grep lib
/usr/lib
/usr/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu/odbc
/usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so
...

$ sudo tree /usr/lib/x86_64-linux-gnu/odbc
/usr/lib/x86_64-linux-gnu/odbc
├── libesoobS.so
├── libmimerS.so
├── libnn.so
├── libodbcdrvcfg1S.so
├── libodbcdrvcfg2S.so
├── libodbcminiS.so
├── libodbcmyS.so
├── libodbcnnS.so
├── libodbcpsqlS.so
├── libodbctxtS.so
├── liboplodbcS.so
├── liboraodbcS.so
├── libsapdbS.so
├── libtdsS.so
└── libtdsodbc.so

~~~

~~~bash
$ dpkg -L odbcinst | grep ini
/etc/odbc.ini
.
~~~

~~~bash
$ sudo vim /etc/odbcinst.ini
...
~~~

~~~ini
[FreeTDS]
Description=FreeTDS Driver
Driver=/usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so
Setup=/usr/lib/x86_64-linux-gnu/odbc/libtdsS.so
~~~

