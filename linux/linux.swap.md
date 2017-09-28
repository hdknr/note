## スワップファイル(Ubuntu)

確認:

~~~bash
$ sudo cat /proc/swaps
~~~

作成：

- 時間がかかるので`nginx` などを止める。
- `count` x `bs` で空き容量を相談して決める

~~~bash
$ sudo mkdir /var/swap/
$ sudo dd if=/dev/zero of=/var/swap/swap0 bs=2M count=512
$ sudo chmod 600 /var/swap/swap0
~~~

割り当て:

~~~bash
$ sudo mkswap /var/swap/swap0
$ sudo swapon /var/swap/swap0
~~~

~~~bash
$ free
              total        used        free      shared  buff/cache   available
Mem:        1014648      366736      407744       41584      240168      445428
Swap:       1048572      170056      878516
~~~

/etc/fstab に追加:

~~~
/var/swap/swap0 swap swap defaults 0 0
~~~
