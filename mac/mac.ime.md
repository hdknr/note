## 日本語入力パレットが残ったままになったら

~~~bash

$ ps ax | grep 82053
82053   ??  U      0:21.68 /System/Library/Input Methods/JapaneseIM.app/Contents/MacOS/JapaneseIM
82564 s006  R+     0:00.00 grep 82053
~~~

~~~bash
$ killall JapaneseIM
~~~
