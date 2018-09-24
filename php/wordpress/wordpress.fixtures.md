# テストFixture

- https://github.com/nlemoine/wp-cli-fixtures

## PHP.INI

- [Common Issues – WP-CLI — WordPress](https://make.wordpress.org/cli/handbook/common-issues/#php-fatal-error-allowed-memory-size-of-999999-bytes-exhausted-tried-to-allocate-99-bytes)

~~~bash
$ vi $(phpenv prefix)/etc/php.ini
~~~

~~~ini
memory_limit = 512M
~~~

## インストール

~~~bash 
$ bin/wp-cli.phar package install git@github.com:nlemoine/wp-cli-fixtures.git --path=wordpress                                                  
Warning: Package name mismatch...Updating from git name 'nlemoine/wp-cli-fixtures' to composer.json name 'hellonico/wp-cli-fixtures'.                                                                
Installing package hellonico/wp-cli-fixtures (dev-master)                                                                                                                                            
Updating /home/vagrant/.wp-cli/packages/composer.json to require the package...                                                                                                                      
Registering git@github.com:nlemoine/wp-cli-fixtures.git as a VCS repository...
Using Composer to install the package...
---
Loading composer repositories with package information
Updating dependencies
Resolving dependencies through SAT
Looking at all rules.
Something's changed, looking at all rules again (pass #1)

Dependency resolution completed in 0.925 seconds
...
Writing lock file
Generating autoload files
---
Success: Package installed.
~~~

~~~bash
$ curl  https://raw.githubusercontent.com/nlemoine/wp-cli-fixtures/master/examples/fixtures.yml > bin/fixtures.yml
~~~

~~~bash
$ bin/wp-cli.phar fixtures load --file=bin/fixtures.yml --path=wordpress
Loading fixtures... This might take some time depending on images number and connection speed
Saving fixtures...  100% [==============================================================================================================================================================] 0:36 / 0:35
Success: 10 users have been successfully created
Success: 15 attachments have been successfully created
Success: 50 terms have been successfully created
Success: 100 posts have been successfully created
Success: 10 pages have been successfully created
Success: 15 products have been successfully created
Success: 50 comments have been successfully created
~~~

~~~bash
$ bin/wp-cli.phar server --host=0.0.0.0 --docroot=wordpress
PHP 7.2.10 Development Server started at Mon Sep 24 14:11:59 2018
Listening on http://0.0.0.0:8080
Document root is /vagrant/projects/shaper-ubuntu/wordpress
Press Ctrl-C to quit.
~~~

確認:

~~~bash
$ curl -s http://192.168.56.54:8080/wp-json/wp/v2/posts/ | jq '.[] | "\(.id) , \(.title.rendered)"' -r

1 , Hello world!
35 , Ratione distinctio repellendus ut id ut.
80 , Enim neque voluptas qui qui.
75 , Non ipsum illo voluptas cupiditate amet nihil eum.
73 , Aspernatur nostrum illum vero.
105 , Ipsam consequatur incidunt quia in asperiores.
49 , Aut aut nihil impedit eum ea quae et.
93 , Est fuga est excepturi excepturi est.
47 , Aliquam repellat tempora modi aut molestiae est quisquam.
53 , Quis est facilis sit magni.
~~~