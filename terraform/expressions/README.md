## 式(Expression )


- [for](https://www.terraform.io/docs/language/expressions/for.html)
- [splat](https://www.terraform.io/docs/language/expressions/splat.html)  (`list[*]`)


## [エスケープシーケンス](https://www.terraform.io/language/expressions/strings#escape-sequences)

バックスラッシュ:

- `\n` -> LF 改行
- `\r` -> CR
- `\t` -> タブ
- `\"` -> リテラル文字
- `\\` -> バックスラッシュ
- `\uNNNN` -> Unicode文字(4文字16進):  基本多言語面(BMP: basic multilingual plane)
- `\UNNNNNNNN -> Unicode文字(８文字16進)、追加多言語面(SMP: supplementary planes)

バックスラッシュ以外:

- `$${` -> `${`
- `%%{` -> `%{`

