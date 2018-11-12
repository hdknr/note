# cargo new

~~~bash
$ cargo new hello_world --bin

     Created binary (application) `hello_world` project
~~~

~~~bash
$ tree .
.
├── README.md
└── hello_world
    ├── Cargo.toml
    └── src
        └── main.rs

2 directories, 3 files
~~~

Cargo.toml:

~~~ini
[package]
name = "hello_world"
version = "0.1.0"
authors = ["hdknr <gmail@foo.com>"]

[dependencies]
~~~

main.rs:

~~~rust
fn main() {
    println!("Hello, world!");
}
~~~

~~~bash
$ cd hello_world

$ cargo run
   Compiling hello_world v0.1.0 (/Users/hide/Documents/Tech/scriptogram/rust/guide/hello_cargo/cargo_new/hello_world)
    Finished dev [unoptimized + debuginfo] target(s) in 0.42s
     Running `target/debug/hello_world`
Hello, world!
~~~