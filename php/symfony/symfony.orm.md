## sqlite

~~~bash
$ vi app/config/config.yml
~~~

~~~yaml

doctrine:
    dbal:
        driver: pdo_sqlite
        path: '%kernel.project_dir%/app/sqlite.db'
        charset: UTF8
~~~        


## データベース作成

~~~bash
$ php bin/console doctrine:database:create

Created database /vagrant/projects/samples/sym/web/app/sqlite.db for connection named default
~~~

## Product エンティティ

~~~bash
$ mkdir -p src/AppBundle/Entity
$ vi   src/AppBundle/Entity/Product.php
~~~

~~~php
<?php
// src/AppBundle/Entity/Product.php
namespace AppBundle\Entity;

use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Entity
 * @ORM\Table(name="product")
 */
class Product
{
    /**
     * @ORM\Column(type="integer")
     * @ORM\Id
     * @ORM\GeneratedValue(strategy="AUTO")
     */
    private $id;

    /**
     * @ORM\Column(type="string", length=100)
     */
    private $name;

    /**
     * @ORM\Column(type="decimal", scale=2)
     */
    private $price;

    /**
     * @ORM\Column(type="text")
     */
    private $description;
}

~~~

## データベース反映

~~~bash
$ php bin/console doctrine:schema:update --force

Updating database schema...
Database schema updated successfully! "1" query was executed
~~~

~~~bash
$ sqlite3 app/sqlite.db

SQLite version 3.16.2 2017-01-06 16:32:41
Enter ".help" for usage hints.
sqlite> .tables
product
sqlite> .schema product
CREATE TABLE product (id INTEGER NOT NULL, name VARCHAR(100) NOT NULL, price NUMERIC(10, 2) NOT NULL, description CLOB NOT NULL, PRIMARY KEY(id));
~~~

- エンティティクラスにフィールド追加したり削除したあとで、`doctrine:schema:update --force` するとデータベースに反映される
