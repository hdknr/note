// main 関数は特別で、全てのRustプログラムの開始点
// 引数を取らず、返り値も返さない関数 main を宣言します

fn main() { //  { と } : 関数宣言と同じ行にスペースを1つ空けて開き波括弧を置くのが、良いスタイルとされます。
    // インデントが4スペースであり、タブでない
    println!("Hello, world!");      // 行はセミコロン(;)で終わります
    // !: マクロ呼びだし( https://doc.rust-jp.rs/the-rust-programming-language-ja/1.6/book/macros.html)

    // 式指向言語: 
    // ほとんど式であり、文でない
    // https://doc.rust-jp.rs/the-rust-programming-language-ja/1.6/book/glossary.html#%E5%BC%8F%E6%8C%87%E5%90%91%E8%A8%80%E8%AA%9E
}