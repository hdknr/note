- [Drupal Consoleを使った開発環境構築](http://qiita.com/ippey_s/items/371eb5ec2dfcdff9fade)


~~~bash
$ drupal site:new

 Select value for repository placeholder [drupal-composer/drupal-project:8.x-dev]:
  [0] drupal-composer/drupal-project:8.x-dev
  [1] acquia/lightning-project
  [2] acquia/reservoir-project
 > 0

 Enter value for directory placeholder:
 > web

 Enter value for directory placeholder:
> web


// exec

Executing command: composer create-project drupal-composer/drupal-project:8.x-dev web --prefer-dist --no-progress --no-interaction
Installing drupal-composer/drupal-project (8.x-dev 7c4120c7fb907efe06674a3cea4cc12d7fb588d3)
 - Installing drupal-composer/drupal-project (8.x-dev 7c4120c): Downloading (100%)
Created project in web
> DrupalProject\composer\ScriptHandler::checkComposerVersion
Loading composer repositories with package information
Updating dependencies (including require-dev)

 ~~~

## インストール

~~~bash
$ cd web/
~~~
