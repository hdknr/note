# adb コマンド

- [よく使うadbのコマンド](http://qiita.com/t2low/items/cb37cec5f864c4748e14)
- [adbコマンドを利用したandroid制御まとめ ](http://qiita.com/yuki-nakamura/items/be14dcd9e47ca7cd0233)
- [package名のみからadb shell am start -nする ](http://qiita.com/mattak@github/items/41b1ce1d48ddb3b2bb4a)
- [開発中によく使用するadbコマンド](http://asnet.hatenablog.com/entry/2015/08/07/081010)
- [android adb, retrieve database using run-as](http://stackoverflow.com/questions/18471780/android-adb-retrieve-database-using-run-as)

## 例

~~~
$ adb devices
List of devices attached
356592050465307 device
~~~

## シェル

~~~
$ adb shell
shell@SH-06F:/ $
~~~

## パッケージ一覧

~~~bash
$ adb shell pm list package | head | sort

package:com.android.defcontainer
package:com.android.phone
package:com.qualcomm.fastdormancy
...
~~~

## ログ

~~~bash
$ adb logcat | grep Maps
~~~


## run-as

~~~bash
$ adb shell
shell@SH-06F:/ $ run-as jp.lafoglia.droidmap

shell@SH-06F:/data/data/jp.lafoglia.droidmap $ ls -al
drwxrwx--x u0_a283  u0_a283           2016-01-09 21:06 cache
drwxrwx--x u0_a283  u0_a283           2016-01-09 21:06 files
lrwxrwxrwx install  install           2016-01-09 21:05 lib -> /data/app-lib/jp.lafoglia.droidmap-1
drwxrwx--x u0_a283  u0_a283           2016-01-09 21:06 shared_prefs

~~~
