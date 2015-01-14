Sqlite.Net: 結果  のメッセージ:	System.DllNotFoundException : DLL ”sqlite3”を読み込めません:指定されたモジュールが見つかりません。 (HRESULT からの例外:0x8007007E)

# 現象

- Xamarin Mac でうごいているプロジェクト
- Visual Studio Community 2013 で表題のメッセージでエラー
- PCLなので

```
var sqlite = new SQLite.Net.Platform.Generic.SQLitePlatformGeneric ();
```

- 要するに sqlite3.dll のロードに失敗している

# 対応

- https://www.sqlite.org/download.html
- "Precompiled Binaries for Windows"
- sqlite-dll-win32-x86-3080702.zip　(とか) をダウンロード
- 解凍
- sqlite3.dll をコピー

	32bit版OSの場合は「C:¥Windows¥System32」
	
	64bit版OSの場合は「C:¥Windows¥SysWOW64」
