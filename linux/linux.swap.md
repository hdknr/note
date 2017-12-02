## スワップファイル(Ubuntu)

確認:

~~~bash
$ sudo cat /proc/swaps

Filename                                Type            Size    Used    Priority
/var/swap/swap0                         file            1048572 0       -1
~~~

~~~bash
$ sudo swapon -s
Filename                                Type            Size    Used    Priority
/var/swap/swap0                         file            1048572 0       -1
~~~

~~~bash
$ cat /proc/meminfo | grep Swap
SwapCached:            0 kB
SwapTotal:       1048572 kB
SwapFree:        1048572 kB
~~~

~~~bash
$ free -kt
              total        used        free      shared  buff/cache   available
Mem:        8173956      581512     4888112      190496     2704332     7055820
Swap:       1048572           0     1048572
Total:      9222528      581512     5936684
~~~

~~~bash
$ vmstat 10 -S M
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0   4771    264   2376    0    0     0    13    3    3  1  0 99  0  0
 0  0      0   4771    264   2376    0    0     0     0   76   82  0  0 100  0  0
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
