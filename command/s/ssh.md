# ssh

- [sftp](sftp.md)

## ssh ログインした IP アドレス記録

- Debian

```bash
$ zgrep sshd /var/log/auth.log* | grep "Accepted publickey for admin" | sed -re 's/.*from ([^: ]+).*/\1/' | sort -u | while read ip;do echo $ip `dig +short -x $ip`;done
154.167.141.179 p5491179-ipngn1402marunouchi.tokyo.ocn.ne.jp.
157.168.71.211 p7957211-ipngn1702marunouchi.tokyo.ocn.ne.jp.
222.229.233.5 p82335-ipbffx32marunouchi.tokyo.ocn.ne.jp.
```

## ネットワークを変えたら接続できなくなった

/etc/hosts.allow で日本ネットワークのみ許可制限がはいっているとか:

```
sshd: .jp
```

## autossh

- [ssh 接続を維持し続ける autossh の使い方](https://www.xmisao.com/2013/07/16/autossh-how-to.html)
- [autossh をサービス化して SSH 接続を強化](https://remoteroom.jp/diary/2019-07-18/)

```bash
brew install autossh        # macOS
apt install autossh     # debian/ubuntu
```

## タイムアウト

クライアント:

- ServerAliveInterval (null パケット送信間隔)
- ServerAliveCountMax (null パケットの戻りを待つ回数)

## 記事

- [ssh ポートフォワーディング - Qiita](https://qiita.com/mechamogera/items/b1bb9130273deb9426f5)
- [混乱しがちな「SSH トンネルの確立方法」をイメージ図とセットでまとめたコマンド集](https://gigazine.net/news/20210209-ssh-tunnel/)
- [自分のリバース SSH トンネルサーバーを立てましょう](https://kojichu.photoruction.com/entry/2022/08/08/093500)
- [sish: An open source serveo/ngrok alternative](https://github.com/antoniomika/sish)
- [SSH 接続でのタイムアウト対策](https://zenn.dev/syommy_program/articles/c7bd0d0daa156c)
