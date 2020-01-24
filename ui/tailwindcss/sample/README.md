# サンプル

- https://tailwindcss.com/docs/installation/

インストール:

~~~bash 
$ npm install tailwindcss
~~~

[tailewind.config.js]の作成と編集(オプション):

~~~bash
$ npx tailwind init
$ vim tailwind.config.jp
~~~

[styles.css](styles.css) を定義:

~~~css
@tailwind base;

@tailwind components;

@tailwind utilities;
~~~

ビルド:

~~~bash
$ npx tailwind build styles.css -o output.css
~~~
