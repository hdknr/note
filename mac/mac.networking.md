# DHCP

- [How to Renew a DHCP Lease in Mac OS X](http://osxdaily.com/2013/02/11/renew-dhcp-lease-mac-os-x/)

- en0 でDHCPの確認

```
$ ipconfig getpacket en0 | grep dhcp
dhcp_message_type (uint8): ACK 0x5
```

## ifconfig

```
$ sudo ipconfig set en0 DHCP
```

### 再起動

~~~
$ sudo ifconfig en0 down ; sudo ifconfig en0 up;
~~~

## scutil

```
$ echo "add State:/Network/Interface/en0/RefreshConfiguration temporary" | sudo scutil
```

## DNS

### キャッシュクリア

~~~zsh
% sudo killall -HUP mDNSResponder
~~~

## その他

- [macのhostnameがDHCPで上書きされる件 ](http://blog.kenichikat.org/2012/11/machostnamedhcp.html)


# Wi Fi

## 不安点

- [YosemiteにアップデートしてWi-Fiが不安定になったからやってみたこと](http://qiita.com/BeMarble/items/f22095141e734e577e79)
- [Fix Wi-Fi Problems in OS X Yosemite](http://osxdaily.com/2014/10/25/fix-wi-fi-problems-os-x-yosemite/)
