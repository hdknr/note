# [fsck](https://git-scm.com/docs/git-fsck)

## Git: `error: remote unpack failed: eof before pack header was fully read`

~~~bash
% git push
fatal: failed to read object dec849e86d9c7218333791c588be590ce0f82bec: Input/output error
error: remote unpack failed: eof before pack header was fully read
To github.com:hdknr/hdknr.github.com.git
 ! [remote rejected]   master -> master (failed)
error: failed to push some refs to 'git@github.com:hdknr/hdknr.github.com.git'
~~~

- [git - error: remote unpack failed: eof before pack header was fully read - Stack Overflow](https://stackoverflow.com/questions/54301016/error-remote-unpack-failed-eof-before-pack-header-was-fully-read)

~~~bash
$ git fsck --full
...
dangling blob edff43ffccc85fc25c8e6a2ad1f8c08367e6d22f
dangling blob eeff80eac51c6b6bfbcd78512adcfc4be307a117
dangling blob efbfe5d76645a53ebe2493b1cb1e77ab7d0265e2
~~~

~~~bash
$ git push 
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 276 bytes | 276.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:hdknr/hdknr.github.com.git
   3f3c512a..b8f3bc9d  master -> master
~~~