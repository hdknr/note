Date: 2014-02-04  
Title:  Python: parser で構文解析
Type: post  
Excerpt:   


[parser](http://docs.python.org/2/library/parser.html) で Django manage.py を処理してみる:


    >>> import parser
    >>> eval( parser.suite( open('manage.py').read() ).compile() )
    
    Usage:  subcommand [options] [args]
    
    Options:
      -v VERBOSITY, --verbosity=VERBOSITY
                            Verbosity level; 0=minimal output, 1=normal output,
                            2=verbose output, 3=very verbose output
      --settings=SETTINGS   The Python path to a settings module, e.g.
                            "myproject.settings.main". If this isn't provided, the
                            DJANGO_SETTINGS_MODULE environment variable will be
                            used.
      --pythonpath=PYTHONPATH
                            A directory to add to the Python path, e.g.
                            "/home/djangoprojects/myproject".
      --traceback           Print traceback on exception
      --version             show program's version number and exit
      -h, --help            show this help message and exit
    
    Type ' help <subcommand>' for help on a specific subcommand.
    

tolist() で解析コードをリスト化:
    
    >>> code_list = parser.suite( open('manage.py').read()).tolist()
    >>> type(code_list)
    <type 'list'>
    >>> code_list
    [257, [267, [268, [269, [281, 
    :
    :

このリストを戻して実行すると おなじく python manage.py を実行 :

    >>> eval( parser.sequence2st( code_list).compile() )
    
    
なので、この code_listに別のパースドコードを挿入してからcompile() すればコードの注入可能？
    
(いつかつづく)
