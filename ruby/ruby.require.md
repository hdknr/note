- [ロード](http://i.loveruby.net/ja/rhg/book/load.html)

## ロードパス
- rbenv での ロードパス

~~~bash
$ ruby -e 'puts $:'
/home/vagrant/.anyenv/envs/rbenv/rbenv.d/exec/gem-rehash
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/site_ruby/2.2.0
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/site_ruby/2.2.0/x86_64-linux
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/site_ruby
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/vendor_ruby/2.2.0
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/vendor_ruby/2.2.0/x86_64-linux
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/vendor_ruby
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/2.2.0
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/2.2.0/x86_64-linux
~~~

## ローディング

- require
- load

### require

- ロードパスからファイルを探してくる
- 拡張ライブラリもロードできる
- 拡張子.rb/.soを省略できる
- 同じファイルは二度以上ロードしない

### load

- ロードパスからファイルを探してくる
- ロードできるのはRubyプログラムだけ。
- また拡張子は省略できず、 常に完全なファイル名を指定しないといけない。
- 同じファイルは二度以上ロードしない


## RUBYLIB

~~~bash
$ echo $PWD
/home/vagrant/projects/helloruby

$ export RUBYLIB=$PWD

$ ruby -e 'puts $:'
/home/vagrant/.anyenv/envs/rbenv/rbenv.d/exec/gem-rehash
/home/vagrant/projects/helloruby
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/site_ruby/2.2.0
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/site_ruby/2.2.0/x86_64-linux
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/site_ruby
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/vendor_ruby/2.2.0
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/vendor_ruby/2.2.0/x86_64-linux
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/vendor_ruby
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/2.2.0
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/2.2.0/x86_64-linux
~~~

## $LOADPATH

~~~bash
$ cat hello.rb
puts $LOAD_PATH
~~~

~~~bash
$ ruby hello.rb

/home/vagrant/.anyenv/envs/rbenv/rbenv.d/exec/gem-rehash
/home/vagrant/projects/helloruby
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/site_ruby/2.2.0
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/site_ruby/2.2.0/x86_64-linux
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/site_ruby
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/vendor_ruby/2.2.0
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/vendor_ruby/2.2.0/x86_64-linux
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/vendor_ruby
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/2.2.0
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/2.2.0/x86_64-linux
~~~

~~~bash
$ cat hello.rb
$LOAD_PATH.push('/tmp')
$LOAD_PATH.insert(0, '/var')
puts $LOAD_PATH
~~~

~~~bash
$ ruby hello.rb
/var
/home/vagrant/.anyenv/envs/rbenv/rbenv.d/exec/gem-rehash
/home/vagrant/projects/helloruby
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/site_ruby/2.2.0
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/site_ruby/2.2.0/x86_64-linux
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/site_ruby
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/vendor_ruby/2.2.0
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/vendor_ruby/2.2.0/x86_64-linux
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/vendor_ruby
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/2.2.0
/home/vagrant/.anyenv/envs/rbenv/versions/2.2.2/lib/ruby/2.2.0/x86_64-linux
/tmp
~~~

## Gem.find_files

~~~ruby
irb(main):004:0>  Gem.find_files('animals')
=> ["/home/vagrant/projects/helloruby/animals.rb"]
~~~

## 参照

- [クラス・モジュールの概念 Ruby](http://qiita.com/ToruFukui/items/2dd4d2d1ce6ed05928de)

### 名前空間

~~~
$ cat animals.rb
~~~
~~~ruby
class Cat
  def tuna
    "good"
  end
end

module Zoo

  class Cat  

    def tuna
      "delicious"
    end
  end

end
~~~

~~~ruby
$ irb
irb(main):001:0> require "animals"
=> true
irb(main):002:0> Cat.new.tuna
=> "good"
irb(main):003:0> Zoo::Cat.new.tuna
=> "delicious"
~~~
