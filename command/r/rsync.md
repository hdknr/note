# rsync

- [rsync オプション](http://qiita.com/bezeklik/items/22e791df71 87958d76c1)

| オプション | 別名                   | 意味                                                                             |
| ---------- | ---------------------- | -------------------------------------------------------------------------------- |
| `-a`       | `--archive`            | `-rlptgoD` と同じ                                                                |
|            |                        |                                                                                  |
| `-H`       | `--hard-links`         | ハードリンクをそのまま反映                                                       |
| `-h`       | `--human-readable`     | ファイルサイズの`bytes`を`K`や`M`で出力                                          |
| `-v`       | `--verbose`            | コピーしたファイル名やバイト数などの転送情報を出力                               |
| `-z`       | `--compress`           | データ転送時に圧縮                                                               |
|            | `--compress-level=NUM` | `NUM`がゼロでない場合 `--compress` オプションが暗黙的に指定される                |
|            | `--skip-compress=LIST` |                                                                                  |
| `-c`       | `--checksum`           | タイムスタンプとファイルサイズではなくチェックサムで差分を確認                   |
| `-u`       | `--update`             | 転送先に既にファイルが存在し、転送先のタイムスタンプの方が新しい場合は転送しない |
| `-n`       | `--dry-run`            | コピーや転送を実際には行わず転送内容のみ出力                                     |
|            | `--delete`             | 転送元に存在しないファイルは削除                                                 |
|            | `--exclude=PATTERN`    | 同期から除外                                                                     |

アーカイブ `-a` の個別設定:

| オプション | 別名          | 意味                                                       |
| ---------- | ------------- | ---------------------------------------------------------- |
| `-r`       | `--recursive` | 指定ディレクトリ配下をすべて対象とする                     |
| `-l`       | `--links`     | シンボリックリンクをそのままシンボリックリンクとしてコピー |
| `-p`       | `--perms`     | パーミッションをそのままコピー                             |
| `-t`       | `--times`     | タイムスタンプをそのままコピー                             |
| `-g`       | `--group`     | グループをそのままコピー                                   |
| `-o`       | `--owner`     | ファイル所有者をそのままコピー (root のみ有効)             |
| `-D`       |               | `--devices --specials` と同じ                              |
|            | `--devices`   | ブロックデバイスをコピー (root のみ有効)                   |
|            | `--specials`  | 名前付きパイプや FIFO などの特殊ファイルをコピー           |

```bash
$ time rsync -av --delete --exclude-from ${PATTERNFILE} -e "ssh -i /root/.ssh/id_rsync" ${SOURCEDIR} ${DESTDIR} 2>&1 | tee -a ${LOGFILE}
.
```

## 記事

- [QIITA](https://qiita.com/search?q=rsync)
