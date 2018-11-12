# [Hello, Cargo!](https://doc.rust-lang.org/1.2.0/book/hello-cargo.html)

- [Rustaceans](https://www.rustaceans.org/)
- [rust-lang/cargo: The Rust package manager](https://github.com/rust-lang/cargo#installing-cargo-from-nightlies)

Cargo:

- building your code
- downloading the dependencies your code needs
- building those dependencies.

Carge.tom([TOML](https://github.com/toml-lang/toml)):

~~~ini
[package]

name = "hello_world"
version = "0.0.1"
authors = [ "hdknr <hdknr@example.com>" ]
~~~

~~~bash
$ tree .
.
├── Cargo.toml
├── README.md
└── src
    └── main.rs

1 directory, 3 files
~~~

~~~bash
$ cargo build
   Compiling hello_world v0.0.1 (/Users/hide/Documents/Tech/scriptogram/rust/guide/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 3.77s
~~~

~~~bash
 tree . -a
.
├── Cargo.lock
├── Cargo.toml
├── README.md
├── src
│   └── main.rs
└── target
    ├── .rustc_info.json
    └── debug
        ├── .cargo-lock
        ├── .fingerprint
        │   └── hello_world-f8d0bcb25c6dce93
        │       ├── bin-hello_world-f8d0bcb25c6dce93
        │       ├── bin-hello_world-f8d0bcb25c6dce93.json
        │       └── dep-bin-hello_world-f8d0bcb25c6dce93
        ├── build
        ├── deps
        │   ├── hello_world-f8d0bcb25c6dce93
        │   ├── hello_world-f8d0bcb25c6dce93.d
        │   └── hello_world-f8d0bcb25c6dce93.dSYM
        │       └── Contents
        │           ├── Info.plist
        │           └── Resources
        │               └── DWARF
        │                   └── hello_world-f8d0bcb25c6dce93
        ├── examples
        ├── hello_world
        ├── hello_world.d
        ├── hello_world.dSYM -> deps/hello_world-f8d0bcb25c6dce93.dSYM
        ├── incremental
        │   └── hello_world-j7obrgmydb8o
        │       ├── s-f6llmsoeee-1nedoky-3inm0679hjb1x
        │       │   ├── 1a85sb6n6hvpzfr6.o
        │       │   ├── 1kp776cemnmsjsi9.o
        │       │   ├── 233xk7c1lulv918w.o
        │       │   ├── 3pedocgrcyv3da6j.o
        │       │   ├── 4mtio3wmhub32p01.o
        │       │   ├── 4zegdz9voixm1hq8.o
        │       │   ├── dep-graph.bin
        │       │   ├── query-cache.bin
        │       │   └── work-products.bin
        │       └── s-f6llmsoeee-1nedoky.lock
        └── native

17 directories, 25 files
~~~

~~~bash
$ cargo run

    Finished dev [unoptimized + debuginfo] target(s) in 0.01s
     Running `target/debug/hello_world`

Hello, world!
~~~

Cargo.lock(依存関係の保持):

~~~ini
[[package]]
name = "hello_world"
version = "0.0.1"
~~~