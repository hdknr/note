# 正規表現

| 種類	        | コマンド	 | 説明           |
| ------------- | -------- | ------------- |
| BRE           |                          | Basic Regular Express  |
| 基本正規表現    |  `sed`, `sed --posix`, `grep`       | BREをGNU拡張したもの。7つの正規表現演算子でエスケープが必要 |
| 拡張正規表現	  |  `sed -r` / `sed -E`, `grep -E`, `egrep` | Extended Reuglar Exression (ERE)。7つの正規表現演算子がエスケープ無しで使える |


BREでエスケープ必要:

| BRE             | ERE                   |
| --------------- | --------------------- |
| `\+`            |	`+` |
| `\?`  |	`?` |
| `\{n,m\}`  |	`{n,m}` |
| `\{n,\}`  |	`{n,}` |
| `\{n\}`  |	`{n}` |
| `\(regexp\)`  |	`(regexp)` |
| `\|`  |	`|` |

不要(BRE == ERE):

| BRE             | ERE                   |
| --------------- | --------------------- |
| `*`	          | `*` |
| `.`  |	`.` |
| `^`  |	`^` |
| `$`  |	`$` |
| `\1 \2 \3 \4 \5 \6 \7 \8 \9`  |	`\1 \2 \3 \4 \5 \6 \7 \8 \9` |
| `[char-list]`  |	`[char-list]` |
| `[:alnum:]`  |	`[:alnum:]` |
| `[:alpha:]`  |	`[:alpha:]` |
| `[:blank:]`  |	`[:blank:]` |
| `[:cntrl:]`  |	`[:cntrl:]` |
| `[:digit:]`  |	`[:digit:]` |
| `[:graph:]`  |	`[:graph:]` |
| `[:lower:]`  |	`[:lower:]` |
| `[:print:]`  |	`[:print:]` |
| `[:punct:]`  |	`[:punct:]` |
| `[:space:]`  |	`[:space:]` |
| `[:upper:]`  |	`[:upper:]` |
| `[:xdigit:]`  |	`[:xdigit:]` |
| `\b`  |	`\b` |
| `\B`  |	`\B` |
| `\<`  |	`\<` |
| `\>`  |	`\>` |
| `\w`  |	`\w` |
| `\W`  |	`\W` |

## `.+`

~~~bash
$ echo "class Model(models.Model):" | sed  's/(.\+//'

class Model


$ echo "class Model(models.Model):" | sed -e 's/(.\+//'

class Model                                                                   
~~~

### `.*`

~~~bash
$ echo "class Model(models.Model):" | sed  's/(.*//'
class Model
~~~
