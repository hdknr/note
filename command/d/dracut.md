# dracut

~~~bash
$ sudo dracut --force --add growroot /boot/initramfs-$(uname -r).img
.
~~~

- `/boot/initramfs-$(uname -r).img` イメージを dracut で作る
- このイメージに `growroot` コマンドを追加して作成
- 次回、OSがリブートされるときに `growroot` が実行される

## 記事

- [「Amazon EC2でCentOS6を使用するときのハマリポイント」をAnsibleのPlaybookにしてみた - Qiita](https://qiita.com/sadapon2008/items/d0d1ced73c114a816802)
- [EC2 の CentOS インスタンスのルートドライブのディスク容量を増設する - Qiita](https://qiita.com/1000k/items/d3dd886beb5cf01ec734)
- [Dracutの歩き方 - ククログ(2015-06-02)](https://www.clear-code.com/blog/2015/6/2.html)
- [CentOS HVM方式のルートボリュームを拡張する。 - Qiita](https://qiita.com/kooohei/items/0bae73e5c12ad936a41a)

## 関連

- [growpart](growpart.md)
