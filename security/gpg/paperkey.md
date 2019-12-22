# paperkey

- [Paperkey - an OpenPGP key archiver](http://www.jabberwocky.com/software/paperkey/)
- [Paperkey - ArchWiki](https://wiki.archlinux.jp/index.php/Paperkey)

macOS:

~~~bash
$ brew install paperkey
.
~~~

公開鍵エクスポート:

~~~bash
$ gpg -o ~/test.pub --export 9055311658955590F57BEAE5A8AE65BB2CC51F60
.
~~~

バックアップ作成:

~~~bash
$ gpg --export-secret-key 9055311658955590F57BEAE5A8AE65BB2CC51F60 | paperkey --output ~/test.paperkey
.
~~~

ファイル にリストア:

~~~bash
$ paperkey --pubring ~/test.pub --secrets ~/test.paperkey --output ~/test.pri
.
~~~

~~~bash 
$ file ~/test.pri

/Users/hide/test.pri: PGP       Secret Key - 2048b created on Sun Feb 17 20:52:26 2019 - RSA (Encrypt or Sign) e=65537 Plaintext or unencrypted data
~~~

~~~bash
$ gpg --list-packets --verbose ~/test.pri | grep user

:user ID packet: "hdknr <hdknr@hoge.co.jp>"
~~~

~/.gnupg へのインポート:

~~~bash
$ paperkey --pubring ~/test.pub --secrets ~/test.paperkey | gpg --import
.
~~~

## その他

- [GPGの秘密鍵や公開鍵のバックアップ方法](https://www.rk-k.com/archives/3351)
- [How to use OCR from the command line in Linux? - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/377359/how-to-use-ocr-from-the-command-line-in-linux)
- [macos - QR decoder that works on mac? - Stack Overflow](https://stackoverflow.com/questions/210470/qr-decoder-that-works-on-mac)
- [kaashif.co.uk: Backing up PGP private keys](https://kaashif.co.uk/2017/03/10/backing-up-pgp-private-keys/)
