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

[SoF](https://stackoverflow.com/posts/30248924/revisions):
~~~
xmlstarlet sel -t -m "/ROOT/ITEM/PHOTO" -v . -n xml_2015-05-13-20\:39.xml
           |   |  |                     |    |
           |   |  |                     |    -n ... add new-line after printed element
           |   |  |                     -v .  print the value of the matched node
           |   |  -m match this Xpath
           |   -t  (select) using a template (the -m part)
           sel(ect)
~~~           
