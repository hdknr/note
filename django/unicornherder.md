```
(slu)hdknr@wzy:~/ve/slu/src/djunions/sites/slu$ pip install unicornherder

Downloading/unpacking unicornherder
  Downloading unicornherder-0.0.10.tar.gz
  Running setup.py egg_info for package unicornherder
    
Downloading/unpacking psutil>=0.5.1 (from unicornherder)
  Downloading psutil-2.1.3.tar.gz (224kB): 224kB downloaded
  Running setup.py egg_info for package psutil
    
    warning: no previously-included files matching '*' found under directory 'docs/_build'
Installing collected packages: unicornherder, psutil
  Running setup.py install for unicornherder
    
    Installing unicornherder script to /home/hdknr/ve/slu/bin
  Running setup.py install for psutil
    building '_psutil_linux' extension
    gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -I/usr/include/python2.7 -c psutil/_psutil_linux.c -o build/temp.linux-x86_64-2.7/psutil/_psutil_linux.o
    gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-z,relro build/temp.linux-x86_64-2.7/psutil/_psutil_linux.o -o build/lib.linux-x86_64-2.7/_psutil_linux.so
    building '_psutil_posix' extension
    gcc -pthread -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -fPIC -I/usr/include/python2.7 -c psutil/_psutil_posix.c -o build/temp.linux-x86_64-2.7/psutil/_psutil_posix.o
    gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-z,relro build/temp.linux-x86_64-2.7/psutil/_psutil_posix.o -o build/lib.linux-x86_64-2.7/_psutil_posix.so
    
    warning: no previously-included files matching '*' found under directory 'docs/_build'
Successfully installed unicornherder psutil
Cleaning up...

```

```
(slu)hdknr@wzy:~/ve/slu/src/djunions/sites/slu$ unicornherder --help

usage: unicornherder [-h] [-u TYPE] [-b UNICORN_BIN] [-g GUNICORN_BIN]
                     [-p PATH] [-t 30] [-v]
                     ...

Manage daemonized (g)unicorns.

positional arguments:
  args                  Any additional arguments will be passed to
                        unicorn/gunicorn. Prefix with '--' if you are passing
                        flags (e.g. unicornherder -- -w 4 myapp:app)

optional arguments:
  -h, --help            show this help message and exit
  -u TYPE, --unicorn TYPE
                        The type of unicorn to manage (gunicorn,
                        gunicorn_django, unicorn, unicorn_rails)
  -b UNICORN_BIN, --unicorn-bin UNICORN_BIN
                        path to a specific unicorn to manage
  -g GUNICORN_BIN, --gunicorn-bin GUNICORN_BIN
                        path to a specific gunicorn to manage
  -p PATH, --pidfile PATH
                        Path to the pidfile that unicorn will write
  -t 30, --timeout 30   Timeout in seconds to start workers
  -v, --version         show program's version number and exit

```

pidファイルが存在すると"Gunicorn died. Exiting."になるけどプロセスは起動している
