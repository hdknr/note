# デバッグ

- 実際は symfony のデバッグ


## logger

~~~php
class FieldController extends CommonFormController
{
    public function newAction()
    {
        ...
        $logger = $this->get('logger');

        $trace = debug_backtrace(); 
        $file = $trace[0]['file'];
        $logger->error($file);

        if(!$this->request->isXmlHttpRequest()){
            $logger->error('not XmlHttpRequst');
        }

        if(!$fieldType){
            $query = var_export($_GET, true);
            $logger->error('no field type');
            $logger->error($query);
        }
        ...
~~~

### app/logs

~~~bash 
$ tree app/logs/
app/logs/
├── mautic_prod-2018-07-22.php
├── mautic_prod-2018-08-09.php
└── prod-2018-08-10.php

0 directories, 3 files
~~~~