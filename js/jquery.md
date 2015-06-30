~~~
> var f = function(msg){ console.log('msg=' + msg);}
undefined

> f
[Function]

> f('xxx')
msg=xxx
undefined

> (function(msg){ console.log('msg=' + msg);return true;})('hello');
msg=hello
true
~~~

~~~
(function ($){
    var dog = $('#dog');
})(jQuery);
~~~