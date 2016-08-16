
- https://github.com/xdan/datetimepicker
- http://xdsoft.net/jqplugins/datetimepicker/


## Django

- settings.py / [bower](../bower.md)

~~~py
BOWER_INSTALLED_APPS = [                                                         
  ...
  'datetimepicker',       # https://github.com/xdan/datetimepicker             
  ...
]
~~~
~~~bash
$ python manage.py bower install
$ python manage.py collectstatic
~~~

- テンプレート

~~~html
{% block head_style%}{{ block.super}}
<link href="{% static 'datetimepicker/jquery.datetimepicker.css' %}" rel="stylesheet">
{% endblock %}
....


{% block bottom_script %} {{ block.super }}
<script src="{% static 'datetimepicker/build/jquery.datetimepicker.full.js' %}"></script>
<script type="text/javascript">
  $(function() {
    $.datetimepicker.setLocale('ja');
    $("input#id_opening_on, input#id_closing_on").datetimepicker({
      lang: 'ja',
      format: 'Y-m-d H:i',
      defaultTime: '10:00',
      timepickerScrollbar: false
    });
  });
</script>
{% endblock %}
~~~
