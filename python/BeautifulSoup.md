## prettify

~~~py
	>>> from bs4 import BeautifulSoup as Soup
	>>> browser.get('http://twitter.com')
	>>> print Soup(browser.page_source).select('form')[1].prettify()

	<form action="/sessions/change_locale" class="language" method="POST">
	 <input name="lang" type="hidden"/>
	 <input name="redirect" type="hidden"/>
	 <input name="authenticity_token" type="hidden" value="4ae7df1ac2b69b61e5d260c1e4b7ccd29112fcdf"/>
	</form>
~~~	