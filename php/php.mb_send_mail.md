# mb_send_mail

- [mb_send_mail](http://php.net/manual/ja/function.mb-send-mail.php)
- `sendmail` コマンドをよびだしている

## PHP.INI の設定

~~~bash 
$ vi $(phpenv prefix)/etc/php.ini
~~~

Ubuntu:

~~~ini
sendmail_path = /usr/sbin/sendmail -t -i
~~~

## `sender` を設定して送信

- [sendmail.sendmail(8) - Linux man page](https://linux.die.net/man/8/sendmail.sendmail)

~~~php
<?php
      mb_language("ja");
      mb_internal_encoding("utf-8");
      $to = 'hdknr@twitter.com';
      $subject = 'test subject';

      $msg = 'test message';
      $from = "hdknr@instagram.com";
      $header="From: {$from}\nReply-To: {$from}\nContent-Type: text/plain;";
      $opt = "-f {$from}";              # sender を指定する
      $ret = mb_send_mail($to,$subject,$msg,$header, $opt);
      var_dump($ret);
?>