# Format strings and escaping

- @text
- @json
- @html
- @uri
- @csv
- @tsv
- @sh
- @base64
- @base64d


~~~bash
$ python vendors dump_category | jq -r ".[] | [.full_name, .full_slug] | @csv"
.
~~~
