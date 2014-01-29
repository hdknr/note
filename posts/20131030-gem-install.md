Date: 2013-10-30  5:30
Title: Ruby:rbenvの環境にRubyGemsを入れてみる
Type: post  
Excerpt:   


@novさんの opneid_connectを rbenvのrubyに入れてみる。

    hdknr@wzy:~/rubys$ git clone https://github.com/nov/openid_connect.git
    Cloning into 'openid_connect'...
    remote: Counting objects: 2409, done.
    remote: Compressing objects: 100% (1230/1230), done.
    remote: Total 2409 (delta 927), reused 2382 (delta 900)
    Receiving objects: 100% (2409/2409), 350.96 KiB | 312 KiB/s, done.
    Resolving deltas: 100% (927/927), done.


    hdknr@wzy:~/rubys$ cd openid_connect/

gem buildする:

    hdknr@wzy:~/rubys/openid_connect$ gem build openid_connect.gemspec 
    WARNING:  description and summary are identical
      Successfully built RubyGem
      Name: openid_connect
      Version: 0.7.3
      File: openid_connect-0.7.3.gem
      
    
    hdknr@wzy:~/rubys/openid_connect$ ls -l *.gem
    -rw-r--r-- 1 hdknr hdknr 29184 10月 30 05:19 openid_connect-0.7.3.gem


gem install 。依存gemsも入るよ: 

    hdknr@wzy:~/rubys/openid_connect$ gem install openid_connect-0.7.3.gem 
    Fetching: tzinfo-0.3.38.gem (100%)
    Fetching: attr_required-0.0.5.gem (100%)
    Fetching: i18n-0.6.5.gem (100%)
    Fetching: multi_json-1.8.2.gem (100%)
    Fetching: minitest-4.7.5.gem (100%)
    Fetching: atomic-1.1.14.gem (100%)
    Building native extensions.  This could take a while...
    Fetching: thread_safe-0.1.3.gem (100%)
    Fetching: activesupport-4.0.0.gem (100%)
    Fetching: builder-3.1.4.gem (100%)
    Fetching: activemodel-4.0.0.gem (100%)
    Fetching: validate_url-0.2.0.gem (100%)
    Fetching: mime-types-1.25.gem (100%)
    Fetching: polyglot-0.3.3.gem (100%)
    Fetching: treetop-1.4.15.gem (100%)
    Fetching: mail-2.5.4.gem (100%)
    Fetching: validate_email-0.1.6.gem (100%)
    Fetching: url_safe_base64-0.2.2.gem (100%)
    Fetching: bindata-1.6.0.gem (100%)
    Fetching: json-jwt-0.6.0.gem (100%)
    Fetching: httpclient-2.3.4.1.gem (100%)
    Fetching: swd-0.2.1.gem (100%)
    Fetching: webfinger-1.0.0.gem (100%)
    Fetching: rack-1.5.2.gem (100%)
    Fetching: rack-oauth2-1.0.5.gem (100%)
    Successfully installed tzinfo-0.3.38
    Successfully installed attr_required-0.0.5
    Successfully installed i18n-0.6.5
    Successfully installed multi_json-1.8.2
    Successfully installed minitest-4.7.5
    Successfully installed atomic-1.1.14
    Successfully installed thread_safe-0.1.3
    Successfully installed activesupport-4.0.0
    Successfully installed builder-3.1.4
    Successfully installed activemodel-4.0.0
    Successfully installed validate_url-0.2.0
    Successfully installed mime-types-1.25
    Successfully installed polyglot-0.3.3
    Successfully installed treetop-1.4.15
    Successfully installed mail-2.5.4
    Successfully installed validate_email-0.1.6
    Successfully installed url_safe_base64-0.2.2
    Successfully installed bindata-1.6.0
    Successfully installed json-jwt-0.6.0
    Successfully installed httpclient-2.3.4.1
    Successfully installed swd-0.2.1
    Successfully installed webfinger-1.0.0
    Successfully installed rack-1.5.2
    Successfully installed rack-oauth2-1.0.5
    Successfully installed openid_connect-0.7.3
    25 gems installed
    Installing ri documentation for tzinfo-0.3.38...
    Installing ri documentation for attr_required-0.0.5...
    Installing ri documentation for i18n-0.6.5...
    Installing ri documentation for multi_json-1.8.2...
    Installing ri documentation for minitest-4.7.5...
    Installing ri documentation for atomic-1.1.14...
    Installing ri documentation for thread_safe-0.1.3...
    Installing ri documentation for activesupport-4.0.0...
    Installing ri documentation for builder-3.1.4...
    Installing ri documentation for activemodel-4.0.0...
    Installing ri documentation for validate_url-0.2.0...
    Installing ri documentation for mime-types-1.25...
    Installing ri documentation for polyglot-0.3.3...
    Installing ri documentation for treetop-1.4.15...
    Installing ri documentation for mail-2.5.4...
    Installing ri documentation for validate_email-0.1.6...
    Installing ri documentation for url_safe_base64-0.2.2...
    Installing ri documentation for bindata-1.6.0...
    Installing ri documentation for json-jwt-0.6.0...
    Installing ri documentation for httpclient-2.3.4.1...
    Installing ri documentation for swd-0.2.1...
    Installing ri documentation for webfinger-1.0.0...
    Installing ri documentation for rack-1.5.2...
    Installing ri documentation for rack-oauth2-1.0.5...
    Installing ri documentation for openid_connect-0.7.3...
    Installing RDoc documentation for tzinfo-0.3.38...
    Installing RDoc documentation for attr_required-0.0.5...
    Installing RDoc documentation for i18n-0.6.5...
    Installing RDoc documentation for multi_json-1.8.2...
    Installing RDoc documentation for minitest-4.7.5...
    Installing RDoc documentation for atomic-1.1.14...
    Installing RDoc documentation for thread_safe-0.1.3...
    Installing RDoc documentation for activesupport-4.0.0...
    Installing RDoc documentation for builder-3.1.4...
    Installing RDoc documentation for activemodel-4.0.0...
    Installing RDoc documentation for validate_url-0.2.0...
    Installing RDoc documentation for mime-types-1.25...
    Installing RDoc documentation for polyglot-0.3.3...
    Installing RDoc documentation for treetop-1.4.15...
    Installing RDoc documentation for mail-2.5.4...
    Installing RDoc documentation for validate_email-0.1.6...
    Installing RDoc documentation for url_safe_base64-0.2.2...
    Installing RDoc documentation for bindata-1.6.0...
    Installing RDoc documentation for json-jwt-0.6.0...
    Installing RDoc documentation for httpclient-2.3.4.1...
    Installing RDoc documentation for swd-0.2.1...
    Installing RDoc documentation for webfinger-1.0.0...
    Installing RDoc documentation for rack-1.5.2...
    Installing RDoc documentation for rack-oauth2-1.0.5...
    Installing RDoc documentation for openid_connect-0.7.3...

