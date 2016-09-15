## echo バックするだけ

~~~coffee
module.exports = (robot) ->
   robot.respond /(.+)/i, (msg) ->
      msg.send "Hi, #{msg.match[1]}"
~~~      

## Javascript を呼ぶ

- [Calling JavaScript function from CoffeeScript file](http://stackoverflow.com/questions/17264752/calling-javascript-function-from-coffeescript-file)

~~~bash
$ cat scripts/app.js
~~~

~~~js
function echo (msg) {
    return "Hello, " + msg + " from Javascript.";
};
~~~

~~~coffee
app = require('./app')

module.exports = (robot) ->
    robot.respond /(.+)/i, (msg) ->
       msg.send app.echo(msg.match[1])
~~~
