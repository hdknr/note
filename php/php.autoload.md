autoload


- [Autoloading in PHP and the PSR-0 Standard](http://www.sitepoint.com/autoloading-and-the-psr-0-standard/)

## PSR-0

- `FQN`: A fully-qualified namespace and class must have the following structure `<Vendor Name>(<Namespace>)*<Class Name>`.
- `Vendor Name`: Each namespace must have a top-level namespace (“`Vendor Name`”).
- `Sub Namespaces`: Each namespace can have as many sub-namespaces as it wishes.
- `Separator`: Each namespace separator is converted to a `DIRECTORY_SEPARATOR` when loading from the file system.
- `Underscore`: Each underscore in the class name is converted to a `DIRECTORY_SEPARATOR`. The underscore has no special meaning in the namespace.
- `.php`: The fully-qualified namespace and class is suffixed with `.php` when loading from the file system.
- `Case Sensitive`: Alphabetic characters in vendor names, namespaces, and class names may be of any combination of lower case and upper case.


## catsample.php

- 構成

~~~bash
$ tree .
.
├── Lafoglia
│   └── Tools
│       └── Cat.php
├── autoload.php
└── catsample.php

2 directories, 3 files
~~~

- Catクラス。

~~~php
$ cat Lafoglia/Tools/Cat.php 

<?php
namespace Lafoglia\Tools;

class Cat
{
    public function mew(){
        return "Mew Mew Mnew"; 
    }
}
~~~

- オートローダ

~~~php

$ cat autoload.php 
<?php
/* Based on http://qiita.com/misogi@github/items/8d02f2eac9a91b4e6215
 *
 */
class ClassLoader
{
    public static function loadClass($class)
    {
        foreach (self::directories() as $directory) {
            $file_name = str_replace(
                "\\", "/", 
                $directory.DIRECTORY_SEPARATOR.$class.".php");

            if (is_file($file_name)) {
                require $file_name;
                return true;
            }
        }
    }

    private static $dirs;

    private static function directories()
    {
        if (empty(self::$dirs)) {
            $base = '.';
            self::$dirs = array(
                $base,
                $base . '/controllers',
                $base . '/models'
            );
        }

        return self::$dirs;
    }
}

spl_autoload_register(array('ClassLoader', 'loadClass'));
~~~

- サンプル

~~~php
$ cat catsample.php 

<?php
require_once "autoload.php";

use Lafoglia\Tools\Cat;

$cat = new Cat;
echo $cat->mew(), "\n";
~~~

- 実行

~~~php

$ php catsample.php 
Mew Mew Mnew
~~~

## composer : vendor/autoload.php
- composer を入れて、 composerの規約でモジュールおけばよい

~~~php
$ more vendor/autoload.php 
<?php

// autoload.php @generated by Composer

require_once __DIR__ . '/composer' . '/autoload_real.php';

return ComposerAutoloaderInit7800aec593606dc0ecedc58da7190635::getLoader();
~~~

- getLoader() の処理 vendor/composer/autoload_real.php

~~~php
<?php

// autoload_real.php @generated by Composer

class ComposerAutoloaderInit7800aec593606dc0ecedc58da7190635
{
    private static $loader;

    public static function loadClassLoader($class)
    {
        if ('Composer\Autoload\ClassLoader' === $class) {
            require __DIR__ . '/ClassLoader.php';
        }
    }

    public static function getLoader()
    {
        if (null !== self::$loader) {
            return self::$loader;
        }

        spl_autoload_register(
        	array('ComposerAutoloaderInit7800aec593606dc0ecedc58da7190635', 
        		  'loadClassLoader'), true, true);
		.....        		  
		/* 以下のモジュール読んでオートロードの処理をする
		vendor/composer/autoload_namespaces.php
		vendor/composer/autoload_psr4.php
		vendor/composer/autoload_classmap.php
		vendor/composer/autoload_files.php
		*/
		...
		return $loader;
	}
}
	
function composerRequire7800aec593606dc0ecedc58da7190635($file)
{
    require $file;
}	
~~~

### psysh

~~~
$ vendor/bin/psysh
Psy Shell v0.6.0-dev (PHP 5.6.10 — cli) by Justin Hileman
>>>
~~~

- composer.json,もしくはcomposer.lock のディクレトリから遡って autoload.php を探し、最終的に composerの autoload.php を見つけてロード 

~~~php
    $cwd = str_replace('\\', '/', $cwd);

    $chunks = explode('/', $cwd);
    while (!empty($chunks)) {
        $path = implode('/', $chunks);

        // Find composer.json
        if (is_file($path . '/composer.json')) {
            if ($cfg = json_decode(file_get_contents($path . '/composer.json'), true)) {
                if (isset($cfg['name']) && $cfg['name'] === 'psy/psysh') {
                    // We're inside the psysh project. Let's use the local
                    // Composer autoload.
                    if (is_file($path . '/vendor/autoload.php')) {
                        require $path . '/vendor/autoload.php';
                    }   

                    return;
                }
            }
        }

        // Or a composer.lock
        if (is_file($path . '/composer.lock')) {
            if ($cfg = json_decode(file_get_contents($path . '/composer.lock'), true)) {
                foreach (array_merge($cfg['packages'], $cfg['packages-dev']) as $pkg) {
                    if (isset($pkg['name']) && $pkg['name'] === 'psy/psysh') {
                        // We're inside a project which requires psysh. We'll
                        // use the local Composer autoload.
                        if (is_file($path . '/vendor/autoload.php')) {
                            require $path . '/vendor/autoload.php';
                        }

                        return;
                    }
                }
            }
        }

        array_pop($chunks);
    }

~~~