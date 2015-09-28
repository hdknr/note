## Alembic

- 蒸留器
- [Integrating Alembic with SQLAlchemy](https://stackoverflow.com/questions/15038036/integrating-alembic-with-sqlalchemy)
- [Alembicでマイグレーションスクリプトを自動生成する最小限の設定](http://qiita.com/furico/items/f34c400f76179430e6b4)

### やってみる

~~~
$ pip install SQLAlchemy
Collecting SQLAlchemy
  Downloading SQLAlchemy-1.0.8.tar.gz (4.6MB)
    100% |████████████████████████████████| 4.6MB 119kB/s 
Installing collected packages: SQLAlchemy
  Running setup.py install for SQLAlchemy
Successfully installed SQLAlchemy-1.0.8

$ pip install alembic
Collecting alembic
  Downloading alembic-0.8.2.tar.gz (931kB)
    100% |████████████████████████████████| 933kB 540kB/s 
Requirement already satisfied (use --upgrade to upgrade): SQLAlchemy>=0.7.6 in /home/vagrant/.anyenv/envs/pyenv/versions/wordpress/lib/python2.7/site-packages (from alembic)
Collecting Mako (from alembic)
  Downloading Mako-1.0.2.tar.gz (564kB)
    100% |████████████████████████████████| 565kB 759kB/s 
Collecting python-editor>=0.3 (from alembic)
  Downloading python-editor-0.4.tar.gz
Requirement already satisfied (use --upgrade to upgrade): MarkupSafe>=0.9.2 in /home/vagrant/.anyenv/envs/pyenv/versions/wordpress/lib/python2.7/site-packages (from Mako->alembic)
Installing collected packages: Mako, python-editor, alembic
  Running setup.py install for Mako
  Running setup.py install for python-editor
  Running setup.py install for alembic
Successfully installed Mako-1.0.2 alembic-0.8.2 python-editor-0.4
~~~

~~~
$ mkdir myapp && cd myapp
~~~
~~~
$ vi models.py 
~~~
~~~py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return "<User(name='%s')>" % (self.name)
~~~

~~~
$ tree .
.
└── models.py

0 directories, 1 file
~~~

~~~
$ alembic init migrations
  Creating directory /vagrant/projects/alchemy/myapp/migrations ... done
  Creating directory /vagrant/projects/alchemy/myapp/migrations/versions ... done
  Generating /vagrant/projects/alchemy/myapp/alembic.ini ... done
  Generating /vagrant/projects/alchemy/myapp/migrations/README ... done
  Generating /vagrant/projects/alchemy/myapp/migrations/env.pyc ... done
  Generating /vagrant/projects/alchemy/myapp/migrations/env.py ... done
  Generating /vagrant/projects/alchemy/myapp/migrations/script.py.mako ... done
  Please edit configuration/connection/logging settings in '/vagrant/projects/alchemy/myapp/alembic.ini' before proceeding.
~~~

~~~
$ tree .
.
├── alembic.ini
├── migrations
│   ├── README
│   ├── env.py
│   ├── env.pyc
│   ├── script.py.mako
│   └── versions
└── models.py

2 directories, 6 files
~~~

~~~
$ vim migrations/env.py
~~~
~~~diff
@@ -15,7 +15,13 @@ fileConfig(config.config_file_name)
 # for 'autogenerate' support
 # from myapp import mymodel
 # target_metadata = mymodel.Base.metadata
-target_metadata = None
+# target_metadata = None
+import sys
+import os
+BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
+sys.path.insert(0, BASE_DIR)
+import models
+target_metadata = models.Base.metadata
~~~

~~~
$ vi alembic.ini
~~~

~~~diff
-sqlalchemy.url = driver://user:pass@localhost/dbname
+# sqlalchemy.url = driver://user:pass@localhost/dbname
+sqlalchemy.url = sqlite:////vagrant/projects/alchemy/myapp/myapp.sqlite3
~~~

~~~
$ alembic revision --autogenerate -m "Init tables"
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'users'
  Generating /vagrant/projects/alchemy/myapp/migrations/versions/2fe260c91e5d_init_tables.py ... done
~~~

~~~
$ tree migrations/versions/
migrations/versions/
├── 2fe260c91e5d_init_tables.py
└── 2fe260c91e5d_init_tables.pyc

0 directories, 2 files
~~~

~~~sql
$ sqlite3 myapp.sqlite3 
SQLite version 3.8.7.1 2014-10-29 13:59:56
Enter ".help" for usage hints.
sqlite> .tables
alembic_version
~~~

~~~sql
sqlite> .schema alembic_version
CREATE TABLE alembic_version (
        version_num VARCHAR(32) NOT NULL
);
sqlite> select count(*) from alembic_version;
0
~~~

~~~
$ alembic upgrade head
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 2fe260c91e5d, Init tables
~~~

~~~sql
sqlite> .tables
alembic_version  users 

sqlite> .schema users
CREATE TABLE users (
        id INTEGER NOT NULL, 
        name VARCHAR(255) NOT NULL, 
        PRIMARY KEY (id)
);
~~~


~~~
$ vi models.py
~~~
~~~diff
     id = Column(Integer, primary_key=True)
     name = Column(String(255), nullable=False)
+    age = Column(Integer, nullable=True)
~~~

~~~
$ alembic revision --autogenerate -m "Add 'age'"
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added column 'users.age'
  Generating /vagrant/projects/alchemy/myapp/migrations/versions/1d0ea4f78aa1_add_age.py ... done
~~~

~~~
$ more  migrations/versions/1d0ea4f78aa1_add_age.py
~~~
~~~py
"""Add 'age'

Revision ID: 1d0ea4f78aa1
Revises: 2fe260c91e5d
Create Date: 2015-09-14 08:06:27.474704

"""

# revision identifiers, used by Alembic.
revision = '1d0ea4f78aa1'
down_revision = '2fe260c91e5d'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('age', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'age')
    ### end Alembic commands ###
~~~  

~~~
$ alembic upgrade head
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 2fe260c91e5d -> 1d0ea4f78aa1, Add 'age'
~~~

~~~sql
sqlite> .schema users
CREATE TABLE users (
        id INTEGER NOT NULL, 
        name VARCHAR(255) NOT NULL, 
        age INTEGER, 
        PRIMARY KEY (id)
);
~~~

~~~py
>>> import ConfigParser
>>> config = ConfigParser.RawConfigParser()
>>> config.read('alembic.ini')
>>> config.items('alembic')
[('script_location', 'migrations'), ('sqlalchemy.url', 'sqlite:////vagrant/projects/alchemy/myapp/myapp.sqlite3')]

>>> from sqlalchemy import create_engine
>>> create_engine(config.items('alembic')[1][1])
Engine(sqlite:////vagrant/projects/alchemy/myapp/myapp.sqlite3)
>>> engine = _
>>> engine.table_names()
[u'alembic_version', u'users']


>>> from models import *

>>> from sqlalchemy.orm import sessionmaker
>>> DBSession = sessionmaker()
>>> DBSession.configure(bind=engine)
>>> session = DBSession()
>>> session.query(User).all()
[]

>>> user = User(age=32, name='Bob')
>>> user.age
32
>>> user.name
'Bob'
>>> session.add(user)
>>> session.commit()
>>> session.query(User).all()
[<User(name='Bob')>]
>>> session.query(User).filter(User.age > 30).count()
1
>>> session.query(User).filter(User.age > 40).count()
0
~~~