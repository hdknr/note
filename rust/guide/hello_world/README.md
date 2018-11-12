# [Hello, world!](https://doc.rust-lang.org/1.2.0/book/hello-world.html)


~~~bash
$ rustc main.rs
$ tree .
.
├── main
└── main.rs

0 directories, 2 files

$ file main
main: Mach-O 64-bit executable x86_64


$ ./main
Hello, world!
~~~

## `main`

- エントリポイント

## 関数

- 引数: `(`, `)`
- 定義: `{`,  `}`

## マクロ(`!`)呼び出し

- [Macros](https://doc.rust-lang.org/1.2.0/book/macros.html)

## コーディング規約

- 4スペースタブ
- 関数名 と`{` の間に１空白
- https://github.com/rust-lang/rust/blob/master/src/etc/CONFIGS.md

## `"文字列"`

- `statically allocated`
- [The Stack and the Heap](https://doc.rust-lang.org/1.2.0/book/the-stack-and-the-heap.html)

## 式(expression) (`;`)

- `expression oriented`
