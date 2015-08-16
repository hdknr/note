~~~bash
$ vendor/bin/wp plugin list
+--------------------+----------+--------+---------+
| name               | status   | update | version |
+--------------------+----------+--------+---------+
| akismet            | inactive | none   | 3.1.3   |
| hello              | inactive | none   | 1.6     |
| wp-multibyte-patch | inactive | none   | 2.3.1   |
+--------------------+----------+--------+---------+
~~~

~~~bash
$ vendor/bin/wp scaffold plugin wp-authmod
Success: Created /home/vagrant/projects/wphome/wordpress/wp-content/plugins/wp-authmod
Success: Created test files.

~~~

~~~bash
$ ln -s wordpress/wp-content/plugins/wp-authmod .
~~~

~~~bash
$ vendor/bin/wp plugin list
+--------------------+----------+--------+-----------+
| name               | status   | update | version   |
+--------------------+----------+--------+-----------+
| akismet            | inactive | none   | 3.1.3     |
| hello              | inactive | none   | 1.6       |
| wp-authmod         | inactive | none   | 0.1-alpha |
| wp-multibyte-patch | inactive | none   | 2.3.1     |
+--------------------+----------+--------+-----------+~~~

~~~bash
$ tree wp-authmod
wp-authmod
├── Gruntfile.js
├── bin
│   └── install-wp-tests.sh
├── package.json
├── phpunit.xml
├── readme.txt
├── tests
│   ├── bootstrap.php
│   └── test-sample.php
└── wp-authmod.php

~~~


## phpunit

~~~
$ ./composer.phar require phpunit/phpunit
$ ln -s $PWD/www/wordpress/wp-content/plugins/wp-authmod .
$ cd wp-authmod
~~~

~~~
$ bin/install-wp-tests.sh wpauth_test $DBROOT_USER $DBROOT_PASSWD
~~~
~~~
$ tree /tmp/wordpress-tests-lib/
/tmp/wordpress-tests-lib/
├── includes
│   ├── bootstrap.php
│   ├── exceptions.php
│   ├── factory.php
│   ├── functions.php
│   ├── install.php
│   ├── mock-fs.php
│   ├── mock-image-editor.php
│   ├── mock-mailer.php
│   ├── testcase-ajax.php
│   ├── testcase-canonical.php
│   ├── testcase-xmlrpc.php
│   ├── testcase.php
│   ├── trac.php
│   ├── utils.php
│   └── wp-profiler.php
└── wp-tests-config.php
~~~

~~~
$ /vagrant/projects/wpauth/vendor/bin/phpunit 
Installing...
Running as single site... To run multisite, use -c tests/phpunit/multisite.xml
Not running ajax tests. To execute these, use --group ajax.
Not running ms-files tests. To execute these, use --group ms-files.
Not running external-http tests. To execute these, use --group external-http.
PHPUnit 4.8.2 by Sebastian Bergmann and contributors.

.

Time: 4.3 seconds, Memory: 26.75Mb

OK (1 test, 1 assertion)
~~~


