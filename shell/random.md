# 乱数

## `$RANDOM`

~~~bash
$ echo $((RANDOM%10000))
~~~

## /dev/random, /dev/urandom

~~~bash
$ echo $(( $(od -vAn -N4 -tu4 < /dev/random) % 5 ))
~~~
