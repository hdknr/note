## [Getting Started](https://vuepress.vuejs.org/guide/getting-started.html)

~~~bash 
$ npm install yarn -g
~~~

~~~bash 
$ yarn global add vuepress 

yarn global v1.7.0
[1/4] 🔍  Resolving packages...
[2/4] 🚚  Fetching packages...
[3/4] 🔗  Linking dependencies...
[4/4] 📃  Building fresh packages...
success Installed "vuepress@0.10.0" with binaries:
      - vuepress
✨  Done in 38.68s.
~~~

~~~bash 
$ echo '# Hello VuePress' > README.md
~~~

~~~bash 
$ vuepress dev

  VuePress dev server listening at http://localhost:8080/
~~~

~~~bash 
$ curl http://localhost:8080/

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title></title>
  </head>
  <body>
    <div id="app"></div>
  <script type="text/javascript" src="/assets/js/app.js"></script></body>
</html>
~~~~


~~~bash 
$ vuepress build

Rendering static HTML...

Success! Generated static files in .vuepress/dist.
~~~

~~~bash 
$ tree .vuepress/

.vuepress/
└── dist
    ├── 404.html
    ├── assets
    │   ├── css
    │   │   └── 1.styles.9e0563b4.css
    │   ├── img
    │   │   └── search.83621669.svg
    │   └── js
    │       ├── 0.1775f720.js
    │       └── app.c6885314.js
    └── index.html

5 directories, 6 files

~~~

~~~bash 
$ cd .vuepress/dist/
$ python -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
~~~

~~~bash 
$ php -S localhost:8000
~~~

## トピック

- [.vuepress/config.js](vuepress.config.md)
- [Netlifyサンプル](vuepress.netlify.md)
- [markdown-it/markdown-it](https://github.com/markdown-it/markdown-it)
- [Markdownを拡張する](https://vuepress.vuejs.org/guide/markdown.html)