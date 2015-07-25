Swift: 共通モジュールを作ってスクリプトから参照

- モジュールはdylibで作る必要あり
- 型の参照が必要なので、.swiftmodule も必要

# Loggerモジュールを用意

~~~
Peeko:Downloads hide$ mkdir sample
Peeko:Downloads hide$ cd sample/
~~~

## logger.swift

~~~
import Foundation

public class Logger
{
    var prefix: String
    
    public init(_ prefix: String) 
    {
        self.prefix = prefix
    }
    
    public func log(msg: String)
    {
        print(prefix)
        println(msg)
    }
}
~~~

# コンパイルしてモジュールとオブジェクトコード作成

## モジュール & doc (swiftc)

~~~
Peeko:sample hide$ xcrun -sdk iphonesimulator8.0 swiftc -emit-module logger.swift -module-name Logger

Peeko:sample hide$ file *
Logger.swiftdoc:    data
Logger.swiftmodule: data
logger.swift:       ASCII Java program text
~~~

## Mach-O オブジェクト (swiftc)

~~~
Peeko:sample hide$ xcrun -sdk iphonesimulator8.0 swiftc -emit-object -o Logger.o logger.swift

Peeko:sample hide$ file *
Logger.o:           Mach-O 64-bit object x86_64
Logger.swiftdoc:    data
Logger.swiftmodule: data
logger.swift:       ASCII Java program text
~~~


# dylib 作成 (libtool)

~~~
Peeko:sample hide$ export SWL=/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/iphonesimulator
~~~

~~~
Peeko:sample hide$ libtool -dynamic  -L$SWL -o libLogger.dylib  Logger.o /usr/lib/libSystem.dylib
ld: warning: -macosx_version_min not specified, assuming 10.10
~~~

こっちでもよさそう

~~~
Peeko:sample hide$ libtool -dynamic  -L$SWL -o libLogger.dylib  Logger.o -lSystem
~~~

~~~
Peeko:sample hide$ file *
Logger.o:           Mach-O 64-bit object x86_64
Logger.swiftdoc:    data
Logger.swiftmodule: data
libLogger.dylib:    Mach-O 64-bit dynamically linked shared library x86_64
logger.swift:       ASCII Java program text
~~~

# アプリ作成

## hello.swift

~~~
import Logger

var logger = Logger("> ")
logger.log(String("Hello"))
~~~

# 実行 (swift)

~~~
Peeko:sample hide$ xcrun -sdk iphonesimulator8.0 swift -I . -L . -lLogger hello.swift
~~~

~~~
> Hello
~~~


# リソース

- [.soや.dylibや.aファイル、共有ライブラリなどについて調べてみた - kanonjiの日記](https://www.evernote.com/shard/s302/sh/2e0a0cd5-ed3b-4a8f-9993-5210383de2e7/f6f709ca125d30c2ab0d6c992b731897)