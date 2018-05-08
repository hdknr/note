## ES6以前はクラスがない

- 関数オブジェクトをクラスに見立てて擬似的にクラスのようなものを実現

## prototype 

- prototype は JavaScript における親クラス、Javaで言うところの Objectクラス のようなもの
- 関数を定義すると自動的に生成される `object`

~~~js 
> function World(){}
undefined

> World.
World.__defineGetter__      World.__defineSetter__      World.__lookupGetter__
World.__lookupSetter__      World.__proto__             World.constructor
World.hasOwnProperty        World.isPrototypeOf         World.propertyIsEnumerable
World.toLocaleString        World.toString              World.valueOf

World.apply                 World.arguments             World.bind
World.call                  World.caller                World.length
World.name                  

World.prototype             

> typeof(World.prototype)
'object'
~~~

- プロトタイプにセットした関数はインスタンス間で共有される

## 例

Clock:
~~~js
> function Clock(){ this.dt = new Date();}
undefined
> Clock.prototype.now = function(){return this.dt;}
[Function]
> const c = new Clock();
undefined
> c.now()
2018-05-08T13:57:56.577Z
~~~

profile.js:

~~~js 
const Profile = (function () {

    function Profile(first_name, last_name) {
        // コンストラクタとなる関数
        this.first_name = first_name;
        this.last_name = last_name;
    }

    Profile.prototype.fullname = function () {
        // コンストラクタとなる関数にプロトタイプで fullname関数を定義(メソッド)
        return [this.last_name, this. first_name].join(' ');
    }

    return Profile;
}());

module.exports = Profile;
~~~

sample.js:

~~~js
Profile = require('./profile.js')
var p = new Profile('James', 'Bob')
console.log(p.fullname())
~~~

~~~bash 
$ node sample.js 
Bob James
~~~

## 記事

- [JavaScriptのプロトタイプからオブジェクト指向を学ぶ](https://qiita.com/takeharu/items/809114f943208aaf55b3)
- [[JavaScript] 1. クラスの定義](https://qiita.com/Koizumi-Greenwich/items/7a579c43084286dd38be)