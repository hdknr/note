## gettext

- [Gettext 関数 ](https://secure.php.net/manual/ja/ref.gettext.php)


## 簡単な例
- 確認

~~~bash
$ php -r "var_dump(function_exists('gettext'));"
bool(true)
~~~

~~~php
<?php

$lang = "ja_JP.UTF-8";
$domain = "messages";
setlocale(LC_ALL, $lang);

bindtextdomain($domain, "./locale/");
textdomain($domain);

echo _("hello world");
?>
~~~

~~~bash
$ xgettext test.php -o locale/ja_JP.UTF-8/LC_MESSAGES/messages.po 
~~~

~~~bash
$ vim locale/ja_JP.UTF-8/LC_MESSAGES/
~~~

~~~
$ msgfmt locale/ja_JP.UTF-8/LC_MESSAGES/messages.po -o locale/ja_JP.UTF-8/LC_MESSAGES/messages.mo 
~~~

### 現在のパス以下のファイル

~~~bash
$ find . -iname "*.php" | xargs xgettext --from-code=UTF-8 -o locale/ja_JP.UTF-8/LC_MESSAGES/messages.po
~~~

## Wordpress

- ./wp-includes/l10n.php で処理しています
- require_onceされています

~~~php
require_once( ABSPATH . WPINC . '/l10n.php' );
~~~

### ロード

bindtextdomainはつかわないで、moファイルを解析して内部で管理している

- wp-includes/pomo/po.php
- wp-includes/pomo/mo.php
- wp-includes/pomo/translations.php 
- wp-includes/pomo/streams.php 