確認:

    hdknr@wzy:~/rubys/openid_connect$ gem list
    
    *** LOCAL GEMS ***
    
    activemodel (4.0.0)
    activesupport (4.0.0)
    atomic (1.1.14)
    attr_required (0.0.5)
    bigdecimal (1.1.0)
    bindata (1.6.0)
    builder (3.1.4)
    httpclient (2.3.4.1)
    i18n (0.6.5)
    io-console (0.3)
    json (1.5.5)
    json-jwt (0.6.0)
    mail (2.5.4)
    mime-types (1.25)
    minitest (4.7.5, 2.5.1)
    multi_json (1.8.2)
    openid_connect (0.7.3)
    polyglot (0.3.3)
    rack (1.5.2)
    rack-oauth2 (1.0.5)
    rake (0.9.2.2)
    rdoc (3.9.5)
    swd (0.2.1)
    thread_safe (0.1.3)
    treetop (1.4.15)
    tzinfo (0.3.38)
    url_safe_base64 (0.2.2)
    validate_email (0.1.6)
    validate_url (0.2.0)
    webfinger (1.0.0)

jsonを確認。:

    hdknr@wzy:~ $ irb
    irb(main):001:0> Gem.find_files('json')
    => ["/home/hdknr/.rbenv/versions/1.9.3-p448/lib/ruby/1.9.1/json.rb", 
       "/home/hdknr/.rbenv/versions/1.9.3-p448/lib/ruby/gems/1.9.1/gems/json-jwt-0.6.0/lib/json"]  
    
