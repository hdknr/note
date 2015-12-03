## unmet dependency

- [npm WARN unmet dependency発生したら。](https://www.wantedly.com/techniques/2700)

~~~bash$

npm update -g npm

/home/vagrant/.anyenv/envs/ndenv/versions/0.12.0/bin/npm -> /home/vagrant/.anyenv/envs/ndenv/versions/0.12.0/lib/node_modules/npm/bin/npm-cli.js

npm WARN unmet dependency /home/vagrant/.anyenv/envs/ndenv/versions/0.12.0/lib/node_modules/npm/node_modules/columnify requires strip-ansi@'^2.0.0' but will load
~~~

~~~bash
$ npm cache clean
$ npm cache clean -g
~~~

~~~
bash$ npm outdated -g

Package  Current  Wanted  Latest  Location
jquery     2.1.3   2.1.4   2.1.4  
jsdom      4.0.1   7.1.0   7.1.0  
npm        3.5.1   3.5.1   3.5.0  
~~~
