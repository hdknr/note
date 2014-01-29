Date: 2013-11-20  
Title: rbenv: gem が Permisson Denied でインストール出来ない  
Type: post  
Excerpt:   


ruby バージョン:

    ubuntu@ip-10-0-0-117:~$ which ruby
    /home/ubuntu/.rbenv/shims/ruby
    

bundlerインストールできない:

    ubuntu@ip-10-0-0-117:~$ gem install bundler
    ERROR:  While executing gem ... (Errno::EACCES)
        Permission denied - /var/lib/gems
    
    
gemのパス:

    ubuntu@ip-10-0-0-117:~$ which gem
    /home/ubuntu/.rbenv/shims/gem
    

環境みるとおかしい

    ubuntu@ip-10-0-0-117:~$ gem env
    RubyGems Environment:
      - RUBYGEMS VERSION: 1.8.23
      - RUBY VERSION: 1.9.3 (2012-04-20 patchlevel 194) [x86_64-linux]
      - INSTALLATION DIRECTORY: /var/lib/gems/1.9.1
      - RUBY EXECUTABLE: /usr/bin/ruby1.9.1
      - EXECUTABLE DIRECTORY: /usr/local/bin
      - RUBYGEMS PLATFORMS:
        - ruby
        - x86_64-linux
      - GEM PATHS:
         - /var/lib/gems/1.9.1
         - /home/ubuntu/.gem/ruby/1.9.1
      - GEM CONFIGURATION:
         - :update_sources => true
         - :verbose => true
         - :benchmark => false
         - :backtrace => false
         - :bulk_threshold => 1000
      - REMOTE SOURCES:
         - http://rubygems.org/
         
有効にしていなかったっぽい:
         
    ubuntu@ip-10-0-0-117:~$ rbenv local 1.9.3-p448
    ubuntu@ip-10-0-0-117:~$ rbenv rehash     
    
    ubuntu@ip-10-0-0-117:~$ gem env
    RubyGems Environment:
      - RUBYGEMS VERSION: 1.8.23
      - RUBY VERSION: 1.9.3 (2013-06-27 patchlevel 448) [x86_64-linux]
      - INSTALLATION DIRECTORY: /home/ubuntu/.rbenv/versions/1.9.3-p448/lib/ruby/gems/1.9.1
      - RUBY EXECUTABLE: /home/ubuntu/.rbenv/versions/1.9.3-p448/bin/ruby
      - EXECUTABLE DIRECTORY: /home/ubuntu/.rbenv/versions/1.9.3-p448/bin
      - RUBYGEMS PLATFORMS:
        - ruby
        - x86_64-linux
      - GEM PATHS:
         - /home/ubuntu/.rbenv/versions/1.9.3-p448/lib/ruby/gems/1.9.1
         - /home/ubuntu/.gem/ruby/1.9.1
      - GEM CONFIGURATION:
         - :update_sources => true
         - :verbose => true
         - :benchmark => false
         - :backtrace => false
         - :bulk_threshold => 1000
      - REMOTE SOURCES:
         - http://rubygems.org/
    
インストールできた::
    
    ubuntu@ip-10-0-0-117:~$ gem install bundler
    Fetching: bundler-1.3.5.gem (100%)
    Successfully installed bundler-1.3.5
    1 gem installed
    Installing ri documentation for bundler-1.3.5...
    Installing RDoc documentation for bundler-1.3.5...     

local するとカレントディレクトリに .rbenv-versionができる

    ubuntu@ip-10-0-0-117:~$ more .rbenv-version 
    1.9.3-p448
    
これを削除するともとにもどっていまいます。

グローバルにすると:

    ubuntu@ip-10-0-0-117:~$ rbenv global 1.9.3-p448
    ubuntu@ip-10-0-0-117:~$ more .rbenv/version
    1.9.3-p448
    
    ubuntu@ip-10-0-0-117:~$ gem env | grep "RUBY VERSION"
      - RUBY VERSION: 1.9.3 (2013-06-27 patchlevel 448) [x86_64-linux]
      
削除すると戻る:

    ubuntu@ip-10-0-0-117:~$ rm .rbenv/version
    ubuntu@ip-10-0-0-117:~$ gem env | grep "RUBY VERSION"
      - RUBY VERSION: 1.9.3 (2012-04-20 patchlevel 194) [x86_64-linux]      