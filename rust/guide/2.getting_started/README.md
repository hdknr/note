# 2. [Getting Started](https://doc.rust-lang.org/1.2.0/book/getting-started.html)

## Installing Rust

### rustup

- https://rustup.rs/
- [rust-lang-nursery/rustup.rs: The Rust toolchain installer](https://github.com/rust-lang-nursery/rustup.rs)

~~~bash
$ curl https://sh.rustup.rs -sSf | sh
.
~~~

Ubuntu:

~~~bash
$ curl https://sh.rustup.rs -sSf | sh
info: downloading installer

Welcome to Rust!

This will download and install the official compiler for the Rust programming 
language, and its package manager, Cargo.

It will add the cargo, rustc, rustup and other commands to Cargo's bin 
directory, located at:

  /home/vagrant/.cargo/bin

This path will then be added to your PATH environment variable by modifying the
profile file located at:

  /home/vagrant/.profile

You can uninstall at any time with rustup self uninstall and these changes will
be reverted.

Current installation options:

   default host triple: x86_64-unknown-linux-gnu
     default toolchain: stable
  modify PATH variable: yes

1) Proceed with installation (default)
2) Customize installation
3) Cancel installation
>1

info: syncing channel updates for 'stable-x86_64-unknown-linux-gnu'
info: latest update on 2018-11-08, rust version 1.30.1 (1433507eb 2018-11-07)
info: downloading component 'rustc'
 76.4 MiB /  76.4 MiB (100 %) 982.4 KiB/s ETA:   0 s                 
info: downloading component 'rust-std'
 52.8 MiB /  52.8 MiB (100 %)   1.8 MiB/s ETA:   0 s                
info: downloading component 'cargo'
  4.4 MiB /   4.4 MiB (100 %)   2.5 MiB/s ETA:   0 s                
info: downloading component 'rust-docs'
  8.9 MiB /   8.9 MiB (100 %)   1.9 MiB/s ETA:   0 s                
info: installing component 'rustc'
info: installing component 'rust-std'
info: installing component 'cargo'
info: installing component 'rust-docs'
info: default toolchain set to 'stable'

  stable installed - rustc 1.30.1 (1433507eb 2018-11-07)


Rust is installed now. Great!

To get started you need Cargo's bin directory ($HOME/.cargo/bin) in your PATH 
environment variable. Next time you log in this will be done automatically.

To configure your current shell run source $HOME/.cargo/env

~~~

~~~bash
$ cat ~/.cargo/env

export PATH="$HOME/.cargo/bin:$PATH"
~~~

~~~bash
$ source ~/.cargo/env
$ which rustc
/home/vagrant/.cargo/bin/rustc
~~~

~~~bash
$ rustup --help
rustup 1.14.0 (1e51b07cc 2018-10-04)
The Rust toolchain installer

USAGE:
    rustup [FLAGS] <SUBCOMMAND>

FLAGS:
    -v, --verbose    Enable verbose output
    -h, --help       Prints help information
    -V, --version    Prints version information

SUBCOMMANDS:
    show           Show the active and installed toolchains
    update         Update Rust toolchains and rustup
    default        Set the default toolchain
    toolchain      Modify or query the installed toolchains
    target         Modify a toolchain's supported targets
    component      Modify a toolchain's installed components
    override       Modify directory toolchain overrides
    run            Run a command with an environment configured for a given toolchain
    which          Display which binary will be run for a given command
    doc            Open the documentation for the current toolchain
    man            View the man page for a given command
    self           Modify the rustup installation
    set            Alter rustup settings
    completions    Generate completion scripts for your shell
    help           Prints this message or the help of the given subcommand(s)

DISCUSSION:
    rustup installs The Rust Programming Language from the official
    release channels, enabling you to easily switch between stable,
    beta, and nightly compilers and keep them updated. It makes
    cross-compiling simpler with binary builds of the standard library
    for common platforms.

    If you are new to Rust consider running `rustup doc --book` to
    learn Rust.
~~~

~~~bash
$ rustup update
info: syncing channel updates for 'stable-x86_64-unknown-linux-gnu'
info: checking for self-updates

  stable-x86_64-unknown-linux-gnu unchanged - rustc 1.30.1 (1433507eb 2018-11-07)
~~~


## 記事

- [rustup で Rust コンパイラーを簡単インストール - Qiita](https://qiita.com/chikoski/items/b6461367e8c3875bb235)
- [HTTPS通信の疎通確認に覚えておきたい３つのコマンド - Qiita](https://qiita.com/greymd/items/68b0c40044a88171235a)

## 2.2 Hello, World!

- [hello, World](hello_world)

## 2.3 Hello, Cargo!

- [hello, Cargo](hello_cargo)
