
- [多言語対応：英語と日本語を自動切り替え(後編)](https://cakephp.euonymus.info/%E5%A4%9A%E8%A8%80%E8%AA%9E%E5%AF%BE%E5%BF%9C%EF%BC%9A%E8%8B%B1%E8%AA%9E%E3%81%A8%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%92%E8%87%AA%E5%8B%95%E5%88%87%E3%82%8A%E6%9B%BF%E3%81%88%E5%BE%8C%E7%B7%A8/)


## i18n

~~~
../cake/console/cake i18n
~~~

~~~
Welcome to CakePHP v1.3.20 Console
---------------------------------------------------------------
App : app
Path: /home/cakenr/Rev201503/source/app
---------------------------------------------------------------
I18n Shell
---------------------------------------------------------------
[E]xtract POT file from sources
[I]nitialize i18n database table
[H]elp
[Q]uit
What would you like to do? (E/I/H/Q) 
> E     
~~~


~~~
What is the full path you would like to extract?
Example: /home/cakenr/Rev201503/source/myapp
[Q]uit [D]one  
[/home/cakenr/Rev201503/source/app] > D    
~~~


~~~
What is the full path you would like to output?
Example: /locale
[Q]uit  
[/locale] > locale
~~~

~~~
Would you like to merge all domains strings into the default.pot file? (y/n) 
[n] > y
~~~

~~~
Extracting...
---------------------------------------------------------------
Paths:
Output Directory: locale/
---------------------------------------------------------------

Done.
---------------------------------------------------------------
I18n Shell
---------------------------------------------------------------
[E]xtract POT file from sources
[I]nitialize i18n database table
[H]elp
[Q]uit
What would you like to do? (E/I/H/Q) 
> Q
~~~

## mo ファイル
- [CakePHPの国際化で使用するpoファイルを更新する](http://blog.zista.jp/docs/id/0000000117)

~~~
AppPath="/path/to/cake/app"
/path/to/cake/console/cake i18n extract  -paths $AppPath  -output $AppPath/locale/ -merge yes
msgmerge -U  $AppPath/locale/jpn/LC_MESSAGES/default.po $AppPath/locale/default.pot
echo "msgmerge Done."

~~~

~~~
msgfmt default.po  -o default.mo 
~~~

### tmp の動きがよくわからん

- クリアし直すと動く(> <)

~~~
$ rm -rf tmp/
$ svn update
$ tree tmp
tmp
├── cache
│   ├── models
│   │   └── empty
│   ├── persistent
│   │   └── empty
│   └── views
│       └── empty
├── dbbackup
│   └── empty
├── logs
│   └── empty
├── sessions
│   └── empty
└── tests
    └── empty

8 directories, 7 files

$ sudo chmod -R 777 tmp/
~~~