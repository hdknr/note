パフォーマンス系の話

# kswapd0:  ロードアベレージが高い

- [kswapd0 プロセスが CPU を食ってた](https://memo.ecp.plus/kswapd0/)
- [/proc/sys/vm/drop_caches (Linux 2.6.16 以降)](http://pooh.gr.jp/?p=5477)

vm.drop_caches
- 0: 初期値
- 1: ページキャッシュ解放
- 2: dentry、inode 解放
- 3: ページキャッシュ、dentry、inode 解放


ページキャッシュだけ解放:

~~~bash
$ sudo sync && sudo /sbin/sysctl -w vm.drop_caches=1
~~~

~~~bash
$ free
              total        used        free      shared  buff/cache   available
Mem:        1014496      271272      636592       10860      106632      692196
Swap:             0           0           0
~~~
