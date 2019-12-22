# エラー

## Repository 'http://dl.google.com/linux/chrome/deb stable Release' changed its 'Origin' value from 'Google, Inc.' to 'Google LLC' 

~~~bash
E: Repository 'http://dl.google.com/linux/chrome/deb stable Release' changed its 'Origin' value from 'Google, Inc.' to 'Google LLC'
N: This must be accepted explicitly before updates for this repository can be applied. See apt-secure(8) manpage for details.
~~~

~~~bash
$ sudo apt update
ヒット:1 http://jp.archive.ubuntu.com/ubuntu bionic InRelease
取得:2 http://jp.archive.ubuntu.com/ubuntu bionic-security InRelease [83.2 kB]
取得:3 http://jp.archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB]
取得:4 http://jp.archive.ubuntu.com/ubuntu bionic-proposed InRelease [242 kB]                                            
無視:5 http://dl.google.com/linux/chrome/deb stable InRelease                              
取得:6 http://jp.archive.ubuntu.com/ubuntu bionic-backports InRelease [74.6 kB]             
取得:7 http://dl.google.com/linux/chrome/deb stable Release [943 B]                        
取得:8 http://dl.google.com/linux/chrome/deb stable Release.gpg [819 B]                    
E: Repository 'http://dl.google.com/linux/chrome/deb stable Release' changed its 'Origin' value from 'Google, Inc.' to 'Google LLC'
N: This must be accepted explicitly before updates for this repository can be applied. See apt-secure(8) manpage for details.
Do you want to accept these changes and continue updating from this repository? [y/N] Y
取得:9 http://dl.google.com/linux/chrome/deb stable/main amd64 Packages [1,109 B]                                                                                                                 
491 kB を 16秒 で取得しました (29.8 kB/s)                                                                                                                                                         
パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています       
状態情報を読み取っています... 完了
アップグレードできるパッケージが 208 個あります。表示するには 'apt list --upgradable' を実行してください。
~~~

