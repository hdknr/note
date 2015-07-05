SRC=logger.swift
TEST=hello.swift
NAME=Logger

SSDK=$(xcrun --show-sdk-path --sdk macosx)
SWIFT="xcrun swift -I ./ -L ./ -sdk $SSDK"
SWIFTC="xcrun swiftc -sdk $SSDK"
SWL=/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/macosx
LTOPT="-lSystem -L$SWL -macosx_version_min 10.10"
#
# 1. echo モジュール作成
# (swift import 用)
$SWIFTC -emit-module -module-name $NAME $SRC

# 2. オブジェクトコード作成(Mach-O 64-bit object x86_64)
$SWIFTC -emit-object -o $NAME.o $SRC

# 3. シェアードライブラリ作成
# (Mach-O 64-bit dynamically linked shared library x86_64)
# -  lib{{ name }}.dynlib という名前にする
libtool $LTOPT -dynamic -o lib$NAME.dylib $NAME.o

# 4. テストコードを直接実行する
$SWIFT -l$NAME $TEST
