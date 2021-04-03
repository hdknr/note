# 組み込み変数(Embedded Variables) ([ngx_http_core_module](https://nginx.org/en/docs/http/ngx_http_core_module.html#variables)) 



The ngx_http_core_module module supports embedded variables with names matching the Apache Server variables. First of all, these are variables representing client request header fields, such as $http_user_agent, $http_cookie, and so on. Also there are other variables:

`$proxy_protocol_***` : `listen` で proxy_protocol パラメータが設定されている時だけ

| **name**                    | **PROXYプロトコルヘッダー**   | **apach** |
| --------------------------- | ----------------------------- | --------- |
| $proxy_protocol_addr        | クライアントアドレス (1.5.12) |           |
| $proxy_protocol_port        | クライアントポート(1.11.0)    |           |
| $proxy_protocol_server_addr | サーバーアドレス (1.17.6)     |           |
| $proxy_protocol_server_port | サーバーポート (1.17.6)       |           |


`$request_body`:

    The variable’s value is made available in locations processed by the proxy_pass, fastcgi_pass, uwsgi_pass, and scgi_pass directives when the request body was read to a memory buffer.

`$request_body_file`:

    At the end of processing, the file needs to be removed. To always write the request body to a file, client_body_in_file_only needs to be enabled. When the name of a temporary file is passed in a proxied request or in a request to a FastCGI/uwsgi/SCGI server, passing the request body should be disabled by the proxy_pass_request_body off, fastcgi_pass_request_body off, uwsgi_pass_request_body off, or scgi_pass_request_body off directives, respectively.

`$server_addr`:

    an address of the server which accepted a request
    Computing a value of this variable usually requires one system call. 
    To avoid a system call, the listen directives must specify addresses and use the bind parameter.

| **name**              | **desc**                                                                                         | **apach**             |
| --------------------- | ------------------------------------------------------------------------------------------------ | --------------------- |
| $arg_name             | argument name in the request line                                                                |                       |
| $args                 | arguments in the request line                                                                    |                       |
| $binary_remote_addr   | クライアントアドレス(バイナリ, 4=IPv4, 16=IPv6)                                                  |                       |
| $body_bytes_sent      | 送信バイト数(ヘッダー含まず)                                                                     | “%B”  (mod_log_confi) |
| $bytes_sent           | クライアントへの送信バイト数(1.3.8, 1.2.5)                                                       |                       |
| $connection           | connection serial number (1.3.8, 1.2.5)                                                          |                       |
| $connection_requests  | 現在のリクエスト数/接属 (1.3.8, 1.2.5)                                                           |                       |
| $content_length       | “Content-Length” リクエストヘッダー                                                              |                       |
| $content_type         | “Content-Type” リクエストヘッダー                                                                |                       |
| $cookie_ _name_       | クッキー名                                                                                       |                       |
| $document_root        | `root` あるいは `alias`ディレクティブ名                                                          |                       |
| $document_uri         | == `$uri`                                                                                        |                       |
| $host                 | 順に評価: 1) reqeust行のホスト名, 2) "Host" ヘッダー , 3) サーバー名                             |                       |
| $hostname             | ホスト名                                                                                         |                       |
| $http_ _name_         | 任意のリクエストヘッダー(英子文字で、'-' -> '_' に変換)                                          |                       |
| $https                | SSLであれば　“on” 、なければ空                                                                   |                       |
| $is_args              | request行に引数があれば　"?" なければ空                                                          |                       |
| $limit_rate           | 応答制限の設定値 (`limit_rate`を参照)                                                            |                       |
| $msec                 | 現在時刻秒のミリ単位 (1.3.9, 1.2.6)                                                              |                       |
| $nginx_version        | バージョン                                                                                       |                       |
| $pid                  | `PID`                                                                                            |                       |
| $pipe                 | "p": パイプラインされているリクエスト, ".": されていない (1.3.12, 1.2.7)                         |                       |
| $query_string         | == `args`                                                                                        |                       |
| $realpath_root        | `root`/`alias` に対応する 絶対 `pathname` ; シンボリックリンクはリアルパスにリゾルブされる       |                       |
| $remote_addr          | クライアントアドレス                                                                             |                       |
| $remote_port          | クライアントポート                                                                               |                       |
| $remote_user          | Basic認証でのユーザー                                                                            |                       |
| $request              | 全てのrequest行                                                                                  |                       |
| $request_body         | request ボディ                                                                                   |                       |
| $request_body_file    | request ボディの一時ファイル名                                                                   |                       |
| $request_completion   | “OK” :リクエスト完了   (以外は空白)                                                              |                       |
| $request_filename     | ファイルパス , `root` / `alias`を元にしたリクエストURIで決まる                                   |                       |
| $request_id           | 16バイトのランダムリクエストID(16進)(1.11.0)                                                     |                       |
| $request_length       | リクエスト長さ(リクエスト行, ヘッダー, ボディ)(1.3.12, 1.2.7)                                    |                       |
| $request_method       | メソッド (GET, POST)                                                                             |                       |
| $request_time         | 最初のバイトが読まれからのリクエスト処理秒 (msec )(1.3.9, 1.2.6)                                 |                       |
| $request_uri          | オリジナルリクエストURI(引数あり                                                                 |                       | ) |
| $scheme               | “http” / “https”                                                                                 |                       |
| $sent_http_ _name_    | _name_ で指定したヘッダーフィールド。(英子文字, '-' -> '_' 変換される)                           |                       |
| $sent_trailer_ _name_ | _name_ で指定した応答ヘッダーフィールド(1.13.2) (英子文字, '-' -> '_' 変換される)                |                       |
| $server_addr          | リクエストを受け付けたサーバーアドレス                                                           |                       |
| $server_name          | リクエストを受け付けたサーバー名                                                                 |                       |
| $server_port          | リクエストを受け付けたサーバーポート                                                             |                       |
| $server_protocol      | リクエストプロトコル (“HTTP/1.0”, “HTTP/1.1”, or “HTTP/2.0”)                                     |                       |
| $status               | 応答ステータス(1.3.2, 1.2.2)                                                                     |                       |
| $time_iso8601         | ISO8601 のローカル時間   (1.3.12, 1.2.7)                                                         |                       |
| $time_local           | Common Log Format (1.3.12, 1.2.7) のローカル時間                                                 |                       |
| $uri                  | 現在のURI.ノーマライズ済。 リクエスト処理で変更される(内部リダイレクトやindexファイルの処理など) |                       |



$tcpinfo_rtt, $tcpinfo_rttvar, $tcpinfo_snd_cwnd, $tcpinfo_rcv_space
information about the client TCP connection; available on systems that support the TCP_INFO socket option