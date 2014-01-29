Date: 2013-09-17  17:00
Title:   C#, Python, PHP : コレクション周り
Type: post  
Excerpt:   


# そもそも #
C#はコレクションクラスがいろいろあります。。。。 orz

# キーがあるか？ #

Python: in キーワード:

    >>> a={'a':1,}
    >>> 'a' in a
    True
    >>> 'b' in a
    False
    
PHP: array_key_exists関数:

    php > $a=array('a' => 1);

    php > print (true==array_key_exists('a',$a));
    1
    php > print (false==array_key_exists('b',$a));
    1
   
C#: ContansKeyメソッド（Generics):

    var a = new Dictionary<string, object> { { "a", 1 } };
    Console.WriteLine(a.ContainsKey("a"));
    Console.WriteLine(a.ContainsKey("b"));

    True
    False
    
    
        