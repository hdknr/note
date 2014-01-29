Date: 2013-07-04 18:00
Title: BeatifulSoup: soupselectで簡単に目的のtagを削除
Type: post  
Excerpt:   


[soupselect](https://github.com/simonw/soupselect)で、jQuery風のセレクタをSoupにかけられるので超便利です。


    import sys
    import shutil
    from BeautifulSoup import BeautifulSoup as Soup,Tag
    from soupselect import select
    
    if __name__ == '__main__' and len(sys.argv) > 1:
        shutil.copyfile( sys.argv[1], ".org."+sys.argv[1]) 
        soup = Soup( open(sys.argv[1]).read() )
        map( lambda tag :tag.extract(),select(soup, "div.content script" ) )
        with open( sys.argv[1],"w") as out:
            out.write(soup.prettify("utf-8") )

これで、

    <div class="content">
        . . . 
        <script>
           . . .
           
の script を抜いて書き込みます。                   
        