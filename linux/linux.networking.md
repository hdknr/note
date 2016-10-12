
# 帯域制御

## trickle

- [Trickleを使って帯域制限をする](http://apatheia.info/blog/2013/01/01/network-restriction-using-trickle/)
- [[Linux]trickleを使ってプログラムごとにアドホックに帯域制御する](https://siguniang.wordpress.com/2015/05/17/throttle-network-bandwidth-per-program-with-trickle/)

~~~bash
$ trickle -u 2000 aws s3 cp /path/to/upload s3://bucketname/to/
~~~
