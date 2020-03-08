# Oracle インストール


## Ubuntu 環境

ユーザー/ グループ:

~~~bash
$ sudo addgroup oinstall
Adding group `oinstall' (GID 1001) ...
Done.

$ sudo addgroup dba 
Adding group `dba' (GID 1002) ...
Done.

$ sudo addgroup nobody
Adding group `nobody' (GID 1003) ...
Done.

$ sudo usermod -g nobody nobody

$ sudo useradd -g oinstall -G dba -p password -d /home/oracle -s /bin/bash oracle
$ mkdir -p /home/oracle
$ chown -R oracle:dba /home/oracle

$ sudo passwd oracle
Enter new UNIX password:  oracle
Retype new UNIX password: oracle
passwd: password updated successfully
~~~

コマンドパス:

~~~bash
$ sudo ln -s /usr/bin/awk /bin/awk
$ sudo ln -s /usr/bin/rpm /bin/rpm
$ sudo ln -s /usr/bin/basename /bin/basename
$ sudo mkdir /etc/rc.d
$ for i in 0 1 2 3 4 5 6 S ; do sudo ln -s /etc/rc$i.d /etc/rc.d/rc$i.d ; done
~~~

インストール先ストレージ:

~~~
$ sudo mkdir -p /u01/app/oracle
$ sudo chown -R oracle:dba /u01
~~~

## Ubuntu OS 設定


/etc/sysctl.conf:

~~~ini
fs.file-max = 65535 
kernel.shmall = 2097152 
kernel.shmmax = 2147483648 
kernel.shmmni = 4096
kernel.sem = 250 32000 100 128 
net.ipv4.ip_local_port_range = 1024 65535 
net.core.rmem_default = 1048576 
net.core.rmem_max = 1048576 
net.core.wmem_default = 262144 
net.core.wmem_max = 262144
~~~


/etc/security/limits.conf:

~~~ini
# Oracle
oracle soft nproc 2047 
oracle hard nproc 16383 
oracle soft nofile 1023 
oracle hard nofile 65535
~~~

~~~ini
$ sudo sysctl -p
fs.file-max = 65535
kernel.shmall = 2097152
kernel.shmmax = 2147483648
kernel.shmmni = 4096
kernel.sem = 250 32000 100 128
net.ipv4.ip_local_port_range = 1024 65535
net.core.rmem_default = 1048576
net.core.rmem_max = 1048576
net.core.wmem_default = 262144
net.core.wmem_max = 262144
~~~

## サイレント

- 応答ファイルを指定して、バッチインストール

### 1. 本体インストール(db_install.rsp)

- [Oracle 11g の 例](db_install.rsp.11g)
- [Oracle 12c の 例](db_install.rsp.12c)


実行は `oracle` ユーザーで行う:

~~~bash
$ sudo -u oracle ./runInstaller -silent -ignoreSysPrereqs -ignorePrereq -responseFile ~/response/db_install.rsp 
~~~

## 2. root スクリプト


~~~bash
$ cd /u01/app/oraInventory 
$ ./orainstRoot.sh
Changing permissions of /u01/app/oraInventory.      
Adding read,write permissions for group.                    
Removing read,write,execute permissions for world.       
                                                    
Changing groupname of /u01/app/oraInventory to oinstall.   
The execution of the script is complete.
~~~

~~~bash
$ cd /u01/app/oracle/product/11/db_1
$ ./root.sh 

Check /u01/app/oracle/product/11/db_1/install/root_ip-172-30-2-230_2020-02-20_02-14-35.log for the output of root script

$  more  /u01/app/oracle/product/11/db_1/install/root_ip-172-30-2-230_2020-02-20_02-14-35.log

Running Oracle 11g root.sh script...

The following environment variables are set as:
    ORACLE_OWNER= oracle
    ORACLE_HOME=  /u01/app/oracle/product/11/db_1

Creating /etc/oratab file...
Entries will be added to the /etc/oratab file as needed by
Database Configuration Assistant when a database is created
Finished running generic part of root.sh script.
Now product-specific root actions will be performed.
Finished product-specific root actions.
~~~

## 3. netca

`response/netca.rsp`:

~~~bash
$ git diff netca.rsp

diff --git a/netca.rsp b/netca.rsp
index ca227b4..45ccd36 100755
--- a/netca.rsp
+++ b/netca.rsp
@@ -44,7 +44,7 @@ CREATE_TYPE="CUSTOM"
 # The command line flag has precedence over the one in this response file.
 # This feature is present since 10.1.0.3.
 #-------------------------------------------------------------------------------
-#SHOW_GUI=false
+SHOW_GUI=false
 
 #-------------------------------------------------------------------------------
 # Name       : LOG_FILE
@@ -58,7 +58,7 @@ CREATE_TYPE="CUSTOM"
 # The command line argument has precedence over the one in this response file.
 # This feature is present since 10.1.0.3.
 #-------------------------------------------------------------------------------
-#LOG_FILE=""/oracle11gHome/network/tools/log/netca.log""
+LOG_FILE=""/u01/app/oraInventory/logs/netca.log""
 
 [oracle.net.ca]
 #INSTALLED_COMPONENTS;StringList;list of installed components
~~~

~~~bash 
$ sudo su - oracle
$ export DISPLAY=:0.0
$ netca -silent -responsefile ~/response/netca.rsp

Thu Feb 20 04:01:21 UTC 2020 Oracle Net Configuration Assistant
Parsing command line arguments:
    Parameter "silent" = true
    Parameter "responsefile" = /home/oracle/response/netca.rsp
    Parameter "log" = /u01/app/oraInventory/logs/netca.log
Done parsing command line arguments.
Oracle Net Services Configuration:
Profile configuration complete.
Oracle Net Listener Startup:
    Running Listener Control: 
      /u01/app/oracle/product/11/db_1/bin/lsnrctl start LISTENER
    Listener Control complete.
    Listener started successfully.
Listener configuration complete.
Oracle Net Services configuration successful. The exit code is 0
~~~

### 4. listner.ora

~~~bash
$ ls $ORACLE_HOME/network/admin/listener.ora
/u01/app/oracle/product/11/db_1/network/admin/listener.ora
~~~

~~~bash
$ which lsnrctl 
/u01/app/oracle/product/11/db_1/bin/lsnrctl
~~~
