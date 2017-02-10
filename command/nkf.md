## リンク

- [文字コード変換コマンドの nkfの使い方と実例をまとめました。](http://takuya-1st.hatenablog.jp/entry/20100511/12735859530)

## --overwrite : 置き換え

~~~
$ nfk -w --overwirte hoge.php
~~~


## urlencode

~~~bash
$ echo 'テスト' | nkf -WwMQ | tr = %
%E3%83%86%E3%82%B9%E3%83%88
~~~

~~~bash
$ echo %E3%83%86%E3%82%B9%E3%83%88 | nkf -w --url-input
テスト
~~~
