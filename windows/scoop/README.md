# scoop

- [Scoop](https://scoop.sh/)


## インストール


~~~ps1
PS C:\Users\hdknr> Set-ExecutionPolicy RemoteSigned -scope CurrentUser

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose
you to the security risks described in the about_Execution_Policies help topic at
https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): Y
~~~

~~~ps1
PS C:\Users\hdknr> iwr -useb get.scoop.sh | iex

Initializing...
Downloading scoop...
Extracting...
Creating shim...
Downloading main bucket...
Extracting...
Adding ~\scoop\shims to your path.
'lastupdate' has been set to '2020-01-30T12:51:45.6665539+09:00'
Scoop was installed successfully!
Type 'scoop help' for instructions.
~~~

あるいは:

~~~ps1
iex (new-object net.webclient).downloadstring(‘https://get.scoop.sh’)
~~~


`curl`コマンドインストール:

~~~cmd
C:¥Users¥hdknr>scoop install curl

C:¥Users¥hdknr>where curl

C:¥WINDOWS¥System32¥curl.exe
C:¥Users¥hdknr¥scoop¥shime¥curl.exe
~~~

## SSH on Windows

- [https://github.com/lukesampson/scoop/wiki/SSH-on-Windows](https://github.com/lukesampson/scoop/wiki/SSH-on-Windows)

~~~PS1
PS> scoop install openssh
PS> scoop install git-with-openssh
~~~

## Bucket

~~~PS1
PS> sccop bucket add extras
~~~

### VSCode

~~~PS1
PS> scoop install vscode
~~~~

### Vagrant

- https://www.virtualbox.org/wiki/Downloads から　VirutalBox をインストール

~~~powershell
PS C:\Users\hdknr> scoop install vagrant

Installing 'vagrant' (2.2.7) [64bit]
vagrant_2.2.7_x86_64.msi (210.3 MB) [=========================================================================] 100%
Checking hash of vagrant_2.2.7_x86_64.msi ... ok.
Extracting vagrant_2.2.7_x86_64.msi ... done.
Linking ~\scoop\apps\vagrant\current => ~\scoop\apps\vagrant\2.2.7
Creating shim for 'vagrant'.
'vagrant' (2.2.7) was installed successfully!
~~~

~~~powershell
PS C:\Users\hdknr> vagrant plugin install vagrant-vbguest

Installing the 'vagrant-vbguest' plugin. This can take a few minutes...
Fetching: micromachine-3.0.0.gem (100%)
Fetching: vagrant-vbguest-0.23.0.gem (100%)
Installed the plugin 'vagrant-vbguest (0.23.0)'!
~~~

~~~ps1
PS C:\Users\hdknr> vagrant plugin install vagrant-winnfsd

Installing the 'vagrant-winnfsd' plugin. This can take a few minutes...
Fetching: vagrant-winnfsd-1.4.0.gem (100%)
Installed the plugin 'vagrant-winnfsd (1.4.0)'!
~~~

### VSCode

~~~ps1
PS> scoop bucket add extras
PS> scoop install vscode
~~~

## 記事

- [Scoopで作るLinux on Windows開発環境](https://qiita.com/dozo/items/a6f63aa1b03d1773b8ec)
- [windowsで最初にやること](https://qiita.com/honeytrap15/items/e6e7f65bb436a4b5d813)
