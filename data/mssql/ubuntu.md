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

## ODBC Driver for SQL Server on Linux

- [Ubuntu + FreeTDS + Django 2.0.1: The database driver doesn't support modern datatime types. · Issue #142 · michiya/django-pyodbc-azure · GitHub](https://github.com/michiya/django-pyodbc-azure/issues/142)
- [Installing the Microsoft ODBC Driver for SQL Server on Linux and macOS - SQL Server - Microsoft Docs](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017)

~~~bash
$  curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
OK

$ curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list | sudo tee -a /etc/apt/sources.list.d/mssql-release.list
deb [arch=amd64] https://packages.microsoft.com/ubuntu/18.04/prod bionic main(incident)

$ sudo apt update
ヒット:1 http://ap-northeast-1.ec2.archive.ubuntu.com/ubuntu bionic InRelease
取得:2 http://ap-northeast-1.ec2.archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]
取得:3 http://ap-northeast-1.ec2.archive.ubuntu.com/ubuntu bionic-backports InRelease [74.6 kB]                                                  
取得:4 http://ap-northeast-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages [764 kB]                                           
取得:5 http://ap-northeast-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/universe amd64 Packages [1,017 kB]                                     
取得:6 https://packages.microsoft.com/ubuntu/18.04/prod bionic InRelease [3,982 B]                                                               
取得:7 http://security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB]                                                           
取得:8 https://packages.microsoft.com/ubuntu/18.04/prod bionic/main amd64 Packages [76.4 kB]

$ sudo apt list --upgradable
一覧表示... 完了                     
libodbc1/bionic 2.3.7 amd64 [2.3.4-1.1ubuntu3 からアップグレード可]
odbcinst/bionic 2.3.7 amd64 [2.3.4-1.1ubuntu3 からアップグレード可]
odbcinst1debian2/bionic 2.3.7 amd64 [2.3.4-1.1ubuntu3 からアップグレード可]
unixodbc/bionic 2.3.7 amd64 [2.3.4-1.1ubuntu3 からアップグレード可]
unixodbc-dev/bionic 2.3.7 amd64 [2.3.4-1.1ubuntu3 からアップグレード可]

$ sudo apt upgrade -y
パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています                
状態情報を読み取っています... 完了
アップグレードパッケージを検出しています... 完了
以下のパッケージはアップグレードされます:
  libodbc1 odbcinst odbcinst1debian2 unixodbc unixodbc-dev
アップグレード: 5 個、新規インストール: 0 個、削除: 0 個、保留: 0 個。
714 kB のアーカイブを取得する必要があります。
この操作後に追加で 63.5 kB のディスク容量が消費されます。
取得:1 https://packages.microsoft.com/ubuntu/18.04/prod bionic/main amd64 odbcinst amd64 2.3.7 [12.0 kB]
取得:2 https://packages.microsoft.com/ubuntu/18.04/prod bionic/main amd64 unixodbc-dev amd64 2.3.7 [37.1 kB]
取得:3 https://packages.microsoft.com/ubuntu/18.04/prod bionic/main amd64 odbcinst1debian2 amd64 2.3.7 [135 kB]
取得:4 https://packages.microsoft.com/ubuntu/18.04/prod bionic/main amd64 libodbc1 amd64 2.3.7 [511 kB]
取得:5 https://packages.microsoft.com/ubuntu/18.04/prod bionic/main amd64 unixodbc amd64 2.3.7 [19.6 kB]
714 kB を 1秒 で取得しました (902 kB/s)
(データベースを読み込んでいます ... 現在 171408 個のファイルとディレクトリがインストールされています。)
.../odbcinst_2.3.7_amd64.deb を展開する準備をしています ...
odbcinst (2.3.7) で (2.3.4-1.1ubuntu3 に) 上書き展開しています ...
.../unixodbc-dev_2.3.7_amd64.deb を展開する準備をしています ...
unixodbc-dev (2.3.7) で (2.3.4-1.1ubuntu3 に) 上書き展開しています ...
.../odbcinst1debian2_2.3.7_amd64.deb を展開する準備をしています ...
odbcinst1debian2:amd64 (2.3.7) で (2.3.4-1.1ubuntu3 に) 上書き展開しています ...
.../libodbc1_2.3.7_amd64.deb を展開する準備をしています ...
libodbc1:amd64 (2.3.7) で (2.3.4-1.1ubuntu3 に) 上書き展開しています ...
.../unixodbc_2.3.7_amd64.deb を展開する準備をしています ...
unixodbc (2.3.7) で (2.3.4-1.1ubuntu3 に) 上書き展開しています ...
libodbc1:amd64 (2.3.7) を設定しています ...
odbcinst1debian2:amd64 (2.3.7) を設定しています ...
odbcinst (2.3.7) を設定しています ...
unixodbc (2.3.7) を設定しています ...
unixodbc-dev (2.3.7) を設定しています ...
libc-bin (2.27-3ubuntu1) のトリガを処理しています ...
man-db (2.8.3-2ubuntu0.1) のトリガを処理しています ...

$ sudo ACCEPT_EULA=Y apt install msodbcsql17
パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています
状態情報を読み取っています... 完了
以下のパッケージが新たにインストールされます:
  msodbcsql17
アップグレード: 0 個、新規インストール: 1 個、削除: 0 個、保留: 0 個。
750 kB のアーカイブを取得する必要があります。
この操作後に追加で 0 B のディスク容量が消費されます。
取得:1 https://packages.microsoft.com/ubuntu/18.04/prod bionic/main amd64 msodbcsql17 amd64 17.4.2.1-1 [750 kB]
750 kB を 1秒 で取得しました (959 kB/s)
パッケージを事前設定しています ...
以前に未選択のパッケージ msodbcsql17 を選択しています。
(データベースを読み込んでいます ... 現在 171374 個のファイルとディレクトリがインストールされています。)
.../msodbcsql17_17.4.2.1-1_amd64.deb を展開する準備をしています ...
msodbcsql17 (17.4.2.1-1) を展開しています...
msodbcsql17 (17.4.2.1-1) を設定しています ...


$ sudo ACCEPT_EULA=Y apt install mssql-tools
パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています                
状態情報を読み取っています... 完了
以下のパッケージが新たにインストールされます:
  mssql-tools
アップグレード: 0 個、新規インストール: 1 個、削除: 0 個、保留: 0 個。
209 kB のアーカイブを取得する必要があります。
この操作後に追加で 0 B のディスク容量が消費されます。
取得:1 https://packages.microsoft.com/ubuntu/18.04/prod bionic/main amd64 mssql-tools amd64 17.4.1.1-1 [209 kB]
209 kB を 1秒 で取得しました (363 kB/s)
パッケージを事前設定しています ...
以前に未選択のパッケージ mssql-tools を選択しています。
(データベースを読み込んでいます ... 現在 171391 個のファイルとディレクトリがインストールされています。)
.../mssql-tools_17.4.1.1-1_amd64.deb を展開する準備をしています ...
mssql-tools (17.4.1.1-1) を展開しています...
mssql-tools (17.4.1.1-1) を設定しています ...
~~~
