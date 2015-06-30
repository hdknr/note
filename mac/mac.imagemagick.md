## imagemagick install

~~~
$ brew install ImageMagick
==> Downloading https://homebrew.bintray.com/bottles/imagemagick-6.9.0-3.yosemite.bottle.tar.gz
######################################################################## 100.0%
==> Pouring imagemagick-6.9.0-3.yosemite.bottle.tar.gz
Error: The `brew link` step did not complete successfully
The formula built, but is not symlinked into /usr/local
Could not symlink bin/convert
Target /usr/local/bin/convert
already exists. You may want to remove it:
  rm '/usr/local/bin/convert'

To force the link and overwrite all conflicting files:
  brew link --overwrite imagemagick

To list all files that would be deleted:
  brew link --overwrite --dry-run imagemagick

Possible conflicting files are:
/usr/local/bin/convert
/usr/local/share/man/man1/convert.1
==> Summary
🍺  /usr/local/Cellar/imagemagick/6.9.0-3: 1440 files, 22M
~~~

~~~
$ rm '/usr/local/bin/convert'
override rwxr-xr-x  root/wheel for /usr/local/bin/convert? yes

$ ls /usr/local/bin/convert
ls: /usr/local/bin/convert: No such file or directory

$ brew link --overwrite imagemagick
Linking /usr/local/Cellar/imagemagick/6.9.0-3... 71 symlinks created
~~~

## convert

- 横並び

~~~
$ convert +append 26.csv.png  26.xls.png 26.xlsx.png  26.png
~~~

- 縦並び

~~~
$ convert -append 26.csv.png  26.xls.png 26.xlsx.png  26.png
~~~


