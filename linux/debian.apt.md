## dselect

- [ListInstalledPackages](https://wiki.debian.org/ListInstalledPackages)

~~~bash
$ dpkg --get-selections | tee packages.txt
~~~

~~~bash
$ sudo apt-get install dselect
$ sudo dpkg --set-selections < packages.txt
$ apt-get dselect-upgrade
~~~

~~~bash
$ aptitude install $(cat packages.txt | awk '{print $1}')
~~~
