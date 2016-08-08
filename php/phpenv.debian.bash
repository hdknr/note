#!/bin/bash
PHPVER=5.6.17

PKG=(
libcurl4-openssl-dev
libjpeg-dev
libmcrypt-dev
libmysqlclient-dev
libpng12-dev
libreadline-dev
libssl-dev
libtidy-dev
libxslt1-dev
)
WORDPRESS=$(cat << EOF
[wordpress]
listen = var/run/php-fpm/php-fpm.sock
listen.allowed_clients = 127.0.0.1
listen.owner = www-data
listen.group = www-data
listen.mode = 0660

user = {{USER}}
group ={{USER}} 

pm = dynamic
pm.max_children = 50
pm.start_servers = 5
pm.min_spare_servers = 5
pm.max_spare_servers = 35
EOF
)

VERSIONS=($(phpenv versions --bare))

if [[ ${VERSIONS[*]} =~ $PHPVER ]]; then
    echo "$PHPVER already installed.";
    phpenv local $PHPVER;
else 
    for e in ${PKG[@]}; do sudo apt-get install $e -y; done
    CONFIGURE_OPTS="--with-libdir=lib/x86_64-linux-gnu" phpenv install $PHPVER
fi

CONF="$(phpenv prefix)/etc/conf.d/wordpress.conf"
# https://github.com/andreasjansson/envtpl
if [ ! -f $CONF ]; then
    echo "creating.... $CONF";
    echo "$WORDPRESS" | envtpl -o $CONF
fi
echo "edit $CONF to make wordpress to work"

mkdir -p $(phpenv prefix)/var/run/php-fpm

echo "edit $(phpenv prefix)/etc/php.ini to work MySQL with unix socket"
echo "mysqli.default_socket =  /var/run/mysqld/mysqld.sock"
