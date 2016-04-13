~~~bash
$ npm install gitbook-cli -g
/Users/hide/.anyenv/envs/ndenv/versions/v0.12.7/bin/gitbook -> /Users/hide/.anyenv/envs/ndenv/versions/v0.12.7/lib/node_modules/gitbook-cli/bin/gitbook.js
gitbook-cli@2.1.3 /Users/hide/.anyenv/envs/ndenv/versions/v0.12.7/lib/node_modules/gitbook-cli
├── bash-color@0.0.3
├── user-home@2.0.0 (os-homedir@1.0.1)
├── q@1.4.1
├── semver@5.1.0
├── commander@2.9.0 (graceful-readlink@1.0.1)
├── tmp@0.0.28 (os-tmpdir@1.0.1)
├── optimist@0.6.1 (wordwrap@0.0.3, minimist@0.0.10)
├── fs-extra@0.26.5 (path-is-absolute@1.0.0, klaw@1.1.3, jsonfile@2.2.3, graceful-fs@4.1.3, rimraf@2.5.2)
├── lodash@4.5.1
├── npm@3.7.5
└── npmi@1.0.1 (semver@4.3.6, npm@2.15.3)
~~~

~~~bash
$ `ndenv which gitbook` init                                                                                         [1/1886]
Installing GitBook 2.6.7
  SOLINK_MODULE(target) Release/.node
  CXX(target) Release/obj.target/fse/fsevents.o
  SOLINK_MODULE(target) Release/fse.node
gitbook@2.6.7 ../../../../../var/folders/3n/0lk686q1129clzkw38blpwdc0000gp/T/tmp-82714BhWnPuacA9Hp/node_modules/gitbook
├── bash-color@0.0.3
├── escape-string-regexp@1.0.3
├── nunjucks-filter@1.0.0
├── spawn-cmd@0.0.2
├── gitbook-plugin-livereload@0.0.1
├── gitbook-plugin-sharing@1.0.1
├── github-slugid@1.0.0
├── nunjucks-autoescape@1.0.0
├── gitbook-plugin-fontsettings@1.0.2
├── json-schema-defaults@0.1.1
├── graceful-fs@3.0.5
├── jsonschema@1.0.2
├── crc@3.2.1
├── tmp@0.0.24
├── q@1.0.1
├── semver@5.0.1
├── dom-serializer@0.1.0 (domelementtype@1.1.3, entities@1.1.1)
├── resolve@0.6.3
├── urijs@1.17.0
├── send@0.2.0 (fresh@0.2.4, range-parser@1.0.3, mime@1.2.11, debug@2.2.0)
├── npmi@0.1.1 (semver@4.3.6)
├── i18n@0.5.0 (sprintf@0.1.5, debug@2.2.0, mustache@2.2.1)
├── fs-extra@0.16.5 (jsonfile@2.2.3, rimraf@2.5.2)
├── fstream-ignore@1.0.2 (inherits@2.0.1, minimatch@2.0.10, fstream@1.0.8)
├── tiny-lr@0.2.1 (parseurl@1.3.1, debug@2.2.0, qs@5.1.0, livereload-js@2.2.2, faye-websocket@0.10.0, body-parser@1.14.2)
├── request@2.51.0 (caseless@0.8.0, forever-agent@0.5.2, aws-sign2@0.5.0, oauth-sign@0.5.0, stringstream@0.0.5, tunnel-agent@0.4.2, json-stringify-
safe@5.0.1, qs@2.3.3, node-uuid@1.4.7, mime-types@1.0.2, combined-stream@0.0.7, tough-cookie@2.2.2, bl@0.9.5, form-data@0.2.0, http-signature@0.10.
1, hawk@1.1.1)
├── merge-defaults@0.2.1 (lodash@2.4.2)
├── nunjucks@2.2.0 (asap@2.0.3, optimist@0.6.1)
├── cheerio@0.19.0 (entities@1.1.1, css-select@1.0.0, htmlparser2@3.8.3)
├── gitbook-plugin-highlight@1.0.3 (highlight.js@8.8.0)
├── lodash@3.10.1
├── gitbook-plugin-search@1.1.0 (lunr@0.5.12)
├── juice@1.5.0 (commander@2.3.0, batch@0.5.2, slick@1.12.1, cssom@0.3.0, web-resource-inliner@1.1.4)
├── gitbook-parsers@0.8.9 (gitbook-restructuredtext@0.2.3, q@1.4.1, gitbook-markdown@0.5.3, gitbook-asciidoc@0.2.4)
├── chokidar@1.0.6 (path-is-absolute@1.0.0, arrify@1.0.1, is-glob@1.1.3, async-each@0.1.6, is-binary-path@1.0.1, glob-parent@1.3.0, readdirp@1.4.0,
 anymatch@1.3.0, fsevents@0.3.8)
└── npm@2.4.1

info: init book at /Users/hide/Dropbox/アプリ/scriptogram 
info: detect structure from SUMMARY (if it exists) 
info: create SUMMARY.md 
info: found README.md 
info: initialization is finished 

Done, without error

~~~

~~~bash

$ `ndenv which gitbook` build
info: loading book configuration....OK 
info: load plugin gitbook-plugin-highlight ....OK 
info: load plugin gitbook-plugin-search ....OK 
info: load plugin gitbook-plugin-sharing ....OK 
info: load plugin gitbook-plugin-fontsettings ....OK 
info: >> 4 plugins loaded 
info: start generation with website generator 
info: clean website generatorOK 
info: generation is finished 

Done, without error
~~~