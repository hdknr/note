# generate : static レンダリング

## minify

- デフォルトで クロージングタグをレンダリングしない！
- [HTML generated with `nuxt generate` don't have <head> and closing </body>,</html> tags · Issue #1199 · nuxt/nuxt.js](https://github.com/nuxt/nuxt.js/issues/1199)

nuxt.config.js:

~~~js
generate: {
    minify: {
      removeOptionalTags: false,
    },
  },
~~~