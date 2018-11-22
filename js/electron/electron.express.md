# express

## インストール

~~~bash
$ npm install express -g
$ npm install express-generator -g
~~~

~~~bash
$ express

  warning: the default view engine will not be jade in future releases
  warning: use `--view=jade' or `--help' for additional options


   create : public/
   create : public/javascripts/
   create : public/images/
   create : public/stylesheets/
   create : public/stylesheets/style.css
   create : routes/
   create : routes/index.js
   create : routes/users.js
   create : views/
   create : views/error.jade
   create : views/index.jade
   create : views/layout.jade
   create : app.js
   create : package.json
   create : bin/
   create : bin/www

   install dependencies:
     $ npm install

   run the app:
     $ DEBUG=electron:* npm start
~~~

~~~bash
$ npm install
~~~

TCP3000 で起動

~~~bash
$ npm run start

> electron@0.0.0 start /Users/hide/Documents/Boxes/ubn1804/projects/electron
> node ./bin/www

GET / 200 382.935 ms - 170
GET /stylesheets/style.css 200 11.047 ms - 111
GET /favicon.ico 404 27.075 ms - 1352
~~~

## 記事

- [Electron + Express.js のミニマム構成の Web アプリを作る - Qiita](https://qiita.com/kawanet/items/b0f000766af574bb12fb)
- [express実践入門](https://gist.github.com/mitsuruog/fc48397a8e80f051a145)
- [Electron + Express で デスクトップアプリを作る – カバの樹](https://www.kabanoki.net/1184)
