## ページごとに CSSを切り替える

- app/views/layouts/default.ctp 

~~~
<head>
echo $scripts_for_layout;
</head>
~~~

- app/webroot/css/aggregate.css
- inline == false にしないと、headに入らないず、記載した場所に挿入されます(inline)

~~~
echo $html->script('your_page', array('inline' => false));
echo $html->css('your_page', null, array('inline' => false));
~~~

## default: フォームのデフォルト値

~~~
<td>
<?php echo $this->Form->input(
	"age_based_at", 
	 array('class' => 'help', 
           'div' => false, 
           'title'=> 'YYYY-MM-DD', 		// placeholder
           'default' => date('Y-m-d'),
           'label' => __('Age Based At', true))); ?>
</td>
~~~     