## passedArgs

- [Passed Arguments](http://book.cakephp.org/2.0/en/development/routing.html#passed-arguments)
- URLに埋め込まれたパラメータがわたります。

- ビュー

~~~
<?php echo $this->SummaryForm->create(
	'Summary', 
    array('url' => array_merge(array('action' => 'aggregate'), 
	                            $this->params['pass']))); ?>
~~~                                                                   

- コントローラ

~~~
    function aggregate() {
        $this->dbg("aggreate():passedArgs:", $this->passedArgs);
        
        $a = @$this->passedArgs['a']?: 1;
        $b = @$this->passedArgs['b']?: 2;
        
        $this->params['pass'] = array('a' => $a +1 , 'b' => $b + 1 );
    }

~~~

- GET /summaries/aggregate/

~~~
2015-03-05 12:30:11 Debug: aggreate():passedArgs:
2015-03-05 12:30:11 Debug: []
2015-03-05 12:30:11 Debug: ...
~~~

~~~
<form action="/summaries/aggregate/a:2/b:3" 
	id="SummaryForm" 
	novalidate="novalidate" 
	method="post" 
	accept-charset="utf-8">
~~~

- POST /summaries/aggregate/a:2/b:3

~~~
2015-03-05 12:36:50 Debug: aggreate():passedArgs:
2015-03-05 12:36:50 Debug: {
    "a": "2",
    "b": "3"
}
2015-03-05 12:36:50 Debug: ...
~~~

~~~
<form action="/summaries/aggregate/a:3/b:4" 
	id="SummaryForm" 
	novalidate="novalidate" 
	method="post" 
	accept-charset="utf-8">
~~~


### Python の正規表現で

~~~
>>> dict(re.findall('([^:/]+)(?::([^/]+))?', '/k1:v1/k2:v2/k3/'))

{'k3': '', 'k2': 'v2', 'k1': 'v1'}
~~~

