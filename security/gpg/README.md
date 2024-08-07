# gpg

~~~bash 
$ sudo apt install gnupg gnupg-agent gpgsm
.
~~~

## キー生成

### エントロピー

~~~bash
$ sudo apt-get install rng-tools
.
~~~

~~~bash
$ sudo rngd -r /dev/urandom
.
~~~

### 生成

~~~bash
sugar@wzy:~$ gpg --gen-key

gpg (GnuPG) 1.4.12; Copyright (C) 2012 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it. 
There is NO WARRANTY, to the extent permitted by law.

gpg: ディレクトリー「/home/bobby/.gnupg」ができました
gpg: 新しい構成ファイル「/home/bobby/.gnupg/gpg.conf」ができました
gpg: 警告: 「/home/bobby/.gnupg/gpg.conf」のオプションは起動している間、有効になりません
gpg: 鍵輪「/home/bobby/.gnupg/secring.gpg」ができました
gpg: 鍵輪「/home/bobby/.gnupg/pubring.gpg」ができました
ご希望の鍵の種類を選択してください: 
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (署名のみ) 
   (4) RSA (署名のみ) 
選択は? 4 
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048) 
要求された鍵長は2048ビット
鍵の有効期限を指定してください。
         0 = 鍵は無期限
      <n>  = 鍵は n 日間で満了
      <n>w = 鍵は n 週間で満了
      <n>m = 鍵は n か月間で満了
      <n>y = 鍵は n 年間で満了
鍵の有効期間は? (0)1y
Key expires at 2015年12月11日 16時17分10秒 JST 
これで正しいですか? (y/N) y

あなたの鍵を同定するためにユーザーIDが必要です。
このソフトは本名、コメント、電子メール・アドレスから
次の書式でユーザーIDを構成します: 
    "Heinrich Heine (Der Dichter) <heinrichh@duesseldorf.de>"

本名: bobby brown
電子メール・アドレス: bobby@ic-tact.co.jp
コメント: bobby
次のユーザーIDを選択しました: 
    “bobby brown(bobby) <bobby@ic-tact.co.jp>”

名前(N)、コメント(C)、電子メール(E)の変更、またはOK(O)か終了(Q)? O
秘密鍵を保護するためにパスフレーズがいります。

(ここでパスワード入力と再入力)

今から長い乱数を生成します。キーボードを打つとか、マウスを動かす
とか、ディスクにアクセスするとかの他のことをすると、乱数生成子で
乱雑さの大きないい乱数を生成しやすくなるので、お勧めいたします。
........+++++
.+++++
gpg: /home/bobby/.gnupg/trustdb.gpg: 信用データベースができました
gpg: 鍵1EA6114Dを絶対的に信用するよう記録しました
公開鍵と秘密鍵を作成し、署名しました。

gpg: 信用データベースの検査
gpg: 最小の「ある程度の信用」3、最小の「全面的信用」1、PGP信用モデル
gpg: 深さ: 0  有効性:   1  署名:   0  信用: 0-, 0q, 0n, 0m, 0f, 1u
gpg: 次回の信用データベース検査は、2015-12-11です
pub   2048R/1EA6114D 2014-12-11 [満了: 2015-12-11]
                 指紋 = 2FFE DCF5 411E 5293 2DD9  3B37 0C76 DA1E 1EA6 114D
uid                  bobby brown (bobby) <bobby@ic-tact.co.jp>

Note that this key cannot be used for encryption.  You may want to use
the command "--edit-key" to generate a subkey for this purpose.
~~~

~~~bash
$ tree -a .gnupg
.gnupg
├── gpg.conf
├── pubring.gpg
├── pubring.gpg~
├── random_seed
├── secring.gpg
└── trustdb.gpg

0 directories, 6 files
~~~

## プライベートキー一覧

~~~bash
$ gpg --list-secret-keys

/home/boby/.gnupg/secring.gpg
------------------------------
sec   2048R/3B159704 2013-11-15 [満了: 2014-11-29]
uid                  boby (hidelafoglia) <boby@ic-tact.co.jp>
ssb   2048R/36E5A3B7 2013-11-15

