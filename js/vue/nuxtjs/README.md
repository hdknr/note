# nuxt.js

- [#72](https://github.com/hdknr/scriptogr.am/issues/72)
- https://nuxtjs.org/
- [next.js](https://github.com/zeit/next.js)(react の SSR(Server Side Rendering)) のインスパイア

## アーキテクチャ

- [asyncData](nuxtjs.asyncdata.md)
- [ルーティング](nuxtjs.routes.md)

## Topic

- [JAMStack](jamstack.md)
- [インストール](nuxtjs.install.md)
- [認証](nuxtjs.auth.md)
- [ホストとポート番号を変更するには？](https://ja.nuxtjs.org/faq/host-port/)

~~~bash
$ npm install --save-dev cross-env
~~~

packages.json:

~~~js
"scripts": {
  "dev": "cross-env HOST=0.0.0.0 PORT=3333 nuxt"
}
~~~

~~~bash
$ npm run dev

> ssr@1.0.0 dev /vagrant/projects/nuxts/ssr
> cross-env HOST=0.0.0.0 PORT=3333 nuxt
....
~~~

- [django](https://github.com/nuxt/nuxt.js/issues?utf8=%E2%9C%93&q=is%3Aissue%20django)

## nginx

- [How to set up Nuxt.js with Nginx](https://github.com/nuxt/nuxt.js/issues/493)

## 記事

- [SEO、OGP……Vue.js製SPAの「困った」を解決できる「Nuxt.js」が便利だ！](https://www.webprofessional.jp/nuxt-js-universal-vue-js/)
- [【Nuxt.js】Vue.js + SSR を利用したWebサイトコーディングの可能性](https://grow-group.jp/archives/554/)
- [Nuxt.jsとLaravelを使ってTwitterログイン機能を実装する](https://qiita.com/hareku/items/ea09602bf40bf0a42040)
- [マイクロサービスを作るのに、nuxt.jsが最高だった話](https://qiita.com/tkow/items/c869e7a69665ddc7305d)
- [Nuxt.jsとFirebaseを組み合わせて爆速でWebアプリケーションを構築する](https://qiita.com/potato4d/items/cfddeb8732fec63cb29c)
- [Vue.jsでサーバサイドレンダリングしたい](https://qiita.com/kurosame/items/9815a28820e5e63d1a55)
- [Vue.jsでSSR（サーバサイドレンダリング）する](https://qiita.com/namazu510/items/e699afb2fb8161cbac2e)

SMACSS(Scalable and Modular Architecture for CSS):

- [SMACSS+BEMによるテーマ設計（for Drupal8）](https://qiita.com/J_Sugar__/items/9adee163028c9910fbc6)


BEM(Block/Element/Modifier):

- [より良いCSSを書くための様々なCSS設計まとめ](http://uxmilk.jp/43386)

FLOCSS(Foundation/Layout/Object CSS):

- MindBEMding
- [hiloki/flocss](https://github.com/hiloki/flocss)
- [OOCSS BEM SMACSS FLOCSS 違い 無料](http://feb19.jp/blog/archives/000276.php)


PRPL(Push/Render/Pre-cache/Lazy-load):

- [Googleが新たに提唱するProgressive Web Appsの新たな開発パターン「PRPL」とは？](https://html5experts.jp/komasshu/19704/)
