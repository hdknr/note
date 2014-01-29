Date: 2014-01-10  11:00
Title: Trac:Markdown マクロを使えるようにする。
Type: post  
Excerpt:   


[MarkdownMacro](http://trac-hacks.org/wiki/MarkdownMacro) のZipファイルをダウンロード。

解凍してビルド:

    (myve)[hdknr@amz ~]$ unzip markdownmacro-13563.zip 
    Archive:  markdownmacro-13563.zip
    warning:  stripped absolute path spec from /
    mapname:  conversion of  failed
       creating: markdownmacro/trunk/
      inflating: markdownmacro/trunk/COPYING  
       creating: markdownmacro/trunk/Markdown/
      inflating: markdownmacro/trunk/Markdown/__init__.py  
      inflating: markdownmacro/trunk/Markdown/macro.py  
      inflating: markdownmacro/trunk/README  
      inflating: markdownmacro/trunk/setup.cfg  
      inflating: markdownmacro/trunk/setup.py  

    
    (myve)[hdknr@amz ~]$ cd markdownmacro/trunk/
    
    (myve)[hdknr@amz trunk]$ python setup.py bdist_egg
    running bdist_egg
    running egg_info
    creating TracMarkdownMacro.egg-info
    writing requirements to TracMarkdownMacro.egg-info/requires.txt
    writing TracMarkdownMacro.egg-info/PKG-INFO
    writing top-level names to TracMarkdownMacro.egg-info/top_level.txt
    writing dependency_links to TracMarkdownMacro.egg-info/dependency_links.txt
    writing entry points to TracMarkdownMacro.egg-info/entry_points.txt
    writing manifest file 'TracMarkdownMacro.egg-info/SOURCES.txt'
    reading manifest file 'TracMarkdownMacro.egg-info/SOURCES.txt'
    writing manifest file 'TracMarkdownMacro.egg-info/SOURCES.txt'
    installing library code to build/bdist.linux-x86_64/egg
    running install_lib
    running build_py
    creating build
    creating build/lib
    creating build/lib/Markdown
    copying Markdown/__init__.py -> build/lib/Markdown
    copying Markdown/macro.py -> build/lib/Markdown
    creating build/bdist.linux-x86_64
    creating build/bdist.linux-x86_64/egg
    creating build/bdist.linux-x86_64/egg/Markdown
    copying build/lib/Markdown/__init__.py -> build/bdist.linux-x86_64/egg/Markdown
    copying build/lib/Markdown/macro.py -> build/bdist.linux-x86_64/egg/Markdown
    byte-compiling build/bdist.linux-x86_64/egg/Markdown/__init__.py to __init__.pyc
    byte-compiling build/bdist.linux-x86_64/egg/Markdown/macro.py to macro.pyc
    creating build/bdist.linux-x86_64/egg/EGG-INFO
    copying TracMarkdownMacro.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
    copying TracMarkdownMacro.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
    copying TracMarkdownMacro.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
    copying TracMarkdownMacro.egg-info/entry_points.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
    copying TracMarkdownMacro.egg-info/requires.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
    copying TracMarkdownMacro.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
    zip_safe flag not set; analyzing archive contents...
    creating dist
    creating 'dist/TracMarkdownMacro-0.11.4-py2.6.egg' and adding 'build/bdist.linux-x86_64/egg' to it
    removing 'build/bdist.linux-x86_64/egg' (and everything under it)
    
確認:
    
    (myve)[hdknr@amz trunk]$ find . -name "*.egg" -print
    ./dist/TracMarkdownMacro-0.11.4-py2.6.egg

pluginsにコピー:
    
    (myve)[hdknr@amz trunk]$ cp dist/TracMarkdownMacro-0.11.4-py2.6.egg ~/tracs/prj/system/plugins
    
trac.ini に追加:

    (myve)[hdknr@amz trunk]$ vi ~/tracs/prj/system/conf/trac.ini

    [components]

    Markdown.* = enabled


apache reload :

    (myve)[hdknr@amz trunk]$ sudo /etc/init.d/httpd reload
    httpd を再読み込み中: 
