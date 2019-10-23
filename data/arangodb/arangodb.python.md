# Python

## pyarango

- [Tutorial: ArangoDB with Python](https://www.arangodb.com/tutorials/tutorial-python/)

~~~bash
$ pip install pyarango --user

Collecting pyarango
  Downloading https://files.pythonhosted.org/packages/55/5a/f32d2d2a889024f082a9aa22cb2197247c333f10c75a2d3d8f040ae9109a/pyArango-1.3.2.tar.gz
Requirement already satisfied: requests>=2.7.0 in /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-2019.03/lib/python3.7/site-packages (from pyarango) (2.22.0)
Requirement already satisfied: future in /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-2019.03/lib/python3.7/site-packages (from pyarango) (0.17.1)
Collecting datetime (from pyarango)
  Downloading https://files.pythonhosted.org/packages/73/22/a5297f3a1f92468cc737f8ce7ba6e5f245fcfafeae810ba37bd1039ea01c/DateTime-4.3-py2.py3-none-any.whl (60kB)
     |████████████████████████████████| 61kB 1.2MB/s 
Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-2019.03/lib/python3.7/site-packages (from requests>=2.7.0->pyarango) (1.24.1)
Requirement already satisfied: idna<2.9,>=2.5 in /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-2019.03/lib/python3.7/site-packages (from requests>=2.7.0->pyarango) (2.8)
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-2019.03/lib/python3.7/site-packages (from requests>=2.7.0->pyarango) (3.0.4)
Requirement already satisfied: certifi>=2017.4.17 in /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-2019.03/lib/python3.7/site-packages (from requests>=2.7.0->pyarango) (2019.3.9)
Requirement already satisfied: pytz in /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-2019.03/lib/python3.7/site-packages (from datetime->pyarango) (2018.9)
Collecting zope.interface (from datetime->pyarango)
  Downloading https://files.pythonhosted.org/packages/d9/3a/101934e0f2026f0a58698978bfedec6e2021b28b846d9e1d9b54369e044d/zope.interface-4.6.0-cp37-cp37m-macosx_10_14_x86_64.whl (131kB)
     |████████████████████████████████| 133kB 500kB/s 
Requirement already satisfied: setuptools in /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-2019.03/lib/python3.7/site-packages (from zope.interface->datetime->pyarango) (40.8.0)
Building wheels for collected packages: pyarango
  Building wheel for pyarango (setup.py) ... done
  Created wheel for pyarango: filename=pyArango-1.3.2-cp37-none-any.whl size=38812 sha256=7653c25141152d09fb5ad3bc9afc6055ee1e7bc2a01b7eec3fa8a96ee553621b
  Stored in directory: /Users/hide/Library/Caches/pip/wheels/aa/7a/61/ae5691d437947fd1127c199be46f1315cf9447d05b1a3e1dc8
Successfully built pyarango

Installing collected packages: zope.interface, datetime, pyarango
  WARNING: The script sample is installed in '/Users/hide/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

Successfully installed datetime-4.3 pyarango-1.3.2 zope.interface-4.6.0
~~~
