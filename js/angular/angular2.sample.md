
- http://qiita.com/Yamamoto0525/items/65d5a0b36eb4dbd8079b

~~~bash
$ npm install -g angular-cli

npm ERR! fetch failed https://registry.npmjs.org/istanbul-instrumenter-loader/-/istanbul-instrumenter-loader-0.2.0.tgz
npm WARN retry will retry, error on last attempt: Error: fetch failed with status code 400
npm WARN deprecated graceful-fs@1.2.3: graceful-fs v3.0.0 and before will fail on node releases >= v7.0. Please update to graceful-fs@^4.0.0 as soon as possible. Use 'npm ls graceful-fs' to find it in the tree.
npm WARN deprecated minimatch@2.0.10: Please update to minimatch 3.0.2 or higher to avoid a RegExp DoS issue
npm WARN deprecated lodash-node@2.4.1: This package is discontinued. Use lodash@^4.0.0.
npm WARN deprecated lodash.assign@4.2.0: This package is deprecated. Use Object.assign.
npm WARN deprecated minimatch@0.3.0: Please update to minimatch 3.0.2 or higher to avoid a RegExp DoS issue
npm WARN deprecated tough-cookie@2.2.2: ReDoS vulnerability parsing Set-Cookie https://nodesecurity.io/advisories/130
/home/vagrant/.anyenv/envs/ndenv/versions/v5.12.0/bin/ng -> /home/vagrant/.anyenv/envs/ndenv/versions/v5.12.0/lib/node_modules/angular-cli/bin/ng
build:zone.js             ▀ ╢███████████████████████████████████████████████████████████
> execSync@1.0.2 install /home/vagrant/.anyenv/envs/ndenv/versions/v5.12.0/lib/node_modules/angular-cli/node_modules/execSync
> node install.js
~~~

~~~bash
$ ndenv rehash
which ng
/home/vagrant/.anyenv/envs/ndenv/shims/ng
~~~

~~~bash
$ ng new MyApp
Could not start watchman; falling back to NodeWatcher for file system events.
Visit http://ember-cli.com/user-guide/#watchman for more info.
installing ng2
  create .editorconfig
  create README.md
  create src/app/app.component.css
  create src/app/app.component.html
  create src/app/app.component.spec.ts
  create src/app/app.component.ts
  create src/app/app.module.ts
  create src/app/index.ts
  create src/app/shared/index.ts
  create src/assets/.gitkeep
  create src/assets/.npmignore
  create src/environments/environment.prod.ts
  create src/environments/environment.ts
  create src/favicon.ico
  create src/index.html
  create src/main.ts
  create src/polyfills.ts
  create src/styles.css
  create src/test.ts
  create src/tsconfig.json
  create src/typings.d.ts
  create angular-cli.json
  create e2e/app.e2e-spec.ts
  create e2e/app.po.ts
  create e2e/tsconfig.json
  create .gitignore
  create karma.conf.js
  create package.json
  create protractor.conf.js
  create tslint.json
Successfully initialized git.
Installing packages for tooling via npm.
~~~

~~~bash
npm WARN deprecated graceful-fs@1.2.3: graceful-fs v3.0.0 and before will fail on node releases >= v7.0. Please update to graceful-fs@^4.0.0 as soon a
s possible. Use 'npm ls graceful-fs' to find it in the tree.
npm WARN deprecated minimatch@2.0.10: Please update to minimatch 3.0.2 or higher to avoid a RegExp DoS issue
npm WARN deprecated lodash-node@2.4.1: This package is discontinued. Use lodash@^4.0.0.
npm WARN deprecated lodash.assign@4.2.0: This package is deprecated. Use Object.assign.
npm WARN deprecated minimatch@0.3.0: Please update to minimatch 3.0.2 or higher to avoid a RegExp DoS issue
npm WARN deprecated tough-cookie@2.2.2: ReDoS vulnerability parsing Set-Cookie https://nodesecurity.io/advisories/130
npm WARN optional Skipping failed optional dependency /chokidar/fsevents:
npm WARN notsup Not compatible with your operating system or architecture: fsevents@1.0.14
npm WARN @angular/compiler-cli@0.6.3 requires a peer of @angular/compiler@2.0.1 but none was installed.
npm WARN @angular/compiler-cli@0.6.3 requires a peer of @angular/core@2.0.1 but none was installed.
npm WARN @angular/platform-server@2.0.1 requires a peer of @angular/core@2.0.1 but none was installed.
npm WARN @angular/platform-server@2.0.1 requires a peer of @angular/common@2.0.1 but none was installed.
npm WARN @angular/platform-server@2.0.1 requires a peer of @angular/compiler@2.0.1 but none was installed.
npm WARN @angular/platform-server@2.0.1 requires a peer of @angular/platform-browser@2.0.1 but none was installed.

npm ERR! Linux 3.16.0-4-amd64
npm ERR! argv "/home/vagrant/.anyenv/envs/ndenv/versions/v5.12.0/bin/node" "/home/vagrant/.anyenv/envs/ndenv/versions/v5.12.0/bin/npm" "install"
npm ERR! node v5.12.0
npm ERR! npm  v3.8.6
npm ERR! path /vagrant/projects/fanimal/sandbox/MyApp/node_modules/esprima/bin/esvalidate.js
npm ERR! code ENOENT
npm ERR! errno -2
npm ERR! syscall chmod

npm ERR! enoent ENOENT: no such file or directory, chmod '/vagrant/projects/fanimal/sandbox/MyApp/node_modules/esprima/bin/esvalidate.js'
npm ERR! enoent ENOENT: no such file or directory, chmod '/vagrant/projects/fanimal/sandbox/MyApp/node_modules/esprima/bin/esvalidate.js'
npm ERR! enoent This is most likely not a problem with npm itself
npm ERR! enoent and is related to npm not being able to find a file.
npm ERR! enoent

npm ERR! Please include the following file with any support request:
npm ERR!     /vagrant/projects/fanimal/sandbox/MyApp/npm-debug.log

Package install failed, see above.
~~~
