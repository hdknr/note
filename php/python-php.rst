========================
PHP: Compared To Python
========================


Compared to Python
=======================

.. list-table:: Quick Compare
    :widths: 10 45 45

    * - (item)
      - Python

        .. image:: python.jpeg

      - PHP

        .. image:: php.png

    * - Loop
      - for in

        .. code-block:: python
            
            a = [80, 100, 120]
            for i in a:
                print a 

      - foreach(){}

        .. code-block:: php

            $a = array(80, 100, 120);
            foreach($a as &$i){
                echo "{$i}¥n";
            };

    * - 型
      - type(obj) 
      - `get_class <http://php.net/manual/ja/function.get-class.php>`_ ($obj)
  

    * - デフォルト値設定

      - or

        .. code-block:: python

            name =  request.POST['name'] or 'NAME'


      - @ ?: 

        .. code-block:: php
            
            $name = @$_POST['name'] ?: 'NAME';
