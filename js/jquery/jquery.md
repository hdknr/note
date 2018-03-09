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

# Timeline

- [タイムライン系プラグイン](http://www.jqueryrain.com/demo/jquery-timeline-plugin/)
- [magnusjt/schedulerjs](https://github.com/magnusjt/schedulerjs)

# Slider

- [スライダー系プラグイン](http://www.jqueryrain.com/example/jquery-slider-slideshow/)
