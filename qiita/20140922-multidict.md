MultiDict: クローラでフォームPOSTする時にはまるなど

# MultiDict

複数選択があり得るので、[werkzeug](http://werkzeug.pocoo.org/) のMultiDictを使ってみる:

```
$ pip install werkzeug
```

リストからdict:

```py
>>> from werkzeug.datastructures import MultiDict
>>> MultiDict([('a',1), ('a', 2), ('a', 3)])
MultiDict([('a', 1), ('a', 2), ('a', 3)])
```

追加:

```py
>>> d.update({'a': '4'})
>>> d
MultiDict([('a', 1), ('a', 2), ('a', 3), ('a', '4')])
```

更新

```py
>>> d['a']=5
>>> d
MultiDict([('a', 5)])
```


# BeautifulSoupでフォームデータを取得

[BeautifulSoupのselect()](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors)でHTMLからフォームを取得:

```py
    def form_data(self, form_node):
        ''' form_node : HTMLからselect()したformノード
        '''

        data = MultiDict(list(
           (t['name'], t.get('value', '')) 
           for i in ['text', 'hidden', 'password', ]
           for t in form_node.select('input[type=%s]' % i)
        ) + list(
           (t['name'], t.text) 
           for t in form_node.select('textarea')
        ) + list(
           (t['name'], t.get('value', '')) 
           for t in form_node.select('input[checked]' % i)
        ) + list(
            (s.parent['name'], s.get('value', s.text))
            for s in form_node.select('option[selected]')
        ))  

        # TODO: "file", "image", 
        # TODO: HTML5 -- input(list) and datalist

        return data
```

# requestsでPOSTすると最初のパラメータしかわたっていない

[requests](http://docs.python-requests.org/en/latest/)はMultiDictに対応しているということなのだが、手持ちの環境で動かない。。。

しょうがないので、とりあえずdictに変換して対応:

```py
>>> dict(d.lists())
{'a': [1, 2, 3, '4']}
```

```py
    def post(self, uri, data):

        if isinstance(data, MultiDict):
            data = dict(data.lists())

        self.res = self.req.post(
            uri, data=data,
            verify=False, allow_redirects=False)
        self.last_uri = uri
```
