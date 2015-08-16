- [admin_menu](https://codex.wordpress.org/Plugin_API/Action_Reference/admin_menu)

~~~php
	function init() {
		...
		add_action('admin_menu', array($this, 'wpoa_settings_page'));
	}
~~~

- [add_options_page](https://codex.wordpress.org/Function_Reference/add_options_page)

~~~php
	// add the main settings page:
	function wpoa_settings_page() {
		add_options_page( 
			'WP-OAuth Options',		// ページタイトル
			'WP-OAuth', 				// メニュータイトル
			'manage_options', 		// 権限
			'WP-OAuth', 				// メニュースラグ
			array($this, 'wpoa_settings_page_content') // 設定ページ処理関数
		);
	}
~~~	

- 設定ページ関数

~~~php
	function wpoa_settings_page_content() {
		if ( !current_user_can( 'manage_options' ) )  {
			wp_die( __( 'You do not have sufficient permissions to access this page.' ) );
		}
		$blog_url = rtrim(site_url(), "/") . "/";
		include 'wp-oauth-settings.php';	 // ここで設定ページが処理されている
	}
~~~
