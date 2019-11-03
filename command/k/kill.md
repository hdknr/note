## すべてのゾンビをkill

~~~bash
$ kill -9 $(ps -A -ostat,ppid | grep -e '[zZ]'| awk '{ print $2 }')
~~~
