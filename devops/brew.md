# Homebrew

- [brew.sh](http://brew.sh/)

## 更新: `upgrade`

~~~bash
$ env HOMEBREW_INSTALL_CLEANUP=1 brew upgrade
.
~~~

## tap / untap

- [これは便利！Homebrewに追加されたtapコマンドはリポジトリを追加して簡単にフォーミュラを増やせる - Macとかの雑記帳](http://tukaikta.blog135.fc2.com/blog-entry-204.html)

### `remote: Repository not found.`  : `untap`

~~~bash
$ brew update

remote: Repository not found.
fatal: repository 'https://github.com/Homebrew/homebrew-boneyard/' not found
Error: Fetching /usr/local/Homebrew/Library/Taps/homebrew/homebrew-boneyard failed!
~~~

~~~bash
$ brew untap Homebrew/homebrew-boneyard

Untapping homebrew/boneyard...
Untapped (33 files, 278.2KB).
~~~

### `Error: No available formula for php55`: `tap --repair`

~~~bash
$ brew info php55

Error: No available formula for php55
~~~

~~~bash
$ brew tap --repair
..
~~~

## その他

- ["The bottle needs the Xcode CLT to be installed" logged when Xcode CLT are installed · Issue #2502 · Homebrew/homebrew-core](https://github.com/Homebrew/homebrew-core/issues/2502)
- [homebrewの更新はbrew upgrade --cleanupだけでよくなっている - @znz blog](https://blog.n-z.jp/blog/2017-04-27-homebrew-upgrade-cleanup.html)
