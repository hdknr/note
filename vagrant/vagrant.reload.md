# reload

- https://www.vagrantup.com/docs/cli/reload.html

~~~bash
vagrant global-status | grep js2
~~~

~~~bash
397d693  default virtualbox saved    /Users/hide/Documents/Boxes/js2
~~~

~~~bash
vagrant reload 397d693
~~~

~~~bash
vagrant global-status | grep js2
~~~

~~~bash
397d693  default virtualbox running  /Users/hide/Documents/Boxes/js2
~~~