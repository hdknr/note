# Windows 


## 最初にやること

### リモートログインユーザーでオートログイン設定

- Windows Server 2012 R2 のドメインコントローラではうまくいっていません (> <)

~~~
C:\> regedit
~~~

- キーに移動

~~~
HKLM\Software\Microsoft\Windows NT\CurrentVersion\winlogon 
~~~

- REG_SZ を設定

~~~
AutoAdminLogon = "1"            # Enabled  (Zero would mean turn off)
DefaultUserName = "Guyt"        # (Your logon username)
DefaultPassword = "Passw0rd"    # (Remember this or change)
DefaultDomainName = "dom.com"   # (Only needed if this computer has joined a domain)
~~~

- サブキーがあったら削除

~~~
AutoLogonChecked
AutoLogonCount
~~~


- オートログインがされていないと、MacからRDPしたときに、USキー配列になります。
- この場合、WindowsでRDPするとかHyper-Vマネージャーで接続してログインするとかしておくことが必要

### IMEのOn/Offのキーバインド変更

- Mac からRDPした時に困らないように
- Ctrl + '/' とか
- コントロールパネルで　"IME"で検索
- Microsoft IMEの設定(日本語)
- 詳細設定、全般操作、編集操作、キー設定で、「変更」
- "IME-オン/オフ" のキーを変更

### RDP


- Windows でRDP管理を有効にすること
- App Store でインストール
- デバイスマネージャから、リモートデスクトップキーボードを 日本語 106/109 に変更 (Windows Server 2012 R2で意味があるかどうかよく分からない)

- 右クリック: Macの設定。Magic Mouseだと副ボタンの設定。


### chocolatey 

- http://chocolatey.org/  でインストール

### AutoHotKey

- Appleのキーボードを繋いだ時(RDP経由だと意味ないような)

~~~
C:\> choco install autohotkey
~~~

- Mac Keyboard

~~~
    ;Mac keyboard
    #USEHOOK
    vkE9sc071 Up::Send,{vkF3sc029 Down}{VkF3sc029 Up}  ;Apple英数->半全
    vkFFsc072 Up::Send,{vkF3sc029 Down}{VkF3sc029 Up}  ;Appleかな->半全
    #USEHOOK off﻿
~~~

### vim

~~~
C:\> choco install vim
~~~

- $HOME\_vimrc

~~~
set iminsert=0
set imsearch=-1
~~~

### WinScp


~~~
C:\> choco install winscp
~~~

