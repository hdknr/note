# Format strings and escaping

~~~bash
$ python vendors dump_category | jq -r ".[] | [.full_name, .full_slug] | @csv"
.
~~~