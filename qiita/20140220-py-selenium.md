Python: selenium でFirefoxを操作する

pipで selenium をインストール:

    (tact)PeekoOne:~ hide$ pip install selenium
    Downloading/unpacking selenium
      Downloading selenium-2.40.0.tar.gz (2.5Mb): 2.5Mb downloaded
      Running setup.py egg_info for package selenium
        
    Installing collected packages: selenium
      Running setup.py install for selenium
        
    Successfully installed selenium
    Cleaning up...
    
Firefoxのウェブドライバを作成:  

    >>> from selenium import webdriver
    >>> browser = webdriver.Firefox()
    
この時点で、 Firefoxが起動されます
    
Google に移動

    >>> browser.get('http://www.google.com')
    >>> print browser.title
    Google
    
検索の inputタグ をidで探す

    >>> browser.find_element_by_id('lst-ib')
    <selenium.webdriver.remote.webelement.WebElement object at 0x1026661d0>
    >>> q=_

    
これにキーワード入力。

    >>> q.send_keys('selenium')

この時点でFirefoxでJavascriptが動いてキーワード候補がでている。
    
リターンを入力すると、javascriptが起動してフォームがSubmitされます。

    >>> q.send_keys('\n')
    
    >>> print browser.title
    selenium - Google 検索
    
    
CSSセレクタで選択
    
    >>> browser.find_elements_by_css_selector('input[name=q]')
    [<selenium.webdriver.remote.webelement.WebElement object at 0x102a8c890>]
    >>> q=_
    >>> q[0].send_keys('Django\n')
    >>> print browser.title
    Django - Google 検索
    

BeautifulSoupでHTMLを印刷

	>>> from bs4 import BeautifulSoup as Soup
	>>> browser.get('http://twitter.com')
	>>> print Soup(browser.page_source).select('form')[1].prettify()

	<form action="/sessions/change_locale" class="language" method="POST">
	 <input name="lang" type="hidden"/>
	 <input name="redirect" type="hidden"/>
	 <input name="authenticity_token" type="hidden" value="4ae7df1ac2b69b61e5d260c1e4b7ccd29112fcdf"/>
	</form>
