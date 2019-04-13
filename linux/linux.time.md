
## zoneinfo

- Ubuntu

~~~bash
# file /usr/share/zoneinfo/Asia/Tokyo
/usr/share/zoneinfo/Asia/Tokyo: symbolic link to '../Japan'

# file /usr/share/zoneinfo/Japan

/usr/share/zoneinfo/Japan: timezone data, version 2, 3 gmt time flags, 3 std time flags, no leap seconds, 9 transition times, 3 abbreviation chars
~~~

## タイムゾーン変更

- [【Linux】タイムゾーン(Timezone)の変更](http://qiita.com/azusanakano/items/b39bd22504313884a7c3)


Debian:

~~~bash
$ sudo dpkg-reconfigure tzdata
~~~

## datetimectl コマンド

~~~bash
$ sudo timedatectl list-timezones  | grep Tokyo
Asia/Tokyo

$ sudo timedatectl set-timezone Asia/Tokyo
~~~
