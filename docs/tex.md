# TeX/LaTex

## 環境

### macOS

- [MacTeX](https://texwiki.texjp.org/?MacTeX#mirror)

### VS Code

- [VScodeで快適LaTeX環境を構築する方法 - Qiita](https://qiita.com/ichigism/items/707e8a5def368a69e9a6)

### Jupyter Notebook

- [Jupyter (iPython) Notebookを使って技術ノート環境を構築する方法 - MyEnigma](https://myenigma.hatenablog.com/entry/2016/02/20/183423)
- [Jupyter NotebookをGitHub上で公開する - abcdefg.....](http://pppurple.hatenablog.com/entry/2016/06/11/194713)


#### SymPy

- [Sympy+Jupyterで最強の電卓環境を作る - Qiita](https://qiita.com/pashango2/items/500d23c8f43784b54315)
- [Pythonの数式処理ライブラリSymPyをWolfram Alpha(Mathematica, Maxima)の代わりに使う方法 - MyEnigma](https://myenigma.hatenablog.com/entry/2015/11/21/222755)
- Anacondaにはsympyが入っています

~~~bash
$ pip install sympy
~~~

~~~py
from sympy import *
init_printing()

x = Symbol('x')
y = Symbol('y')

expand(1/(x + y))
~~~

## TeX

- [分数](http://www.latex-cmd.com/equation/frac.html)


## Markdown Latex

- [Markdown/LaTeX記法比較表 - Qiita](https://qiita.com/icoxfog417/items/41a6793579eaf7bc0e00)


## 分数

- [LaTeXコマンド集 - 分数 (frac,cfrac)](http://www.latex-cmd.com/equation/frac.html)


~~~latex
\begin{equation*}
 z = \frac{1}{a + b + c} + \frac{2}{e + f + g}
\end{equation*}
~~~
