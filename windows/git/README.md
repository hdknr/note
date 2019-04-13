# git

- [chocolatey](../chocolatey) がインストールされていること

~~~bash
C:\Users\spin\Documents\Projects>cinst git
Chocolatey v0.10.11
Installing the following packages:
git
By installing you accept licenses for the packages.
Progress: Downloading git.install 2.19.1... 100%
Progress: Downloading chocolatey-core.extension 1.3.3... 100%
Progress: Downloading git 2.19.1... 100%

chocolatey-core.extension v1.3.3 [Approved]
chocolatey-core.extension package files install completed. Performing other installation steps.
 Installed/updated chocolatey-core extensions.
 The install of chocolatey-core.extension was successful.
  Software installed to 'C:\ProgramData\chocolatey\extensions\chocolatey-core'

git.install v2.19.1 [Approved]
git.install package files install completed. Performing other installation steps.
The package git.install wants to run 'chocolateyInstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[N]o/[P]rint): y

Using Git LFS
Installing 64-bit git.install...
git.install has been installed.
git.install installed to 'C:\Program Files\Git'
  git.install can be automatically uninstalled.
Environment Vars (like PATH) have changed. Close/reopen your shell to
 see the changes (or in powershell/cmd.exe just type `refreshenv`).
 The install of git.install was successful.
  Software installed to 'C:\Program Files\Git\'

git v2.19.1 [Approved]
git package files install completed. Performing other installation steps.
 The install of git was successful.
  Software install location not explicitly set, could be in package or
  default install location if installer.

Chocolatey installed 3/3 packages.
 See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).

C:\Users\spin\Documents\Projects>refreshenv
Refreshing environment variables from registry for cmd.exe. Please wait...Finished..
~~~

~~~bash
C:\Users\spin\Documents\Projects>git --version
git version 2.19.1.windows.1
~~~

## 改行コード問題

- [windows環境の git で改行コードの自動変換に注意 - Qiita](https://qiita.com/yokoh9/items/1ec8099696ade0c1f36e)

~~~ps1
PS> git config --global core.autoCRLF false
~~~

## sshキーの設定

Windows メニューから　`Git Bash`  を起動し、 `ssh-keygen` コマンドで作成:

~~~bash
hdknr@DESKTOP-DL075EP MINGW64 ~
$ which ssh-keygen
/usr/bin/ssh-keygen

hdknr@DESKTOP-DL075EP MINGW64 ~
$ ssh-keygen.exe -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/hdknr/.ssh/id_rsa):
Created directory '/c/Users/hdknr/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /c/Users/hdknr/.ssh/id_rsa.
Your public key has been saved in /c/Users/hdknr/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:thGefkSIvAPemU4bZz/bkh7ylYJILBco3loqWAVGUZY hdknr@DESKTOP-DL075EP
The key's randomart image is:
+---[RSA 4096]----+
| .=oo.           |
| . oEo . .       |
|  . + + o .      |
| . = + * +       |
|  o = % S .      |
|.. + * X *   .   |
|o o   + = *.o    |
| .       +oB     |
|         .+..    |
+----[SHA256]-----+
~~~

- [秘密鍵・公開鍵を作成する（Win） - Qiita](https://qiita.com/reflet/items/5c6ba6e29fe8436c3185)
