# [tag](https://git-scm.com/docs/git-tag)

~~~
git tag [-a | -s | -u <keyid>] [-f] [-m <msg> | -F <file>] [-e]
	<tagname> [<commit> | <object>]
git tag -d <tagname>…​
git tag [-n[<num>]] -l [--contains <commit>] [--no-contains <commit>]
	[--points-at <object>] [--column[=<options>] | --no-column]
	[--create-reflog] [--sort=<key>] [--format=<format>]
	[--merged <commit>] [--no-merged <commit>] [<pattern>…​]
git tag -v [--format=<format>] <tagname>…​
~~~

## `-a` /  `--annotate`


- Make an unsigned, annotated tag object

~~~bash
% git tag -a tag-release-2020 -m "2020年リリース"
% git push --follow-tags
~~~

- [Git Tag And Push Git Tag](https://vivaxyblog.github.io/2019/08/02/git-tag-and-push-git-tag.html)
