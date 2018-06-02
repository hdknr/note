CAUTION: 古い情報 . [wp-cli.phar で入れた方がよい](wordpress.wp-cli.md)

Wordpress: Composerでインストールしてみる

- [Using Composer with WordPress](http://roots.io/using-composer-with-wordpress/)


## composerを入れる

```
vagrant@10:~/projects/wordpress$ curl -s http://getcomposer.org/installer | php 

#!/usr/bin/env php
All settings correct for using Composer
Downloading...

Composer successfully installed to: /home/vagrant/projects/wordpress/composer.phar
Use it: php composer.phar
```

## composer.json

```
{
  "repositories": [
    {
      "type": "composer",
      "url": "http://wpackagist.org"
    },
    {
      "type": "package",
      "package": {
        "name": "wordpress",
        "type": "webroot",
        "version": "4.1",
        "dist": {
          "type": "zip",
          "url": "https://github.com/WordPress/WordPress/archive/4.1.zip"
        },
        "require": {
          "fancyguy/webroot-installer": "1.0.0"
        }
      }
    }
  ],
  "require": {
    "php": ">=5.3.0",
    "wordpress": "4.1",
    "fancyguy/webroot-installer": "1.0.0",
    "fancyguy/wordpress-monolog": "dev-master",
    "wpackagist/advanced-custom-fields": "*",
    "wpackagist/posts-to-posts": "1.4.x"
  },
  "extra": {
    "webroot-dir": "wp",
    "webroot-package": "wordpress"
  }
}
```

## webroot-installer

```
This is for PHP packages that support composer to configure in their composer.json. 
It will allow a root package to define a webroot directory and webroot package and magically install it in the correct location.
```

- webroot-dirに wpを指定したので、 プロジェクトルートに wpが作成される
- wpディレクトリに落とすのは wordpressパッケージ


### インストール

```
vagrant@10:~/projects/wordpress$ ./composer.phar update
Loading composer repositories with package information
Updating dependencies (including require-dev)
  - Installing fancyguy/webroot-installer (1.0.0)
    Downloading: 100%         

  - Installing composer/installers (v1.0.19)
    Downloading: 100%         

  - Installing wordpress (4.1)
    Downloading: 100%         

  - Installing psr/log (1.0.0)
    Downloading: 100%         

  - Installing monolog/monolog (1.11.0)
    Downloading: 100%         

  - Installing fancyguy/wordpress-monolog (dev-master 802cef4)
    Cloning 802cef4feaee61f513d621fe9516af17f8e067b7

The authenticity of host 'github.com (192.30.252.129)' can't be established.
RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
Are you sure you want to continue connecting (yes/no)? yes
Cloning failed using an ssh key for authentication, enter your GitHub credentials to access private repos
The credentials will be swapped for an OAuth token stored in /home/vagrant/.composer/auth.json, your password will not be stored
To revoke access to this token you can visit https://github.com/settings/applications
Username: hdknr
Password: 
Token successfully created

monolog/monolog suggests installing graylog2/gelf-php (Allow sending log messages to a GrayLog2 server)
monolog/monolog suggests installing raven/raven (Allow sending log messages to a Sentry server)
monolog/monolog suggests installing doctrine/couchdb (Allow sending log messages to a CouchDB server)
monolog/monolog suggests installing ruflin/elastica (Allow sending log messages to an Elastic Search server)
monolog/monolog suggests installing videlalvaro/php-amqplib (Allow sending log messages to an AMQP server using php-amqplib)
monolog/monolog suggests installing ext-amqp (Allow sending log messages to an AMQP server (1.0+ required))
monolog/monolog suggests installing ext-mongo (Allow sending log messages to a MongoDB server)
monolog/monolog suggests installing aws/aws-sdk-php (Allow sending log messages to AWS services like DynamoDB)
monolog/monolog suggests installing rollbar/rollbar (Allow sending log messages to Rollbar)
Writing lock file
Generating autoload files
```

### インストール後

- 通常の composerパッケージ

```
vagrant@10:~/projects/wordpress$ ls vendor/
autoload.php  composer  fancyguy  monolog  psr
```

- wp, wp-content が別途プロジエクトルートにできています

- wpはwordpress 本体

- wp-contentはプラグイン

```
vagrant@10:~/projects/wordpress$ tree wp-content/
wp-content/
└── plugins
    └── fancyguy-monolog
        ├── composer.json
        ├── FancyGuy
        │   └── WordPress
        │       └── Plugin
        │           └── Monolog
        │               └── Logger.php
        └── README.md

6 directories, 3 files

```

## WordPress Packagist

- Wordpress Package を composerでインストールできる

