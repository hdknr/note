## 連想配列

- [How do I test if an item is in a bash array?](http://unix.stackexchange.com/questions/177138/how-do-i-test-if-an-item-is-in-a-bash-array)
- [Bash associative array examples](http://www.artificialworlds.net/blog/2012/10/17/bash-associative-array-examples/)

~~~bash
function inArray # ( keyOrValue, arrayKeysOrValues )
{
  local e
  for e in "${@:2}"; do  
    [[ "$e" == "$1" ]] && return 0;  
  done
  return 1
}

function PRJECT(){
  declare -A P

  P['address']=/vagrant/projects/address/apps/web
  P['ec']=/vagrant/projects/ec/neapp

  if inArray $1 ${!P[@]}; then
    echo "Yes:" ${P[$1]}
  else
    echo "Keys:"  ${!P[@]}
    echo "Keys:"  ${P[@]}
  fi  
}
~~~
