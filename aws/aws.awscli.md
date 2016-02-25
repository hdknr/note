# awscli

- インストール

~~~bash

$  pip install awscli
Collecting awscli
  Downloading awscli-1.9.12-py2.py3-none-any.whl (848kB)
    100% |████████████████████████████████| 851kB 471kB/s
Collecting botocore==1.3.12 (from awscli)
  Downloading botocore-1.3.12-py2.py3-none-any.whl (2.1MB)
    100% |████████████████████████████████| 2.1MB 179kB/s
Requirement already satisfied (use --upgrade to upgrade): rsa<=3.3.0,>=3.1.2 in /Users/hide/ve/tact/lib/python2.7/site-packages (from awscli)
Collecting colorama<=0.3.3,>=0.2.5 (from awscli)
  Downloading colorama-0.3.3.tar.gz
Requirement already satisfied (use --upgrade to upgrade): docutils>=0.10 in /Users/hide/ve/tact/lib/python2.7/site-packages (from awscli)
Collecting jmespath<1.0.0,>=0.7.1 (from botocore==1.3.12->awscli)
  Downloading jmespath-0.9.0-py2.py3-none-any.whl
Collecting python-dateutil<3.0.0,>=2.1 (from botocore==1.3.12->awscli)
  Downloading python_dateutil-2.4.2-py2.py3-none-any.whl (188kB)
    100% |████████████████████████████████| 192kB 2.1MB/s
Requirement already satisfied (use --upgrade to upgrade): pyasn1>=0.1.3 in /Users/hide/ve/tact/lib/python2.7/site-packages (from rsa<=3.3.0,>=3.1.2->awscli)
Requirement already satisfied (use --upgrade to upgrade): six>=1.5 in /Users/hide/ve/tact/lib/python2.7/site-packages (from python-dateutil<3.0.0,>=2.1->botocore==1.3.12->awscli)
Installing collected packages: jmespath, python-dateutil, botocore, colorama, awscli
  Found existing installation: python-dateutil 1.5
    Uninstalling python-dateutil-1.5:
      Successfully uninstalled python-dateutil-1.5
  Running setup.py install for colorama
Successfully installed awscli-1.9.12 botocore-1.3.12 colorama-0.3.3 jmespath-0.9.0 python-dateutil-2.4.2
~~~


~~~bash

$ which aws
/Users/hide/ve/tact/bin/aws
~~~

- 設定

~~~bash

$ aws configure
AWS Access Key ID [None]: XKIXIQXL35DTBNISJZGQ
AWS Secret Access Key [None]: yG9tmKOT85ACdFYHTA/mO/Y1OAksurhsGIl6U0yh
Default region name [None]: ap-northeast-1
Default output format [None]:
~~~

~~~bash
$ tree ~/.aws
/Users/hide/.aws
├── config
└── credentials

0 directories, 2 files
~~~

~~~bash
$ more ~/.aws/config
[default]
region = ap-northeast-1
~~~

~~~bash
$ more ~/.aws/credentials
[default]
aws_access_key_id = XKIXIQXL35DTBNISJZGQ
aws_secret_access_key = yG9tmKOT85ACdFYHTA/mO/Y1OAksurhsGIl6U0yh
~~~
