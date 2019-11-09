# Ubuntu

## スワップ

- [Amazon EC2(Linux)のswap領域ベストプラクティス ｜ Developers.IO](https://dev.classmethod.jp/cloud/ec2linux-swap-bestpractice/)
- [How to Enable Swapfile on Ubuntu AWS Instances - Metova](https://metova.com/how-to-enable-swapfile-on-ubuntu-aws-instances/)
- [インスタンスストアスワップボリューム - Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/instance-store-swap-volumes.html)
- [linux - Why don't EC2 ubuntu images have swap? - Server Fault](https://serverfault.com/questions/218750/why-dont-ec2-ubuntu-images-have-swap)


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
