# sh

- [https://github.com/amoffat/sh](https://github.com/amoffat/sh)
- [https://amoffat.github.io/sh/](https://amoffat.github.io/sh/)

## install

```
$ pip install sh
Collecting sh
  Downloading sh-1.09.tar.gz
    /home/vagrant/.pyenv/versions/wordpress/lib/python2.7/site-packages/setuptools-8.3-py2.7.egg/setuptools/dist.py:284: UserWarning: The version specified requires normalization, consider using '1.9' instead of '1.09'.
Installing collected packages: sh
  Running setup.py install for sh
    /home/vagrant/.pyenv/versions/wordpress/lib/python2.7/site-packages/setuptools-8.3-py2.7.egg/setuptools/dist.py:284: UserWarning: The version specified requires normalization, consider using '1.9' instead of '1.09'.
Successfully installed sh-1.9
```

## ためす

### uptime

```
>>> from sh import uptime
>>> uptime()
 12:24:33 up 22:10,  1 user,  load average: 0.01, 0.02, 0.05

>>> res = _
>>> type(res)
<class 'sh.RunningCommand'>
>>> res
 12:24:33 up 22:10,  1 user,  load average: 0.01, 0.02, 0.05
```

```
>>> res.cmd
['/usr/bin/uptime']
>>> res.pid
25549
>>> res.exit_code
0
```
