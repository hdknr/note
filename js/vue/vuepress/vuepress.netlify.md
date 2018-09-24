- [Building a VuePress site with the Netlify CMS](https://www.vuejsradar.com/vuepress-netlify-cms-integration/)


ディレクトリ:

~~~
.
├── LICENSE
├── README.md
├── docs
│   ├── README.md
│   ├── test.md
│   └── welcome.md
├── netlify.toml
└── package.json
~~~

netlify.toml:

~~~toml
[build]
  command = "yarn docs:build"
  publish = "docs/.vuepress/dist/"
~~~

package.json:

~~~json
{
  "scripts": {
    "docs:dev": "vuepress dev docs",
    "docs:build": "vuepress build docs"
  },
  "devDependencies": {
    "vuepress": "^0.9.0"
  }
}
~~~

~~~bash 
$ npm install
~~~

~~~
docs/.vuepress/
├── components
│   └── PostLayout.vue
├── config.js
├── dist
│   ├── 404.html
│   ├── admin
│   │   ├── config.yml
│   │   └── index.html
│   ├── assets
│   │   ├── css
│   │   │   └── 1.styles.78550756.css
│   │   ├── img
│   │   │   └── search.83621669.svg
│   │   └── js
│   │       ├── 0.6ccd9fd9.js
│   │       └── app.6849934e.js
│   └── index.html
└── public
    ├── admin
    │   ├── config.yml
    │   └── index.html
    └── images
        ├── screen-shot-2018-05-23-at-4.02.40-pm.png
        └── vuejsradar.png

10 directories, 14 files
~~~

docs/.vuepress/config.js :

~~~js
module.exports = {
  title: 'Netlify CMS + VuePress',
  description: 'Netlify + VuePress',
  themeConfig: {
    docsDir: 'docs',
    repo: 'andreliem/vuepress-netlify-cms',
    sidebar: [
      '/',
      '/welcome',
      '/test'
    ],
    nav: [
      {
        text: 'Admin',
        link: '/admin/#/',
      }
    ]
  }
}
~~~


docs/.vuepress/public/admin/config.yml :

~~~yaml
backend:
  name: github
  repo: andreliem/vuepress-netlify-cms
  branch: master # Branch to update (optional; defaults to master)
media_folder: "docs/.vuepress/public/images"
public_folder: "docs/.vuepress/dist/"
collections:
  - name: "doc" # Used in routes, e.g., /admin/collections/blog
    label: "Doc" # Used in the UI
    folder: "docs" # The path to the folder where the documents are stored
    create: true # Allow users to create new documents in this collection
    slug: "{{slug}}" # Filename template, e.g., YYYY-MM-DD-title.md
    fields: # The fields for each document, usually in front matter
      - {label: "Title", name: "title", widget: "string"}
      - {label: "Body", name: "body", widget: "markdown"}
~~~