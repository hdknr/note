## cx_Oracle

- [install cx_oracle for python](https://stackoverflow.com/questions/4307479/install-cx-oracle-for-python)

- [
Instant Client Downloads](http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html) > [Instant Client Downloads
for Linux AMD64](http://www.oracle.com/technetwork/topics/linux-amd64-093390.html)

~~~bash
$ export ORACLE_HOME=/opt/ora
~~~

~~~bash
$ ls -l $ORACLE_HOME
合計 85480
-r--r--r-- 1 vagrant vagrant  1442415 12月  6  2005 classes12.jar
-rwxr-xr-x 1 vagrant vagrant 15306239 12月  6  2005 libclntsh.so.10.1
-rwxr-xr-x 1 vagrant vagrant  1773518 12月  6  2005 libnnz10.so
-rwxr-xr-x 1 vagrant vagrant   958670 12月  6  2005 libocci.so.10.1
-rwxr-xr-x 1 vagrant vagrant 66423996 12月  6  2005 libociei.so
-rwxr-xr-x 1 vagrant vagrant   122861 12月  6  2005 libocijdbc10.so
-r--r--r-- 1 vagrant vagrant  1378315 12月  6  2005 ojdbc14.jar
drwxr-xr-x 4 vagrant vagrant     4096 12月  6  2005 sdk
~~~

~~~bash
$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME
$ cd $ORACLE_HOME && ln -s libclntsh.so.10.1 libclntsh.so
~~~

- OSX

~~~bash
$ ln -s libclntsh.dylib.11.1 libclntsh.dylib
~~~

~~~bash
$ pip install cx_Oracle
Collecting cx-Oracle
  Using cached cx_Oracle-5.2.tar.gz
Building wheels for collected packages: cx-Oracle
  Running setup.py bdist_wheel for cx-Oracle
  Stored in directory: /home/vagrant/.cache/pip/wheels/a5/df/4a/849aa2c9933012aee4fae839ac1618d463bfce02d51b299996
Successfully built cx-Oracle
Installing collected packages: cx-Oracle
Successfully installed cx-Oracle-5.2
~~~
