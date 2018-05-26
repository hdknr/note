## 設定

[Config Reference](https://vuepress.vuejs.org/config/#basic-config)

~~~bash 
$ touch .vuepress/config.js 
~~~

### タイトル

~~~js
module.exports = {
    title: 'こんにちは　VuePress',
    description: 'とても興味深いです'
}
~~~

開発サーバー(`vuepress dev`)の場合, サーバーレンダリングではなく、クライアントのバンドル(`/assets/js/app.js`) で設定される:

~~~bash 
$ curl http://localhost:8080/
~~~

~~~html
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
~~~

スタティック生成(`vuepress build`)すると埋められます:

~~~html 
$ more .vuepress/dist/index.html 
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>こんにちは　VuePress | Hello VuePress</title>
    <meta name="description" content="とても興味深いです">
    
    
    <link rel="preload" href="/assets/css/1.styles.813584bb.css" as="style"><link rel="preload" href="/assets/js/app.83a52e14.js" as="script"><link rel="preload" href="/assets/js/0.1775f720.js" as="script">
    <link rel="stylesheet" href="/assets/css/1.styles.813584bb.css">
  </head>
  <body>
    <div id="app" data-server-rendered="true">
        <div class="theme-container no-sidebar">
            <header class="navbar">
                <div class="sidebar-button">
                    <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" viewBox="0 0 448 512" class="icon">
                        <path fill="currentColor" d="M436 124H12c-6.627 0-12-5.373-12-12V80c0-6.627 5.373-12 12-12h424c6.627 0 12 5.373 12 12v32c0 6.627-5.373 12-12 12zm0 160H12c-6.627 0-12-5.373-12-12v-32c0-6.627 5.373-12 12-12h424c6.627 0 12 5.373 12 12v32c0 6.627-5.373 12-12 12zm0 160H12c-6.627 0-12-5.373-12-12v-32c0-6.627 5.373-12 12-12h424c6.627 0 12 5.373 12 12v32c0 6.627-5.373 12-12 12z">
                        </path>
                    </svg>
                </div>
                <a href="/" class="home-link router-link-exact-active router-link-active"><!---->
                    <span class="site-name"> こんにちは　VuePress </span>
                </a>
                <div class="links">
                    <div class="search-box">
                        <input aria-label="Search" autocomplete="off" spellcheck="false" value=""><!---->
                    </div><!---->
                </div>
            </header>
            
            <div class="sidebar-mask"></div>
            <div class="sidebar"><!----><!----></div>
            <div class="page">
                <div class="content">
                <h1 id="hello-vuepress">
                    <a href="#hello-vuepress" aria-hidden="true" class="header-anchor">#</a> Hello VuePress
                </h1>
                </div>
                <div class="content edit-link"><!----><!----> </div><!---->
            </div>
        </div>
    </div>
    <script src="/assets/js/0.1775f720.js" defer></script>
    <script src="/assets/js/app.83a52e14.js" defer></script>
  </body>
</html>
~~~