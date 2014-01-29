Date: 2013-12-29 11:30
Title: php: Composerでライブラリプロジェクトを作成する
Type: post  
Excerpt:   


Composerが便利そうなので、これでライブラリの開発をしてみる。

とりあえず、[Stagehand](https://bitbucket.org/hdknr/stagehand) というのをつくってみた。

## Stagehand の開発 ##

* レポジトリをつくる。Bitubucketにgitで作った。

### ライブラリ ###

* lib/Stagehandをつくる
* lib/Stagehand/Greeting.php にクラスを作る

Greeting.php:

    <?php
    namespace Stagehand;
    
    class Greeting
    {
        protected

            $hello;
    
        function __construct( $hello='Hello')
        {
            $this->hello = $hello;
        } 
        public function sayHello()
        {
            return $this->hello; 
        }
    }

### テスト ###

* test をつくる
* test/bootstrap.php を作って、テストに必要なライブラリをautoloadさせる

bootstrap.php:

    <?php
    
    require_once __DIR__.'/../vendor/autoload.php';

   
* test/Stagehand/SimpleTest.php  をつくる。単純なテスト。

SimpleTest.php:

    <?php
    
    use Stagehand\Greeting;     // autoloadされているクラスの参照
    
    class SimpleTest extends PHPUnit_Framework_TestCase
    {
        public function testHello() {
            $msg="Konnichiwa";
            $greeting = new Greeting( $msg );
            $this->assertEquals($msg, $greeting->sayHello());
        }
    }
 

### composer のインストール ###

おやくそく:

    $ curl -s http://getcomposer.org/installer | php

### composer.json の作成とパッケージインストール ###

* lib の下にあるライブラリをオートロードさせるように psr-0 を定義すること

composer.json:

    {
        "require-dev": {
            "phpunit/phpunit": "3.7.*"
        },
        "autoload": {
            "psr-0": { "": "lib/" }
        }
    }

* インストール

bash:

    $ php composer.phar install


### phpunit.xml を作成してテスト ###

* test/Stagehand/ の *.php をテスト

phpunit.xml:

    <?xml version="1.0" encoding="UTF-8"?>
    
    <phpunit backupGlobals="false"
             backupStaticAttributes="false"
             colors="true"
             convertErrorsToExceptions="true"
             convertNoticesToExceptions="true"
             convertWarningsToExceptions="true"
             processIsolation="false"
             stopOnFailure="false"
             syntaxCheck="false"
             bootstrap="./test/bootstrap.php"
    >
        <testsuites>
            <testsuite name="Stagehand Tests">
                <directory>./test/Stagehand/</directory>
            </testsuite>
        </testsuites>
    
        <filter>
            <whitelist>
                <directory suffix=".php">./lib/</directory>
            </whitelist>
        </filter>
    </phpunit>
    

* 実行。ランナーは vender/phpunit/phpunit の下にcomposerでインストールされています。

bash:

    $ vendor/phpunit/phpunit/phpunit.php
    
    PHPUnit 3.7.28 by Sebastian Bergmann.
    
    Configuration read from /home/hdknr/php/stagehand/phpunit.xml
    
    Time: 32 ms, Memory: 2.50Mb
    
    OK (1 test, 1 assertion)

### composer.json にメタデータ追加 ###

* 他のプロジェクトでロードできるように

composer.json:

    {
        "name": "hdknr/stagehand",
        "description": "Sample sandbox php for Composer compliance",
        "keywords": ["Composer","sandbox" ],
        "type": "library",
        "license": "MIT",
        "authors": [
            {
                "name": "hideki nara",
                "email": "hdknr@ic-tact.co.jp"
            }
        ],
        "require-dev": {
            "phpunit/phpunit": "3.7.*"
        },
        "require": {
            "php": ">=5.4.0"
        },
        "autoload": {
            "psr-0": { "": "lib/" }
        }
    }
    
### レポジトリにコミット ###

* .gitignore , .gitattributes を適切に追加
* commit && push 


### サンプルプロジェクトでライブラリ動作確認 ###

* test/Main/SimpleTest.php を作成

SimpleTest.php:

    <?php
    
    use Stagehand\Greeting;
    
    class SimpleTest extends PHPUnit_Framework_TestCase
    {
        public function testHello() {
            $msg="ほげほげ";
            $greeting = new Greeting( $msg );
            $this->assertEquals($msg, $greeting->sayHello());
            echo( $msg );
        }
    }
    

* test/bootstrap.php を作成。内容はStagehandのものをコピペ。
* composer.jsonを作成。レポジトリにBitbucketを追加して、requireにパッケージ名と、タグを指定。

composer.json:

    {
        "repositories": [
            {
                "type": "vcs",
                "url": "https://bitbucket.org/hdknr/stagehand.git"
            }
        ],
        "require":{
            "hdknr/stagehand":"dev-master"
        },
        "require-dev": {
            "phpunit/phpunit": "3.7.*"
        }
    }

* composer自体のインストール。
* composerでパッケージインストール。

bash:

    $ php composer.phar install

    Loading composer repositories with package information
    Installing dependencies (including require-dev)       
      - Installing hdknr/stagehand (dev-master 04ebd96)
        Cloning 04ebd9671462662fbd004b8eb8071387ae31fbef
    
      - Installing symfony/yaml (v2.4.0)
        Loading from cache
    
      - Installing phpunit/php-text-template (1.1.4)
        Loading from cache
    
      - Installing phpunit/phpunit-mock-objects (1.2.3)
        Loading from cache
    
      - Installing phpunit/php-timer (1.0.5)
        Loading from cache
    
      - Installing phpunit/php-token-stream (1.2.1)
        Loading from cache
    
      - Installing phpunit/php-file-iterator (1.3.4)
        Loading from cache
    
      - Installing phpunit/php-code-coverage (1.2.13)
        Loading from cache
    
      - Installing phpunit/phpunit (3.7.28)
        Loading from cache
    
    phpunit/php-code-coverage suggests installing ext-xdebug (>=2.0.5)
    phpunit/phpunit suggests installing phpunit/php-invoker (>=1.1.0,<1.2.0)
    Writing lock file
    Generating autoload files

* phpunit.xml を作成。stagehandのものをコピって、test/Main/ にディレクトリを変更。
* テスト実行。
  
bash:
    
    $ vendor/phpunit/phpunit/phpunit.php 

    PHPUnit 3.7.28 by Sebastian Bergmann.
    
    Configuration read from /home/hdknr/php/sample/phpunit.xml
    
    .ほげほげ
    
    Time: 31 ms, Memory: 2.50Mb
    
    OK (1 test, 1 assertion)

