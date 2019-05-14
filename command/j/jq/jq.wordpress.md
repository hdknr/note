# Wordpress API

## `id` と `title` を表示 (`-r` (raw) でダブルクオートを表示しない)

~~~bash
$ curl -s http://192.168.56.54:8080/wp-json/wp/v2/posts/ | jq '.[] | "\(.id) , \(.title.rendered)"' -r
.
~~~
