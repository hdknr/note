# /prで動かす

### staging をクローン

- プロジェクトルート: `/vagrant/projects/taberu/landing`
- `pr` にクローンする

~~~bash 
$ git clone https://github.com/mautic/mautic.git pr
~~~

### nginx: 設定ファイル

ファイル一覧:

~~~bash
$ tree /etc/nginx/sites-available/landing
/etc/nginx/sites-available/landing
├── location.conf
├── phpfpm.conf
└── upstream.conf
~~~

### phpfpm

- phhpenv のPHPを想定

~~~ini
[www]
;- User
user = vagrant
group = vagrant

;- Owner, Group
listen.owner = vagrant
listen.group = vagrant

listen = var/run/landing_phpfpm.sock
listen.allowed_clients = 127.0.0.1
listen.mode = 0666

pm = dynamic
pm.max_children = 5
pm.start_servers = 2
pm.min_spare_servers = 1
pm.max_spare_servers = 3
~~~

7.0.30:

~~~bash 
$ phpenv prefix
/home/vagrant/.anyenv/envs/phpenv/versions/7.0.30
~~~

起動:

~~~bash
$ $(phpenv prefix)/sbin/php-fpm --nodaemonize -y etc/nginx/sites-available/landing/phpfpm.conf
~~~

起動した:

~~~bash
$ ls $(phpenv prefix)/var/run
landing_phpfpm.sock
~~~

このファイルと nginx mautic アップストリームの定義を合わせる:

/etc/nginx/sites-available/landing/upstream.conf:

~~~conf
upstream landing_upstream {
  server unix:/home/vagrant/.anyenv/envs/phpenv/versions/7.0.30/var/run/landing_phpfpm.sock;
}
~~~

### nginxサーバー設定に組み込む

/etc/nginx/site-enabled/default:

~~~conf
# Mauticアップストリーム
include sites-available/landing/upstream.conf;

server {
    listen 8000;
    server_name localhost;
    ....
    # Mauticロケーション
    include sites-available/landing/location.conf;
    ....
~~~

### matic ロケーション(`/pr`)

/etc/nginx/sites-available/landing/location.conf:

~~~conf
location /pr {

  # プロジェクトルート
  root /vagrant/projects/taberu/landing;

  try_files $uri $uri/ /pr/index.php$is_args$query_string;
  # $query_string と $args は同じ

  index index.php;

  location ~ \.php$ {
    fastcgi_pass    landing_upstream;
    fastcgi_index   index.php;

    fastcgi_split_path_info     ^(.+\.php)(/.+)$;
    fastcgi_param   SCRIPT_FILENAME $document_root$fastcgi_script_name;
    fastcgi_param   PATH_INFO $fastcgi_script_name;
    fastcgi_param   HTTP_PROXY "";
    fastcgi_param   HTTP_X_REQUESTED_WITH $http_x_requested_with;
    include         fastcgi_params;
  }
}
~~~


## 記事

- [nginx で使える環境変数一覧[抜粋]](https://qiita.com/FoxBoxsnet/items/21316143c0f7929fc068)