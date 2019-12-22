# Rust([#98](https://github.com/hdknr/scriptogr.am/issues/98))

- https://www.rust-lang.org/learn
- https://www.rust-lang.org/learn/get-started

## インストール

~~~bash
$ curl https://sh.rustup.rs -sSf | sh
..
~~~

## 設定

~~~bash
$ source $HOME/.cargo/env

$ which cargo
/Users/hide/.cargo/bin/cargo

$ rustup --version
rustup 1.14.0 (1e51b07cc 2018-10-04)
~~~

## ツールチェーン

~~~bash
$ rustup install stable
.
~~~

## 更新

~~~bash
$ rustup update

info: syncing channel updates for 'stable-x86_64-apple-darwin'
361.8 KiB / 361.8 KiB (100 %)  31.5 KiB/s ETA:   0 s                
info: latest update on 2019-08-15, rust version 1.37.0 (eae3437df 2019-08-13)
info: downloading component 'rustc'
 78.7 MiB /  78.7 MiB (100 %)   1.2 MiB/s ETA:   0 s                 
info: downloading component 'rust-std'
 56.3 MiB /  56.3 MiB (100 %)   1.6 MiB/s ETA:   0 s                
info: downloading component 'cargo'
  3.6 MiB /   3.6 MiB (100 %)   1.8 MiB/s ETA:   0 s                
info: downloading component 'rust-docs'
 11.3 MiB /  11.3 MiB (100 %)   1.3 MiB/s ETA:   0 s                
info: removing component 'rustc'
info: removing component 'rust-std'
info: removing component 'cargo'
info: removing component 'rust-docs'
info: installing component 'rustc'
info: installing component 'rust-std'
info: installing component 'cargo'
info: installing component 'rust-docs'
info: checking for self-updates
info: downloading self-update

  stable-x86_64-apple-darwin updated - rustc 1.37.0 (eae3437df 2019-08-13)

$ rustup --version
rustup 1.19.0 (2af131cf9 2019-09-08)
~~~
