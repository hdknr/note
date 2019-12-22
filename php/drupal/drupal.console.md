- [How to install Drupal Console](https://drupalconsole.com/articles/how-to-install-drupal-console)

~~~bash
$ mkdir bin
$ curl https://drupalconsole.com/installer -L -o bin/drupal.phar
$ php --version
PHP 7.0.6 (cli) (built: Aug  4 2017 12:18:10) ( NTS )
Copyright (c) 1997-2016 The PHP Group
Zend Engine v3.0.0, Copyright (c) 1998-2016 Zend Technologies
    with Zend OPcache v7.0.6-dev, Copyright (c) 1999-2016, by Zend Technologies
    with Xdebug v2.5.5, Copyright (c) 2002-2017, by Derick Rethans
~~~    

~~~bash
$ php bin/drupal.phar

Drupal Console Launcher (1.0.1)
===============================

Copy configuration files.
  drupal init

Download, install and serve Drupal 8
  drupal quick:start

Create a new Drupal project
  drupal site:new

Install a Drupal project
  drupal site:install

Lists all available commands
  drupal list

Update project to the latest version.
   drupal self-update

$ alias drupal=$PWD/bin/drupal.phar   
$ chmod +x bin/drupal.phar
~~~

~~~bash

$ drupal init

 Select destination to copy configuration:                                 
  [0] /etc/console/                                                         
  [1] /home/vagrant/.console/              
 > 1                                          

 Select language [en]:                                      
 > ja                                         

 Enter temporary file path [/tmp]:
 >                                                                 

 Copy chain files examples (yes/no) [no]:
 > yes

 Copy site alias files examples (yes/no) [no]:                
 > yes

 Shows information for learning purposes? (yes/no) [no]:
 > yes

 Show inline representation of the executed command? (yes/no) [no]:
 > yes

 Show chain representation of the executed command? (yes/no) [no]:
 > yes

 Generate autocomplete files (yes/no) [no]:
 > yes

 Copied files

  1 - /home/vagrant/.console/aliases.yml
  2 - /home/vagrant/.console/chain/develop-contribute.yml
  3 - /home/vagrant/.console/chain/create-data.yml
  4 - /home/vagrant/.console/chain/form-sample.yml
  5 - /home/vagrant/.console/chain/sample.yml
  6 - /home/vagrant/.console/chain/site-install-placeholers-env.yml
  7 - /home/vagrant/.console/chain/site-install-placeholers.yml
  8 - /home/vagrant/.console/chain/site-install.yml
  9 - /home/vagrant/.console/chain/site-update.yml
  10 - /home/vagrant/.console/chain/update-command-data.yml
  11 - /home/vagrant/.console/chain/update-gitbook.yml
  12 - /home/vagrant/.console/chain/quick-start.yml
  13 - /home/vagrant/.console/chain/site-new.yml
  14 - /home/vagrant/.console/phpcheck.yml
  15 - /home/vagrant/.console/router.php
  16 - /home/vagrant/.console/site.mode.yml
  17 - /home/vagrant/.console/sites/drupalvm.yml
  18 - /home/vagrant/.console/sites/sample.yml

 Bash: Bash support depends on the http://bash-completion.alioth.debian.org/
 project which can be installed with your package manager of choice. Then add
 this line to your shell configuration file.
 source "$HOME/.console/console.rc" 2>/dev/null

 Bash or Zsh: Add this line to your shell configuration file:
 source "$HOME/.console/console.rc" 2>/dev/null

 Fish: Create a symbolic link
 ln -s ~/.console/drupal.fish ~/.config/fish/completions/drupal.fish

 Generated or updated files

  1 - /home/vagrant/.console/config.yml
  ~~~

  ~~~bash
  $ drupal self-update
 Checking for updates from version: "1.0.1"
 The latest version "1.0.1", was already installed on your system.
 ~~~
