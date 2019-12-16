# grep

## 存在した時だけなにかする

~~~bash
if grep -q xvdf1 /etc/fstab; then
    echo found
else
    echo not found
fi
~~~

## HOW TO

| やりたいこと | オプション  |
| :--------- | :-------- |
| 行番号の表示 |  `-n`              |
| ハイライト   | `--color=auto`     |

## GREP_OPTIONS

~~~bash
export GREP_OPTIONS='--color=auto -n -H'
~~~
