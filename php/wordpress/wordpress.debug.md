
## WP_DEBUG
- [WP_DEBUG](https://codex.wordpress.org/WP_DEBUG)
- wp-config.php
- wp-settings.php のロードの前に設定すること

~~~php
define('WP_DEBUG', true);
define('WP_DEBUG_LOG', true);

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
~~~

- プラグインモジュールアプリケーション

~~~php
<?php
namespace Authmod;

class App extends AppBase {

    function filter_the_title($title){
        error_log("filter:the_title");
        return "$title (debugging)";
    } 

    function filter_query_vars($qvars){
        error_log("filter:query_vars");
        return $qvars + array('authmod');
    }

    function action_init(){
        error_log("action:init");
    }

    function action_template_redirect(){
        error_log("action:template_redirect");
    }

    function action_pre_get_posts(){
        error_log("action:pre_get_posts");
    }
}
~~~

~~~bash
$ tail wp-content/debug.log 

[13-Aug-2015 00:02:34 UTC] filter:query_vars
[13-Aug-2015 00:02:34 UTC] action:pre_get_posts
[13-Aug-2015 00:02:34 UTC] action:template_redirect
[13-Aug-2015 00:02:34 UTC] action:pre_get_posts
[13-Aug-2015 00:02:34 UTC] filter:the_title
~~~