sec   2048R/44773BA3 2013-11-15 [満了: 2014-12-10]
uid                  boby (hidelafoglia) <boby@ic-tact.co.jp>
ssb   2048R/BFCEA558 2013-11-15
~~~

## パブリックキー一覧

~~~bash
$ gpg --list-key

/home/bobby/.gnupg/pubring.gpg
------------------------------
pub   2048R/3B159704 2013-11-15 [満了: 2014-11-29]
uid                  bobby (hidelafoglia) <bobby@ic-tact.co.jp>

pub   2048R/44773BA3 2013-11-15 [満了: 2014-12-10]
uid                  bobby (hidelafoglia) <bobby@ic-tact.co.jp>
~~~

## キーの管理

| コマンド	                     |   説明                        |
| ----------------------------- | ----------------------------- |
| gpg --gen-key	                | 新規キーの生成 |
| gpg --gen-revoke my_user_ID   | my_user_ID に関するリボークキーを生成 |
| gpg --edit-key user_ID        | インタラクティブにキーを編集、ヘルプは "help" |
| gpg -o file --export	        | 全てのキーをファイルにエクスポート |
| gpg --import file	            | 全てのキーをファイルからインポート |
| gpg --send-keys user_ID       | user_ID のキーをキーサーバーに送信 |
| gpg --recv-keys user_ID       | user_ID のキーをキーサーバーから受信 |
| gpg --list-keys user_ID       | user_ID のキーをリスト |
| gpg --list-sigs user_ID       | user_ID の署名をリスト |
| gpg --check-sigs user_ID      | user_ID の署名をチェック |
| gpg --fingerprint user_ID	    | user_ID のフィンガープリントをチェック |
| gpg --refresh-keys            | ローカルキーリングをアップデート |

## トラストコード

| コード    | 信用の説明 |
| -------- | --------------------------- |
| `-`      | 所有者への信用未付与/未計算 |
| e	       | 信用計算に失敗 |
| q        | 計算用の情報不十分 |
| n        | このキーを信用不可 |
| m	       | スレスレの信用 |
| f	       | フルに信用 |
| u	       | 究極の信用 |

## ファイル操作

| コマンド	                    | 説明        |
| ---------------------------- | ---------- |
| gpg -a -s file               | ファイルを ASCII 文字化した file.asc と署名 |
| gpg --armor --sign file      |  |
| gpg --clearsign file         | メッセージをクリアサイン |
| gpg --clearsign file|mail foo@example.org	    | foo@example.org にクリアサインされたメッセージをメールする |
| gpg --clearsign --not-dash-escaped patchfile  | パッチファイルをクリアサイン |
| gpg --verify file	           | クリアサインされたファイルを確認 |
| gpg -o file.sig -b file      | 署名を別ファイルで作成 |
| gpg -o file.sig --detach-sig file	 |   |
| gpg --verify file.sig file   | file.sig を使ってファイルを確認 |
| gpg -o crypt_file.gpg -r name -e file	        | file からバイナリー crypt_file.gpg への name 宛公開キー暗号化 |
| gpg -o crypt_file.gpg --recipient name --encrypt file  | |
| gpg -o crypt_file.asc -a -r name -e file               | file から ASCII 文字化された crypt_file.asc への name 宛公開キー暗号化 |
| gpg -o crypt_file.gpg -c file                          | file からバイナリー crypt_file.gpg への対称暗号化 |
| gpg -o crypt_file.gpg --symmetric file                 |  |
| gpg -o crypt_file.asc -a -c file                       | file から ASCII 文字化された crypt_file.asc への対称暗号化 |
| gpg -o file -d crypt_file.gpg -r name	                 | 暗号解読 |
| gpg -o file --decrypt crypt_file.gpg                   |  |

## トピック

- [~.gnupg](files.md)

## 記事

- [GPG でファイルをパスワードで暗号化(共通鍵暗号)するときの簡易コマンド一覧](https://qiita.com/TsutomuNakamura/items/e3e9e065454d031d85f7)
