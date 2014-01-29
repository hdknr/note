Date: 2013-09-04  16:00
Title: Django: Gunicornでhttpsのリクエストをリダイレクとするとhttpになる問題
Type: post  
Excerpt:   


Apacheでhttpにプロキシしているので、Gunicorn配下のDjangoがhttpでリクエストされているとおもって、httpにリダイレクトしてしまう。

ので、apacheでヘッダーを追加すると良いようです。:

    <VirtualHost *:443>
    #...
    RequestHeader set X-FORWARDED_PROTO "https"

で、

    Invalid command 'RequestHeader', perhaps misspelled or defined by a module not included in the server configuration

なので、mod_headersを追加する:

    $ sudo a2enmod headers
    Enabling module headers.
    To activate the new configuration, you need to run:
      service apache2 restart