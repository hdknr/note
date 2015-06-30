## XMLの整形

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