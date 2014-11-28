====
PHP
====

.. image:: php.png

Compared to Python
=======================

.. list-table:: Quick Compare

    * - (item)
      - Python
      - PHP

    * - Loop
      - for in

        .. code-block:: python
            
            a = [80, 100, 120]
            for i in a:
                print a 

      - foreach(){}

        .. code-block:: PHP

            $a = array(80, 100, 120);
            foreach($a as &$i){
                echo "{$i}¥n";
            };

    * - 型
      - type(obj) 
      - `get_class <http://php.net/manual/ja/function.get-class.php>`_ ($obj)
  
