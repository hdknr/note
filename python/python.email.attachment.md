## ファイル名のUnicode正規化問題


- [MacとLinuxで互換性のない日本語ファイル](http://qiita.com/suin/items/c6ccc1a23b334113579b)
- [Mac OS X の NFD 問題での対策諸々](http://qiita.com/knaka/items/48e1799b56d520af6a09)


- NFD(OSX) vs. NFC(Windows/Linux) で互換性がない
- Mac側でツールによっては自動変換


## Universal-newline mode


- 添付ファイルを StringIO.StringIOで受けた時に、改行が問題になるかも
- `io.StringIO(data.decode(encoding), newline=None)` で受ける


### CSV は Unicodeだめ (2.7)

- io.StringIOは Unicodeなので、 UTF-8(とか)に変換する

~~~
if isinstance(stream, io.StringIO):
	stream = StringIO.StrinIO(stream.read().encode(encoding))
~~~


