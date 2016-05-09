## トークン化

- [Efficiently split a string using multiple separators and retaining each separator?](https://stackoverflow.com/questions/13186067/efficiently-split-a-string-using-multiple-separators-and-retaining-each-separato)


## アサーション

1.  `(?=...)` :先読みアサーション(lookahead assertion)
2.  `(?!...)` : 否定先読みアサーション(negative lookahead assertion)
3.  `(?<=...)` : 肯定後読みアサーション(positive lookbehind assertion)
4.  `(?<!...)` : 否定後読みアサーション(negative lookbehind assertion)

Python は 先読み(1とに)しか実装していない


~~~py
re.search(r'(\d)(?=(\d{3})+(?!\d))', str(123456789)).groups()
('3', '789')
~~
