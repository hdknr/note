## Magic Method

[コンストラクタ](https://secure.php.net/manual/ja/language.oop5.decon.php#object.construct)
-  `__construct()`  
-  `__destruct()`

[メソッドオーバーロード](https://secure.php.net/manual/ja/language.oop5.overloading.php#object.call)
-  `__call()`
-  `__callStatic()`

[プロパティオーバーロード](https://secure.php.net/manual/ja/language.oop5.overloading.php#language.oop5.overloading.members)
-  `__get()`
-  `__set()`
-  `__isset()`
-  `__unset()`


[スリープ](https://secure.php.net/manual/ja/language.oop5.magic.php#object.sleep)

-  `__sleep()`
-  `__wakeup()`

[文字列キャスト](https://secure.php.net/manual/ja/language.oop5.magic.php#object.tostring)

-  `__toString()`

[コール](https://secure.php.net/manual/ja/language.oop5.magic.php#object.invoke)

-  `__invoke()`

[文字列化(var_export)](https://secure.php.net/manual/ja/language.oop5.magic.php#object.invoke)

-  `__set_state()`

[シャローコピー](https://secure.php.net/manual/ja/language.oop5.cloning.php#object.clone)

-  `__clone() `

[var_dump](https://secure.php.net/manual/ja/language.oop5.magic.php#object.debuginfo)
-  `__debugInfo() `


## `__call` / `__callStatic`

~~~php
<?php
class dog {
    function __call($function, $args) {
        $args = implode(', ', $args);
        print "Call to $function() method with args '$args' failed!\n";
    }
    static function __callStatic($function, $args){
        $args = implode(', ', $args);
        print "Call to $function() static method with args '$args' failed!\n";
    }
}

$poppy = new dog;
$poppy->meow("foo", "bar", "baz");
dog::meow("i" , "my", "me");
~~~

~~~bash
$ php call.php
Call to meow() method with args 'foo, bar, baz' failed!
Call to meow() static method with args 'i, my, me' failed!
~~~

### python

~~~py
class MetaDog(type):
    def __getattr__(cls, name):
        return {
            "meow": lambda *args: "classmethod neow() :" + ",".join(args)
        }.get(name, lambda *args: '')


class Dog:
    __metaclass__ = MetaDog

    def __getattr__(self, name):
        return {
            "meow": lambda *args: "instancemethod neow() :" + ",".join(args)
        }.get(name, lambda *args: '')

dog = Dog()
print dog.meow("i", "my", "me")
print Dog.meow("you", "your", "you")
~~~

~~~bash
$ python call.py
instancemethod neow() :i,my,me
classmethod neow() :you,your,you
~~~
