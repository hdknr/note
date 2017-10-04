## xmllint: XMLの整形

- libxml2-utils(Debian)

~~~
$ dpkg -L libxml2-utils | grep xmllint
/usr/share/man/man1/xmllint.1.gz
/usr/bin/xmllint
~~~

- xmllint

```
$ xmllint --format yourxmlfile.xml
```


## xmlstarlet


~~~bash
$ sudo apt-get install xmlstarlet
~~~

### sitemap.xml からURLを一覧する


~~~bash
$ xmlstarlet sel -t -m "//*[local-name()='loc']/text()" -v . -n  sitemap.xml
~~~
