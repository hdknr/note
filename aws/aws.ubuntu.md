## Ubuntu AMI 一覧

- 東京　64-bit

~~~py
import requests
from bs4 import BeautifulSoup as Soup

r = requests.get('http://cloud-images.ubuntu.com/precise/current/')
html = Soup(r.text, "html.parser")
for tr in html.select('tr'):
    if tr.select('td p')[1].text.replace(' ', '') != '64-bit':
        continue
    if not tr.select('td p')[0].text.replace(' ', '').startswith('ap-northeast'):
        continue

    for p in  tr.select('td p'):
        print p.text.replace(' ', ''),
    print
~~~    
