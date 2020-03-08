# convert

- [imagemagick](../i/imagemagick.md)

## 4つのPNGをマージ

- 水平は `-append`

~~~bash
$ convert +append 455.1.png  455.2.png  455.3.png 455.4.png 455.png
.
~~~

- 垂直は `+append`

~~~bash
$ convert -gravity center -append 501.1.png  501.2.png 501.3.png  x.png
.
~~~
