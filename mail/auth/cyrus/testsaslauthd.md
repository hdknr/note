# testsaslauthd

## Cyrus sasld testsaslauthd connect() : No such file or directory 0


~~~bash
# cd /var/run.
# mv saslauthd saslauthd.bak
# ln -s /var/spool/postfix/var/run/saslauthd /var/run/saslauthd
# service saslauthd restart
~~~