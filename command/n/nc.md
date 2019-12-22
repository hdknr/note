## nc (Netcat)

- [Wikipedia](https://ja.wikipedia.org/wiki/Netcat)
- Windowsはnmapを入れるとncat.exeがインストールされます


- デフォルトTCP

~~~
$ echo "hello photon" | nc   200.100.15.33 4530
~~~

- UDP `-u`

~~~
$ echo "hello photon" | nc  -u 200.100.15.33 5055                                                                                     
~~~

## nmap

- Windows ([chocolatey](https://chocolatey.org/packages/nmap))

~~~
$ choco install nmap
~~~