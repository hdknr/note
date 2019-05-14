# ip

## 外に出て行っているインターフェースのアドレスを確認

~~~bash 
$ ip route get 8.8.8.8 | head -n 1  | awk '{print $7}'
~~~