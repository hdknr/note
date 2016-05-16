mkdocs: HTMLの生成の仕組み

- [build.py](https://github.com/mkdocs/mkdocs/blob/master/mkdocs/commands/build.py)

## ドキュメントルート

~~~bash
$ ls mkdocs.yml
mkdocs.yml

$ ipython
~~~

## config をロードする

~~~python
In [1]: from mkdocs.config import load_config
In [2]: conf = load_config()
In [4]: type(conf)
Out[4]: instance
Out[5]:
['__cmp__',
 '__contains__',
 '__delitem__',
 '__doc__',
 '__getitem__',
 '__hash__',
 '__init__',
 '__len__',
 '__module__',
 '__repr__',
 '__setitem__',
 '_post_validate',
 '_pre_validate',
 '_schema',
 '_schema_keys',
 '_validate',
 'clear',
 'copy',
 'data',
 'fromkeys',
 'get',
 'has_key',
 'items',
 'iteritems',
 'iterkeys',
 'itervalues',
 'keys',
 'load_dict',
 'load_file',
 'pop',
 'popitem',
 'set_defaults',
 'setdefault',
 'update',
 'user_configs',
 'validate',
 'values']
~~~

~~~python
In [8]: type(conf['pages'])
Out[8]: list

In [9]: conf['use_directory_urls']
Out[9]: True
~~~

## ドキュメント一覧を作成する

~~~py
In [10]: from mkdocs import nav

In [11]: site_navigation = nav.SiteNavigation(conf['pages'], conf['use_directory_urls'])

In [12]: type(site_navigation)
Out[12]: mkdocs.nav.SiteNavigation
~~~

## Jinja2のローダー

~~~py
In [14]: import jinja2
In [15]: loader = jinja2.FileSystemLoader(conf['theme_dir'] + [conf['mkdocs_templates'], ])

In [16]: type(loader)
Out[16]: jinja2.loaders.FileSystemLoader
~~~

### Jinja2の環境

~~~py
In [17]: env = jinja2.Environment(loader=loader)

In [18]: type(env)
Out[18]: jinja2.environment.Environment
~~~


## ナビゲーションからMarkdownページの取得

~~~py
In [20]: site_navigation.walk_pages()
Out[20]: <generator object walk_pages at 0x105c32eb0>

In [21]: _.next()
Out[21]: <mkdocs.nav.Page at 0x105abb710>

In [22]: page = _
~~~

### Markdownのパス

~~~py
In [24]: import os
In [25]: input_path = os.path.join(conf['docs_dir'], page.input_path)
In [27]: input_path
Out[27]: u'/Users/hide/Dropbox/\u30a2\u30d5\u309a\u30ea/scriptogram/index.md'
~~~

## Markdownを読み込む

~~~py
In [29]: import io

In [30]: input_content = io.open(input_path, 'r', encoding='utf-8').read()
~~~

## MarkdownをHTML化

### 拡張など設定

~~~py
In [31]: from mkdocs import utils
In [32]: from mkdocs.relative_path_ext import RelativePathExtension
In [33]: extensions = [RelativePathExtension(site_navigation, conf['strict'])] + conf['markdown_extensions']

In [34]: extensions
Out[34]:
[<mkdocs.relative_path_ext.RelativePathExtension at 0x105c3fdd0>,
 u'meta',
 u'toc',
 u'tables',
 u'fenced_code']
~~~

### Markdwon -> HTML

~~~py
In [35]: md = utils.convert_markdown(markdown_source=input_content, extensions=extensions,  extension_configs=conf['mdx_configs'])


In [37]: len(md)
Out[37]: 3

In [38]: [type(i) for i in md]
Out[38]: [unicode, mkdocs.toc.TableOfContents, dict]
~~~

### HTML, TOC, メタデータに分解

~~~py
In [41]: html_content, table_of_contents, meta = md
~~~

## コンテキスト

### グローバルコンテキスト

~~~py
In [43]: from mkdocs.commands.build import get_global_context
In [44]: context = get_global_context(site_navigation, conf)
In [46]: type(context)
Out[46]: dict
~~~


### ページコンテキスト

~~~py
In [47]: from mkdocs.commands.build import get_page_context
In [49]: page_context = get_page_context(page, html_content, table_of_contents, meta, conf)
In [50]: type(page_context)
Out[50]: dict


In [51]: context.update(page_context)
~~~

## レンダリング

### テンプレートを使ってHTMLページ化

~~~py
In [53]: template = env.get_template('base.html')
In [54]: output_content = template.render(context)
~~~

### ファイル出力

~~~py
In [57]: output_path = os.path.join(conf['site_dir'], page.output_path)

In [58]: output_path
Out[58]: u'/Users/hide/Dropbox/\u30a2\u30d5\u309a\u30ea/build/index.html'

In [59]: utils.write_file(output_content.encode('utf-8'), output_path)
~~~

## Markdown変換の実際

- [Available Extensions](https://pythonhosted.org/Markdown/extensions/index.html)


~~~py
In [9]: from markdown.extensions import meta, toc, tables, fenced_code
~~~

~~~py
In [10]: import markdown
In [11]: md = markdown.Markdown(extensions=[u'meta', u'toc', u'tables', u'fenced_code'], extension_configs={})
~~~

~~~py
In [12]: markdown_source = "# Markdown"
In [13]: html_content = md.convert(markdown_source)
In [14]: print html_content
<h1 id="markdown">Markdown</h1>
~~~
