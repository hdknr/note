OSX: Shellshock祭りに参加してみました

[Every Mac Is Vulnerable to the Shellshock Bash Exploit: Here's How to Patch OS X](http://mac-how-to.wonderhowto.com/how-to/every-mac-is-vulnerable-shellshock-bash-exploit-heres-patch-os-x-0157606/)の通りにxcodeビルドでパッチあてたbashをインストールしてみただけのログ

# ソース取得
~~~
Peeko:~ hide$ cd Downloads/
Peeko:Downloads hide$ mkdir bash-fix
Peeko:Downloads hide$ cd bash-fix
Peeko:bash-fix hide$ curl https://opensource.apple.com/tarballs/bash/bash-92.tar.gz | tar zxf -
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 4088k  100 4088k    0     0   374k      0  0:00:10  0:00:10 --:--:--  737k
~~~

# パッチあて

~~~
Peeko:bash-fix hide$ cd bash-92/bash-3.2
Peeko:bash-3.2 hide$ curl https://ftp.gnu.org/pub/gnu/bash/bash-3.2-patches/bash32-052 | patch -p0
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  3250  100  3250    0     0   1087      0  0:00:02  0:00:02 --:--:--  1086
patching file builtins/common.h
patching file builtins/evalstring.c
patching file variables.c
patching file patchlevel.h
~~~

# xcodebuild
~~~
Peeko:bash-3.2 hide$ cd ..
Peeko:bash-92 hide$ xcodebuild
...
Ld build/Release/bash normal x86_64
    cd /Users/hide/Downloads/bash-fix/bash-92
    export MACOSX_DEPLOYMENT_TARGET=10.9
    /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -arch x86_64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.9.sdk -L/Users/hide/Downloads/bash-fix/bash-92/build/Release -F/Users/hide/Downloads/bash-fix/bash-92/build/Release -filelist /Users/hide/Downloads/bash-fix/bash-92/build/bash.build/Release/bash.build/Objects-normal/x86_64/bash.LinkFileList -mmacosx-version-min=10.9 -Wl,-search_paths_first -lintl -lreadline -lsh -lglob -lncurses -Xlinker -dependency_info -Xlinker /Users/hide/Downloads/bash-fix/bash-92/build/bash.build/Release/bash.build/Objects-normal/x86_64/bash_dependency_info.dat -o /Users/hide/Downloads/bash-fix/bash-92/build/Release/bash

=== BUILD AGGREGATE TARGET all OF PROJECT bash WITH THE DEFAULT CONFIGURATION (Release) ===

Check dependencies
The file “BSD.xcconfig” couldn’t be opened because there is no such file. (/Applications/Xcode.app/Contents/Developer/Makefiles/CoreOS/Xcode/BSD.xcconfig)

** BUILD SUCCEEDED **
~~~

# バックアップ

~~~
Peeko:bash-92 hide$ sudo cp /bin/bash /bin/bash.old
Password:
Peeko:bash-92 hide$ sudo cp /bin/sh /bin/sh.old
~~~

# バージョン確認

~~~
Peeko:bash-92 hide$ build/Release/bash --version
GNU bash, version 3.2.52(1)-release (x86_64-apple-darwin13)
Copyright (C) 2007 Free Software Foundation, Inc.
Peeko:bash-92 hide$ build/Release/sh --version
GNU bash, version 3.2.52(1)-release (x86_64-apple-darwin13)
Copyright (C) 2007 Free Software Foundation, Inc.
~~~

# コピー
~~~
Peeko:bash-92 hide$ sudo cp build/Release/bash /bin
Peeko:bash-92 hide$ sudo cp build/Release/sh /bin
~~~

# 確認

~~~
Peeko:bash-92 hide$ env x='() { :;}; echo vulnerable' bash -c "echo this is a test"

bash: warning: x: ignoring function definition attempt
bash: error importing function definition for `x'
this is a test
~~~
