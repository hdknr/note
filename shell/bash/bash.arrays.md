# 配列

- [6.7 Arrays](https://www.gnu.org/software/bash/manual/bash.html#Arrays)
- [Test if element is in array in bash](http://superuser.com/questions/195598/test-if-element-is-in-array-in-bash)
- [Appendix B. Reference Cards ](http://tldp.org/LDP/abs/html/refcards.html#AEN22491)
- [bash 配列まとめ](http://qiita.com/b4b4r07/items/e56a8e3471fb45df2f59)

## ループで参照

~~~bash
#!/bin/bash
ASSETS=(fonts images scripts styles)
echo "${ASSETS[@]}"
for i in ${ASSETS[@]}; do
  echo $i;
done
~~~
~~~bash 
fonts images scripts styles
fonts
images
scripts
styles
~~~

## IFSで行を配列化

~~~bash
$ export IFS=':'
$ find . -name "*.py" -exec grep -H "^import " {} \; |  while read -ra L ; do echo ${L[1]} ${L[0]}; done | sort | grep models
import hashlib ./web/accounts/models.py
import hashlib ./web/core/models.py
import hashlib ./web/magazine/models/defs.py
import hashlib ./web/magazine/models/models.py
import json ./web/core/models.py
import json ./web/tickets/models/methods.py
import mimetypes ./web/bulletins/models.py
import models ./web/accounts/filters.py
import models ./web/events/admin.py
import models ./web/payments/admin.py
import os ./web/bulletins/models.py
import os ./web/communities/models.py
import os ./web/core/models.py
import traceback ./web/core/models.py
import utils ./web/core/models.py
~~~
