# shortcutter

- https://pypi.org/project/shortcutter/#description

~~~py
$ pip3 install shortcutter
~~~

~~~bash 
$ shortcutter --help
usage: shortcutter [-h] [-d] [-m] [-n [NAME]] [-s] [-t] [target]

Automatic shortcut creator. Shortcuts auto-activate their environments by
default.

positional arguments:
  target                The target executable to create Desktop and Menu
                        shortcuts.

optional arguments:
  -h, --help            show this help message and exit
  -d, --desktop         Only create a desktop shortcut.
  -m, --menu            Only create a menu shortcut.
  -n [NAME], --name [NAME]
                        Name of the shortcut without extension (autoname
                        otherwise).
  -s, --simple          Create simple shortcut without activate wrapper.
  -t, --terminal        Create shortcut to environment with shortcutter (plus
                        shortcut to root environment in case of conda).
~~~

## `-d` オプションをつけること

`-d` オプションをいれないと、 `/Applications/` にも作りにいってしまいます。

~~~bash
$ shortcutter /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-5.2.0/bin/anaconda-navigator

Traceback (most recent call last):
  File "/Users/hide/.anyenv/envs/pyenv/versions/anaconda3-5.2.0/lib/python3.6/site-packages/shortcutter/base.py", line 393, in _safe_create
    ret = create()
  File "/Users/hide/.anyenv/envs/pyenv/versions/anaconda3-5.2.0/lib/python3.6/site-packages/shortcutter/base.py", line 368, in create
    return self._create_wrapped_shortcut(shortcut_name, target_path, shortcut_directory)
  File "/Users/hide/.anyenv/envs/pyenv/versions/anaconda3-5.2.0/lib/python3.6/site-packages/shortcutter/base.py", line 310, in _create_wrapped_shortcut
    return self._create_shortcut_file(shortcut_name, wrapper_path, shortcut_directory)
  File "/Users/hide/.anyenv/envs/pyenv/versions/anaconda3-5.2.0/lib/python3.6/site-packages/shortcutter/macos.py", line 58, in _create_shortcut_file
    'end tell\n')
  File "/Users/hide/.anyenv/envs/pyenv/versions/anaconda3-5.2.0/lib/python3.6/site-packages/shortcutter/macos.py", line 25, in create_shortcut
    raise ShortcutError("Error occured creating app - {}".format(str(result.stderr)))
shortcutter.exception.ShortcutError: Error occured creating app - b"osacompile: couldn't write to file /Applications/anaconda-navigator.app: errOSABadStorageType (-1752).\n"
Failed to create menu shortcut.
Desktop shortcut was created for '/Users/hide/.anyenv/envs/pyenv/versions/anaconda3-5.2.0/bin/anaconda-navigator'.
~~~

## ターミナル

- ダブルクリックするとターミナルが開きます:
- 以下の例だと、指定 `python` の `virtualenv` でターミナルが開きます

~~~bash 
$ shortcutter /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-5.2.0/bin/python --terminal

Desktop and menu shortcuts were created for 'terminal at environment'.
~~~

~~~bash
Last login: Mon Sep  3 23:47:55 on ttys009
/Users/hide/.anyenv/envs/pyenv/versions/anaconda3-5.2.0/bin/shortcutter__Terminal_at_anaconda3_5_2_0
Peeko-2:~ hide$ /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-5.2.0/bin/shortcutter__Terminal_at_anaconda3_5_2_0

(base) bash-4.4$ which python
/Users/hide/.anyenv/envs/pyenv/versions/anaconda3-5.2.0/bin/python
~~~


