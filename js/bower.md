# bower install

- npm を anyenv + ndenv でインストールしておく

~~~
$ ndenv install v0.12.4
~~~

~~~
$ which npm
/home/vagrant/.anyenv/envs/ndenv/shims/npm
~~~

- install
- オプションに-gを付けないと、そのディレクトリ内にnode_modulesができてそちらにインストールされます。


~~~
$ npm install bower -g

/home/vagrant/.anyenv/envs/ndenv/versions/0.12.0/bin/bower -> /home/vagrant/.anyenv/envs/ndenv/versions/0.12.0/lib/node_modules/bower/bin/bower
bower@1.3.12 /home/vagrant/.anyenv/envs/ndenv/versions/0.12.0/lib/node_modules/bower
├── is-root@1.0.0
├── junk@1.0.0
├── stringify-object@1.0.0
├── which@1.0.8
├── abbrev@1.0.5
├── chmodr@0.1.0
├── osenv@0.1.0
├── archy@0.0.2
├── opn@1.0.1
├── rimraf@2.2.8
├── bower-logger@0.2.2
├── lru-cache@2.5.0
├── bower-endpoint-parser@0.2.2
├── graceful-fs@3.0.5
├── lockfile@1.0.0
├── nopt@3.0.1
├── retry@0.6.0
├── tmp@0.0.23
├── q@1.0.1
├── request-progress@0.3.0 (throttleit@0.0.2)
├── semver@2.3.2
├── chalk@0.5.0 (escape-string-regexp@1.0.2, ansi-styles@1.1.0, supports-color@0.2.0, strip-ansi@0.3.0, has-ansi@0.1.0)
├── fstream@1.0.4 (inherits@2.0.1)
├── bower-json@0.4.0 (intersect@0.0.3, deep-extend@0.2.11, graceful-fs@2.0.3)
├── p-throttler@0.1.0 (q@0.9.7)
├── shell-quote@1.4.2 (array-filter@0.0.1, array-reduce@0.0.0, array-map@0.0.0, jsonify@0.0.0)
├── promptly@0.2.0 (read@1.0.5)
├── mkdirp@0.5.0 (minimist@0.0.8)
├── bower-config@0.5.2 (osenv@0.0.3, graceful-fs@2.0.3, optimist@0.6.1)
├── fstream-ignore@1.0.2 (inherits@2.0.1, minimatch@2.0.1)
├── tar-fs@0.5.2 (pump@0.3.5, tar-stream@0.4.7)
├── decompress-zip@0.0.8 (nopt@2.2.1, mkpath@0.1.0, touch@0.0.2, readable-stream@1.1.13, binary@0.3.0)
├── glob@4.0.6 (inherits@2.0.1, once@1.3.1, minimatch@1.0.0)
├── request@2.42.0 (caseless@0.6.0, json-stringify-safe@5.0.0, forever-agent@0.5.2, aws-sign2@0.5.0, stringstream@0.0.4, oauth-sign@0.4.0, tunnel-agent@0.4.0, qs@1.2.2, node-uuid@1.4.2, mime-types@1.0.2, bl@0.9.4, form-data@0.1.4, http-signature@0.10.1, tough-cookie@0.12.1, hawk@1.1.1)
├── bower-registry-client@0.2.3 (graceful-fs@2.0.3, request-replay@0.2.0, lru-cache@2.3.1, async@0.2.10, mkdirp@0.3.5, request@2.51.0)
├── cardinal@0.4.0 (redeyed@0.4.4)
├── update-notifier@0.2.0 (semver-diff@0.1.0, string-length@0.1.2, latest-version@0.2.0, configstore@0.3.2)
├── mout@0.9.1
├── handlebars@2.0.0 (optimist@0.3.7, uglify-js@2.3.6)
├── inquirer@0.7.1 (figures@1.3.5, mute-stream@0.0.4, through@2.3.6, readline2@0.1.1, lodash@2.4.1, cli-color@0.3.2, rx@2.3.25)
└── insight@0.4.3 (object-assign@1.0.0, chalk@0.5.1, async@0.9.0, lodash.debounce@2.4.1, os-name@1.0.3, tough-cookie@0.12.1, configstore@0.3.2, inquirer@0.6.0)

~~~

~~~
$ bower --version
1.3.12
~~~

# django-bower

- https://django-bower.readthedocs.org/en/latest/installation.html

~~~
$ pip install django-bower
~~~

- http://bambu-bootstrap.readthedocs.org/en/latest/#

~~~
(wordpress)vagrant@10:~/projects/pia/web$ python manage.py bower install

bower not-cached    git://github.com/FortAwesome/Font-Awesome.git#*
bower resolve       git://github.com/FortAwesome/Font-Awesome.git#*
bower not-cached    git://github.com/twbs/bootstrap.git#*
bower resolve       git://github.com/twbs/bootstrap.git#*
bower download      https://github.com/FortAwesome/Font-Awesome/archive/v4.3.0.tar.gz
bower download      https://github.com/twbs/bootstrap/archive/v3.3.2.tar.gz
bower extract       fontawesome#* archive.tar.gz
bower resolved      git://github.com/FortAwesome/Font-Awesome.git#4.3.0
bower extract       bootstrap#* archive.tar.gz
bower resolved      git://github.com/twbs/bootstrap.git#3.3.2
bower not-cached    git://github.com/jquery/jquery.git#>= 1.9.1
bower resolve       git://github.com/jquery/jquery.git#>= 1.9.1
bower download      https://github.com/jquery/jquery/archive/2.1.3.tar.gz
bower extract       jquery#>= 1.9.1 archive.tar.gz
bower resolved      git://github.com/jquery/jquery.git#2.1.3
bower install       fontawesome#4.3.0
bower install       bootstrap#3.3.2
bower install       jquery#2.1.3

fontawesome#4.3.0 bower_components/fontawesome

bootstrap#3.3.2 bower_components/bootstrap
└── jquery#2.1.3


~~~
# Link

- http://www.nishimiyahara.net/2014/03/21/171931
- [[Grunt & Yeoman] grunt-bower-task で Bower を扱いやすくレイアウトする](http://www.d-wood.com/blog/2013/11/11_5021.html)
- [bowerでインストールしたファイルの配置を設定するにはgrunt-bower-taskが便利](http://kyohei8.hatenablog.com/entry/2013/11/17/145316)
- [GruntとgulpでBower環境を作る](http://create-something.hatenadiary.jp/entry/2014/07/27/204633)
