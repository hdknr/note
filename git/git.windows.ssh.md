# Windows: git に sshの設定

- ssh_config に IdentityFile を設定すればいい、という話

## ChocolateyでNugetのGitインストール

- [gitパッケージ](https://chocolatey.org/packages/git)

~~~bat
C:\Users\hdknr> choco install git
~~~

## ssh-keygen でキーの作成

~~~bat
C:\Users\hdknr>where ssh-keygen
C:\ProgramData\chocolatey\bin\ssh-keygen
C:\ProgramData\chocolatey\bin\ssh-keygen.bat
~~~

~~~bat
C:\Users\hdknr> mkdir .ssh
~~~

~~~bat
C:\Users\hdknr> ssh-keygen -b 4096 -f \Users\hdknr\.ssh\win8.key

Generating public/private rsa key pair.
cygwin warning:
  MS-DOS style path detected: \Users\hdknr\.ssh\win8.key
  Preferred POSIX equivalent is: /cygdrive/c/Users/hdknr/.ssh/win8.key
  CYGWIN environment variable option "nodosfilewarning" turns off this warning.
  Consult the user's guide for more details about POSIX paths:
    http://cygwin.com/cygwin-ug-net/using.html#using-pathnames
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in \Users\hdknr\.ssh\win8.key.
Your public key has been saved in \Users\hdknr\.ssh\win8.key.pub.
The key fingerprint is:
93:66:5a:0e:7b:e4:a1:2d:fc:ee:46:4f:46:1c:07:fa hdknr@Blacky
The key's randomart image is:
+--[ RSA 4096]----+
|          ..     |
|         .. .    |
|        .. o     |
|         oo      |
|      . S.E      |
|     . &.oo      |
|      *.=+       |
|       +. .      |
|       ++        |
+-----------------+

~~~

~~~
C:\Users\hdknr>dir \Users\hdknr\.ssh
 ドライブ C のボリューム ラベルは Acer です
 ボリューム シリアル番号は 9AAA-8637 です

 C:\Users\hdknr\.ssh のディレクトリ

2015/03/29  17:35    <DIR>          .
2015/03/29  17:35    <DIR>          ..
2015/03/29  16:51               410 known_hosts
2015/03/29  17:35             3,243 win8.key
2015/03/29  17:35               738 win8.key.pub

               5 個のファイル               8,372 バイト
               2 個のディレクトリ  807,079,927,808 バイトの空き領域
~~~

## %GIT%¥etc¥ssh¥ssh_config で IndentityFile 指定

~~~bat
C:\Users\hdknr>where git
C:\Program Files (x86)\Git\cmd\git.exe
~~~

~~~bat
C:\Users\hdknr>cd C:\Program Files (x86)\Git\etc
C:\Program Files (x86)\Git\etc>mkdir ssh
~~~

- 編集

~~~bat
C:\Program Files (x86)\Git\etc>gvim ssh\ssh_config
~~~

- Bitbucket.org に設定

~~~
Host bitbucket.org
  IdentityFile C:\Users\hdknr\.ssh\win8.key
~~~

## Bitbucketからclone

- bitbuket に win8.key.pub を設定しておくこと

~~~bat
C:\Users\hdknr>git clone git@bitbucket.org:hdknr/photo.git
Cloning into 'photo'...
remote: Counting objects: 33, done.
remote: Compressing objects: 100% (31/31), done.
remote: Total 33 (delta 1), reused 0 (delta 0)
Receiving objects: 100% (33/33), 9.72 MiB | 400.00 KiB/s, done.
Resolving deltas: 100% (1/1), done.
Checking connectivity... done.
~~~
