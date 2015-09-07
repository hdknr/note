## C bindings : node-ffi
- Node.js Forei gn Function Interface
- [node-ffi/node-ffi](https://github.com/node-ffi/node-ffi)

  node-ffi is a Node.js addon for loading
  and calling dynamic libraries using pure JavaScript.

  It can be used to create bindings
  to native libraries without writing any C++ code.


### for Windows

- [Installing node-ffi on Windows](https://www.evernote.com/shard/s302/sh/fc17c52a-8da3-4795-8afd-a13a3df4098b/43ab31e6e27c1fcb0f9ad1d4828738b6)
- [Call Windows API from node.js msg](https://www.evernote.com/shard/s302/sh/139ea525-d6c7-43ce-906d-9250d4af68a4/5466cc4d068654a0c02305819b4cd1850)

### for Mac

- [node-ffiの公式版をAtom Shellやio.jsで使うには](http://qiita.com/kjunichi/items/9afc1122408377a81dbc)
- [node-ffiを利用してダイナミックライブラリの関数を呼び出す(Mac OS X)](https://www.evernote.com/shard/s302/sh/8ce5725e-ee68-493e-9f5c-e02aabf8438f/b6d0a478ba1b3af53db103480fee9e32)


## Java bindigns: node-java

- [joeferner/node-java](https://github.com/joeferner/node-java)


## .NET bindings: Edge.js

- [Run .NET and Node.js code in-process with Edge.js](http://harajuku-tech.org/post/127822787895/edgejs-provides-an-alternative-way-of-composing)
- [Edge.js Adds Support for Linux and Mac OS X So C# and Node.js Can Run Anywhere](http://harajuku-tech.org/post/127822996215/now-by-supporting-mono-new-edgejs-version-080)

### Mono

- [MonoMacPackager](http://www.mono-project.com/archived/monomacpackager/)
- [create Package for MAC OSX - Xamarin Forums](http://harajuku-tech.org/post/127823987660/project-options-mac-os-x-packaging)
- [コンソールプログラムをMonoインストールなしで実行する](http://qiita.com/ailen0ada/items/8f1a440c5d620a53c02e)
- [Guide:Running Mono Applications](http://www.mono-project.com/archived/guiderunning_mono_applications/)

    mkbundle, macpack コマンド

#### macpack

~~~bash
$ man mackpack
~~~
~~~bash
$ macpack

Error: No assembly to macpack was specified

Usage is:
macpack [options] assembly
   -n appname  -appname:appname    Application Name
   -o output   -output:OUTPUT      Output directory
   -a assembly                     Assembly to pack
   -i file     -icon file          Icon filename
   -r resource1,resource2          Additional files to bundle
   -m [winforms|cocoa|x11|console] The mode for the application
~~~
