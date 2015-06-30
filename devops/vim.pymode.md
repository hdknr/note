## [Pymode]: error: Pymode requires vim compiled with +python. Most of features will be disabled.

~~~
[Pymode]: error: Pymode requires vim compiled with +python. Most of features will be disabled.
Error detected while processing /home/vagrant/.vim/bundle/python-mode/autoload/pymode/virtualenv.vim:
line    3:
E121: Undefined variable: from
E15: Invalid expression: from pymode.virtualenv import enable_virtualenv
Error detected while processing /home/vagrant/.vim/bundle/python-mode/ftplugin/python/pymode.vim:
line   12:
E121: Undefined variable: from
E15: Invalid expression: from pymode.utils import patch_paths
Press ENTER or type command to continue
~~~

~~~
(tracs)vagrant@10:~/projects/tracs$ vim --version | grep python

+cryptv          +linebreak       -python          +viminfo
+cscope          +lispindent      -python3         +vreplace
~~~

~~~
(tracs)vagrant@10:~/projects/tracs$ sudo apt-get install vim-nox
~~~