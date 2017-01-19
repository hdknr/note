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
