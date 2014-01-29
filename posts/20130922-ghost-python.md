Date: 2013-09-22  
Title: Ghost.py : PyQtWebkit ラッパー
Type: post  
Excerpt:   


PySideインストールに必要:

    (tact)hdknr@wzy:~/ve/tact/src/works/web$ sudo aptitude install cmake
    以下の新規パッケージがインストールされます:
      cmake cmake-data{a} emacsen-common{a} libarchive12{a} libxmlrpc-core-c3{a} 
    更新: 0 個、新規インストール: 5 個、削除: 0 個、保留: 0 個。
    6,600 k バイトのアーカイブを取得する必要があります。展開後に 16.1 M バイトのディスク領域が新たに消費されます。
    先に進みますか? [Y/n/?] y
    :
    :

Ghost.pyにPySide(or PyQt)が必要:

    (tact)hdknr@wzy:~$ pip install PySide

[http://bit.ly/1gMfk96](http://bit.ly/1gMfk96)

Ghost.pyをインストール:

    (tact)hdknr@wzy:~$ pip install Ghost.py
    Downloading/unpacking Ghost.py
      Downloading Ghost.py-0.1b2.tar.gz
      Running setup.py egg_info for package Ghost.py
        
        warning: no files found matching '*' under directory 'docs'
        warning: no previously-included files matching '*.pyc' found under directory 'docs'
        warning: no previously-included files matching '*.pyo' found under directory 'docs'
        no previously-included directories found matching 'docs/_build'
        no previously-included directories found matching 'docs/_themes/.git'
    Installing collected packages: Ghost.py
      Running setup.py install for Ghost.py
        
        warning: no files found matching '*' under directory 'docs'
        warning: no previously-included files matching '*.pyc' found under directory 'docs'
        warning: no previously-included files matching '*.pyo' found under directory 'docs'
        no previously-included directories found matching 'docs/_build'
        no previously-included directories found matching 'docs/_themes/.git'
    Successfully installed Ghost.py
    Cleaning up...

BeautifulSoupのセレクターを入れて置く:

    (tact)hdknr@wzy:~/ve/tact/src/works/web$ git clone https://github.com/simonw/soupselect.git
    Cloning into 'soupselect'...
    remote: Counting objects: 32, done.
    remote: Compressing objects: 100% (22/22), done.
    remote: Total 32 (delta 11), reused 27 (delta 9)
    Unpacking objects: 100% (32/32), done.


HTML(Djangoのhelloアプリのテンプレート )。クリックしたら時間を変える:

    tact)hdknr@wzy:~/ve/tact/src/works/web$ more hello/templates/default.html 
    <!DOCTYPE html>
    <html lang="ja">
    <head>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js" ></script>
    </head>
    <body>
     <section id="main" >
       <h1 class="title">Hello</h1>
       <div class="body">
         <button id="time" >now?</button>
       </div>
     </section> 
    </body>
    <script>
    $(document).ready(function() {
      $("button#time").click(function(){
        $(this).text( new Date( $.now() ) . toLocaleString() );
      });
    });
    </script>
    </html>

Webサーバー起動:

    (tact)hdknr@wzy:~/ve/tact/src/works/web$ python manage.py runserver 0.0.0.0:9000
    Validating models...
    
    0 errors found
    September 21, 2013 - 13:44:16
    Django version 1.5.1, using settings 'app.settings'
    Development server is running at http://0.0.0.0:9000/


Ghost起動(２回目なのでQtWebKit起動エラー?):

    >>> from ghost import Ghost
    >>> g = Ghost()
    _XSERVTransSocketINETCreateListener: ...SocketCreateListener() failed
    _XSERVTransMakeAllCOTSServerListeners: server already running
    
    Fatal server error:
    Cannot establish any listening sockets - Make sure an X server isn't already running


ページアクセス:

    >>> page, extra_resources =g.open("http://localhost:9000")
    >>> type(page)
    <class 'ghost.ghost.HttpResource'>
    >>> page.http_status
    200

最初の時間:

    >>> from BeautifulSoup import BeautifulSoup as Soup
    >>> from soupselect.soupselect import select
    
    >>> select(Soup(page.content),"#time")[0].text
    u'now?'


button#timeｗクリック:

    >>> with Ghost.confirm():
    ...     g.click("#time")
    ... 
    
    >>> print select(Soup(g.content),"#time")[0].text
    2013年09月21日 14時18分15秒

もう一度:

    >>> with Ghost.confirm():
    ...     g.click("#time")
    ...     print select(Soup(g.content),"#time")[0].text
    ... 
    (True, [])
    2013年09月21日 14時19分36秒

PyQtWebkitのロケールの設定がおかしいので時間ずれてるのかな？    
