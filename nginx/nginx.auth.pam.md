- [nginx の light,full,extra の違い ( ubuntu編 )](http://blog.it.churaumi.tv/nginx-light-full-extra-configure-compare)
- [nginx の configure オプションを確認する](https://chocoby.jp/blog/2010/11/10/nginx-show-configure-arguments/)
- [stogh/ngx_http_auth_pam_module](https://github.com/stogh/ngx_http_auth_pam_module)

## ngx_http_auth_pam_module

コンパイル:

~~~bash
$ ./configure --add-module=$PATH_TO_MODULE
~~~

## pam の確認

~~~bash
$ sudo nginx -V  2>&1 |  sed 's/--/\n--/g' | grep pam

--add-module=/build/nginx-ryOGNl/nginx-1.6.2/debian/modules/nginx-auth-pam
~~~
