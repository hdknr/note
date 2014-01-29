Date: 2013-07-09  11:00
Title:  Python vs. C# : ファイル周り
Type: post  
Excerpt:   

# モジュールのパス #

Python:

    import os

    dir = os.path.dirname( os.path.abspath(__file__))
    
C#:

    // this はアセンブリに含まれるクラス
    var asm = System.Reflection.Assembly.GetAssembly(this.GetType());    
    var dir = System.IO.Path.GetDirectoryName( asm.Location );
    

# ディレクトリ名とファイル名の連結 #

Python:

    import os
    
    path = os.path.join( dir + "settings.py" )
    
    
C#:

    var path = System.IO.Path.Combine(dir, "web.config");
    
## URIの連結 ##

Python:

    >>> import urlparse
    >>> urlparse.urljoin("http://hoge.com", "edit")
    'http://hoge.com/edit'

C#:

    var uri = new Uri( new Uri("http://hoge.com"), "edit") ;   

どちらも第１引数が URIの「ベース」なので、"/"で終わっていない場合は直前の"/"以降が取除かれる。追加パスが"/"で始まっているとパスで置き換え:

    >>> rest = "https://api.com/v1/path"

    >>> urlparse.urljoin(rest,"xxxx")
    'https://api.com/v1/xxxx'

    >>> urlparse.urljoin(rest,"/xxxx")
    'https://api.com/xxxx'
    
    >>> urlparse.urljoin(rest+"/","xxxx")
    'https://api.com/v1/path/xxxx'

# ファイルとディレクトリの存在確認 #

Python:

    import os
    assert os.path.exists(dname)
    assert os.path.isdir(dname)
    assert os.path.isfile(__file__)

C#:

    Assert.IsTrue(System.IO.Directory.Exists(dir));
    Assert.IsTrue(System.IO.File.Exists(path));

# ディレクトリの再帰的作成 #

Python:

    import os
    os.makedirs("a/b/c/d")

C#:

    System.IO.CreateDirectory("a/b/c/d")

    
# トリミング #

Python:

    >>> "/hoge/hoge/".rstrip('/')
    '/hoge/hoge'
    >>> "/hoge/hoge/".lstrip('/')
    'hoge/hoge/'
    
C#:

    Console.WriteLine("/hoge/hoge/".TrimEnd('/') );    Console.WriteLine("/hoge/hoge/".TrimStart('/'));

# ファイルの一覧 #

C#:
    
    foreach(var file in System.IO.Directory.GetFile( path )) 
    {
        Console.Writeline(file);
    }

    System.IO.Directory.GetFiles(path,"*_?.Rp.json"))
    {
        Console.WriteLine(file);
    }

Python:

    >>> import os
    >>> len( os.listdir('.'))
    133

    >>> import glob
    >>> len( glob.glob('./*.md'))
    131

    >>> len( glob.glob('./*python*.md'))
    7    

# パスのファイル名、ディレクトリ名など #

C#:

    Console.WriteLine(System.IO.Path.GetDirectoryName(file));
    Console.WriteLine(System.IO.Path.GetFileName(file));
    Console.WriteLine(System.IO.Path.GetFileNameWithoutExtension(file));
    Console.WriteLine(System.IO.Path.GetExtension(file));
    

Python:

    >>> os.path.dirname(path)
    >>> os.path.basename(path)
    >>> os.path.split(path)
    >>> os.path.splitext(path)[0]
    >>> os.path.splitext(path)[1]
