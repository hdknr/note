# Wordpress docker

- [Docker+WP-CLI で WordPress の開発環境構築をラクにする](https://satoshimurata.com/docker-wp-cli-wordpress)

```dockerfile
FROM wordpress:latest

RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar \
  && chmod +x wp-cli.phar \
  && mv wp-cli.phar /usr/local/bin/wp \
  && wp --info
```
