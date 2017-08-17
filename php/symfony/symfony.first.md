最初のページ


- [Create your First Page in Symfony](https://symfony.com/doc/current/page_creation.html)

最初にやること:
- 1. ルートを作る(`/lucky/number`)
- 2. コントローラを作る


## コントローラ + ルート

~~~bash
$ tree src/AppBundle/
src/AppBundle/
├── AppBundle.php
└── Controller
    └── DefaultController.php

1 directory, 2 files
~~~

~~~bash
$ vim src/AppBundle/Controller/LuckyController.php
~~~

~~~php
<?php
// src/AppBundle/Controller/LuckyController.php
namespace AppBundle\Controller;

use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
use Symfony\Component\HttpFoundation\Response;

class LuckyController
{
    // ルートの定義
    /**
     * @Route("/lucky/number")
     */
    public function numberAction()      // コントローラ
    {
        $number = mt_rand(0, 100);

        return new Response(
            '<html><body>Lucky number: '.$number.'</body></html>'
        );
    }
}
~~~


## テンプレート

~~~bash
$ tree app/Resources/
app/Resources/
└── views
    ├── base.html.twig
    └── default
        └── index.html.twig

2 directories, 2 files
~~~

~~~bash
$ mkdir -p app/Resources/views/lucky
$ vi app/Resources/views/lucky/number.html.twig
~~~

~~~html
{# app/Resources/views/lucky/number.html.twig #}

<h1>Your lucky number is {{ number }}</h1>

~~~

コントローラ修正:

~~~php
<?php
// src/AppBundle/Controller/LuckyController.php
namespace AppBundle\Controller;

use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
use Symfony\Bundle\FrameworkBundle\Controller\Controller;     // Controllerクラスの利用


class LuckyController extends Controller                      // Controllerをサブクラス
{
    // ルート
    /**
     * @Route("/lucky/number")
     */
    public function numberAction()      // コントローラ
    {
        $number = mt_rand(0, 100);

        return $this->render('lucky/number.html.twig', array(
            'number' => $number,
        ));
    }
}

~~~
