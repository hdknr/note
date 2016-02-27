~~~
adb install -r DeviceInfoViewer2.apk
~~~

~~~
$ adb devices
List of devices attached
356592050465307 device
~~~

~~~
$ adb -s 356592050465307 install -r ~/Downloads/app.0218.1.apk
5216 KB/s (49450732 bytes in 9.257s)
        pkg: /data/local/tmp/app.0218.1.apk
Success
~~~
