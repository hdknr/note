## Jain環境

- main.cf でデフォルトトランスポートを定義

~~~
default_transport=jail
~~~

- master.cf で定義したトランスポートを処理するコマンド

~~~
jail unix  -       n       n       -       -       pipe
  flags=FDRq user=vagrant argv=/home/vagrant/inbound.sh $sender $recipient
~~~