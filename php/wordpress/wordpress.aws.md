## ELBで HTTPSの無限ループ対策


wp-config.phpでSSLで動いているように騙す:

~~~php
/** SSL対策 */
define('FORCE_SSL_LOGIN', true);
define('FORCE_SSL_ADMIN', true);

if (isset($_SERVER['HTTP_X_FORWARDED_PROTO']) && $_SERVER['HTTP_X_FORWARDED_PROTO'] == 'https')
{
    $_SERVER['HTTPS'] = 'on';
}
~~~

## ELB クラスタ

- アップロードファイルをS3へ: S3 でのアセット/スタティック管理
- CDNでアセット/スタティックをS3に、コンテンツをクラスタに振り分ける
