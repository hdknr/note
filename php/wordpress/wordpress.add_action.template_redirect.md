## add_action: template_redirect

- プラグインメインファイル

~~~php
Class WPOA {	
	// ends the login request by clearing the login state and redirecting the user to the desired page:
	// "login-provider.php"の中で幾つかの処理分岐されて呼ばれるメソッドの一つ
	// 最後にリダイレクトして終了
	function wpoa_end_login($msg) {
		$last_url = $_SESSION["WPOA"]["LAST_URL"];
		unset($_SESSION["WPOA"]["LAST_URL"]);
		$_SESSION["WPOA"]["RESULT"] = $msg;
		$this->wpoa_clear_login_state();
		$redirect_method = get_option("wpoa_login_redirect");
		$redirect_url = "";
		
		switch ($redirect_method) {
			case "home_page":
				$redirect_url = site_url();
				break;
			case "last_page":
				$redirect_url = $last_url;
				break;
			case "specific_page":
				$redirect_url = get_permalink(get_option('wpoa_login_redirect_page'));
				break;
			case "admin_dashboard":
				$redirect_url = admin_url();
				break;
			case "user_profile":
				$redirect_url = get_edit_user_link();
				break;
			case "custom_url":
				$redirect_url = get_option('wpoa_login_redirect_url');
				break;
		}
		//header("Location: " . $redirect_url);
		wp_safe_redirect($redirect_url);
		die();
	}
	
	// Queryの処理の実態($providerごとに異なる)
	function wpoa_include_connector($provider) {
		// called by `wpoa_qvar_handlers` <- `template_redirect` action
		
		// normalize the provider name (no caps, no spaces):
		$provider = strtolower($provider);
		$provider = str_replace(" ", "", $provider);
		$provider = str_replace(".", "", $provider);
		// include the provider script:
		include 'login-' . $provider . '.php';  // 動的にイクルードするファイルを決めて処理を分岐
	}
	
	// define the querystring variables that should trigger an action:
	// このプラグインは [connect, code, error_description, error_message]
	// を判定して処理を分岐させる	
	function wpoa_qvar_triggers($vars) {
		$vars[] = 'connect';
		$vars[] = 'code';
		$vars[] = 'error_description';
		$vars[] = 'error_message';
		return $vars;
	}
		
	// handle the querystring triggers:
	function wpoa_qvar_handlers() {
		if (get_query_var('connect')) {
			// 処理providerが決まる(あとで$_SESSIONに入れる)
			$provider = get_query_var('connect');
			$this->wpoa_include_connector($provider);
		}
		elseif (get_query_var('code')) {
			$provider = $_SESSION['WPOA']['PROVIDER']; // セッションからプロバイダ復元
			$this->wpoa_include_connector($provider);
		}
		elseif (get_query_var('error_description') || get_query_var('error_message')) {
			$provider = $_SESSION['WPOA']['PROVIDER']; // セッションからプロバイダ復元
			$this->wpoa_include_connector($provider);
		}
	}

	function init() {
		// URLのQueryに応じて処理をディスパッチする
		add_filter('query_vars', array($this, 'wpoa_qvar_triggers'));
		add_action('template_redirect', array($this, 'wpoa_qvar_handlers'));
		// その他の処理....
	}

	function __construct() {
		// そのほかの処理....
		add_action('init', array($this, 'init'));
	}

	// singleton class pattern:
	protected static $instance = NULL;
	public static function get_instance() {
		NULL === self::$instance and self::$instance = new self;
		return self::$instance;
	}
}

WPOA::get_instance();
~~~
		
