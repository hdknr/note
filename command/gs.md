Ghostscript

## macOS

~~~bash
$ brew update && brew upgrade
$ brew install ghostscript
~~~

~~~bash 
$ gs -dNOPAUSE -sDEVICE=png16m -r256 -sOutputFile=page%03d.png
~~~

- `-sDEVICE=png16m` : the convertion to use, in this case convert to a 24-bit RGB color png file. If you value transparancy, use -sDEVICE=pngalpha.
- `-r256` : the dimensions of your png file, the smaller the number, the smaller the size of your png's. To give you an idea, -r256 comes down to 2816×2176 pixels.