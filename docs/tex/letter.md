# ハガキ

## サービス

- [【2019年亥年版】ネットで年賀状™ スマホで年賀状™2019 - デザイン作成から印刷、配送までが簡単！](https://net-nengajo.jp/)

## その他

- [年賀状（年賀はがき）のサイズ・ピクセル - 用紙サイズ一覧.com](http://www.size-info.com/postcard/nenga.html)

## HTML

- [html + css で年賀状の宛名書き（Ubuntuで年賀状宛名書き） - adbird（広告鳥） 備忘録](http://adbird.hatenablog.com/entry/2016/12/14/123953)
- [HTML+CSSで宛名印刷 - うならぼ](http://unarist.hatenablog.com/entry/2017/01/01/190945)
- [そろそろ真面目に、HTMLで帳票を描く話をしようか - Qiita](https://qiita.com/cognitom/items/d39d5f19054c8c8fd592)

## TeX

- [packages - Installing a class - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/10498/installing-a-class)
- [macでのlatexmkを使ったTeX環境構築 - しゃちの備忘録](http://teru0rc4.hatenablog.com/entry/2017/01/28/213102)
- [TeXで宛名印刷 - Folioscope](http://folioscope.hatenablog.jp/entry/2014/01/13/221455)
- [LaTeXコマンド - 文書クラス（種類）とオプション - documentclass](https://medemanabu.net/latex/documentclass/)
- [installing - How to register my own packages or classes in a separate drive to TeX Live installation? - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/20160/how-to-register-my-own-packages-or-classes-in-a-separate-drive-to-tex-live-insta)
- [LaTeX入門/各種パッケージの利用 - TeX Wiki](https://texwiki.texjp.org/?LaTeX%E5%85%A5%E9%96%80/%E5%90%84%E7%A8%AE%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%81%AE%E5%88%A9%E7%94%A8)

### 1. MacTeX

- [インストール](latex.md)

### 2. jletteraddress

- [ueokande/jletteraddress: A document class of LaTeX for address side of the Japanese letter.](https://github.com/ueokande/jletteraddress)
- `jletteraddres.cls` を TeXファイルと同じフォルダーに置く

### 3. TeXファイル生成プログラム

- jinja2 でテンプレート化
- Excelファイルに住所録

~~~py
import click
import pandas as pd
from jinja2 import Template, Environment, FileSystemLoader


@click.group()
def main():
    pass


def open_excel(path):
    return pd.ExcelFile(path, encoding='utf8')


def get_sheet(excel, index=0):
    return excel.parse(excel.sheet_names[0])


def get_template():
    # http://eosrei.net/articles/2015/11/latex-templates-python-and-jinja2-generate-pdfs

    env = Environment(
    	block_start_string='\BLOCK{',
    	block_end_string='}',
    	variable_start_string='\VAR{',
    	variable_end_string='}',
    	comment_start_string='\#{',
    	comment_end_string='}',
    	line_statement_prefix='%%',
    	line_comment_prefix='%#',
	    trim_blocks=True,
	    autoescape=False,
        loader=FileSystemLoader('.'),
    )
    return env.get_template('template.j2')


@main.command()
@click.argument('path')
def make_tex(path):
    sheet = get_sheet(open_excel(path))
    template = get_template()
    for index, row in sheet.iterrows():
        data = row.to_dict()
        tex = template.render(data)
        with open(f"{index}.tex", 'w') as out:
            out.write(tex)

if __name__ == '__main__':
    main()
~~~

### 4. TeXテンプレート

- `Environment` で設定したように `\VAR{変数名}` で Jinja2 の変数を展開する

~~~j2
\documentclass[]{jletteraddress}
\usepackage{otf}

% Sender's informations
\sendername{\VAR{sender_name}}
\senderaddressa{\VAR{sender_address_a}}
\senderaddressb{\VAR{sender_address_b}}
\senderpostcode{\VAR{sender_postal_code}}

\begin{document}

\addaddress
{\VAR{name}}
{\VAR{suffix}}
{\VAR{postal_code}}
{\VAR{address}}
{\VAR{address2}}

\end{document}
~~~

### 5. Excel住所録

Excelのヘッダー行の:

- `sender_name`
- `sender_address_a`
- `sender_address_b`
- `sender_postal_code`
- `name`
- `suffix`
- `postal_code`
- `address`
- `address2`

２行目以降にデータを登録する

### 6. texファイルの生成

~~~bash
python letters.py  make_tex ~/Download/address.xslx
~~~

### 7. PDF化

0.texから 121.texまでつくられたとする：

~~~bash
for i in `seq 0 121`; do
    platex $i && dvipdfmx $i
done
~~~