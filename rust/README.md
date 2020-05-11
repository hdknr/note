# Rust([#98](https://github.com/hdknr/scriptogr.am/issues/98))

- https://www.rust-lang.org/learn
- https://www.rust-lang.org/learn/get-started

## インストール

- [Install Rust](https://www.rust-lang.org/tools/install
)
~~~bash
$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
~~~

~~~bash
info: downloading installer

Welcome to Rust!

This will download and install the official compiler for the Rust
programming language, and its package manager, Cargo.

It will add the cargo, rustc, rustup and other commands to
Cargo's bin directory, located at:

  /Users/hdknr/.cargo/bin

This can be modified with the CARGO_HOME environment variable.

Rustup metadata and toolchains will be installed into the Rustup
home directory, located at:

  /Users/hdknr/.rustup

This can be modified with the RUSTUP_HOME environment variable.

This path will then be added to your PATH environment variable by
modifying the profile files located at:

  /Users/hdknr/.profile
/Users/hdknr/.zprofile
/Users/hdknr/.bash_profile

You can uninstall at any time with rustup self uninstall and
these changes will be reverted.

Current installation options:


   default host triple: x86_64-apple-darwin
     default toolchain: stable
               profile: default
  modify PATH variable: yes

1) Proceed with installation (default)
2) Customize installation
3) Cancel installation
>1        

info: profile set to 'default'
info: default host triple is x86_64-apple-darwin
info: updating existing rustup installation


Rust is installed now. Great!

To get started you need Cargo's bin directory ($HOME/.cargo/bin) in your PATH
environment variable. Next time you log in this will be done
automatically.

To configure your current shell run source $HOME/.cargo/env
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


## rustup更新

~~~bash
$ rustup self update
~~~

## nightly

~~~bash
% rustup install nightly
info: syncing channel updates for 'nightly-x86_64-apple-darwin'
info: latest update on 2020-05-10, rust version 1.45.0-nightly (bad3bf622 2020-05-09)
info: downloading component 'cargo'
info: downloading component 'clippy'
info: downloading component 'rust-docs'
info: downloading component 'rust-std'
info: downloading component 'rustc'
info: downloading component 'rustfmt'
info: installing component 'cargo'
info: installing component 'clippy'
info: installing component 'rust-docs'
 12.2 MiB /  12.2 MiB (100 %)   4.3 MiB/s in  2s ETA:  0s
info: installing component 'rust-std'
info: installing component 'rustc'
 58.0 MiB /  58.0 MiB (100 %)  16.3 MiB/s in  3s ETA:  0s
info: installing component 'rustfmt'

  nightly-x86_64-apple-darwin installed - rustc 1.45.0-nightly (bad3bf622 2020-05-09)

info: checking for self-updates
~~~
