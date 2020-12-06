# tcpdump


# UDP

~~~zsh
% sudo tcpdump -i lo0 udp port 8010 -vv -X
~~~

- `-i lo0`  : ネットワークインターフェース(mac のループバック)
- `-vv` : verbose
- `-X`  : ASCII + Hex