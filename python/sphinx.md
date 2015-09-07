## reStruecturedText

### **匿名リンク**でハイパーリンク

- [Hyperlink Targets](http://docutils.sourceforge.net/docs/user/rst/quickref.html#hyperlink-targets)
- anonymous hyperlink target : `text`__
- anonymous hyperlink reference : __ url

~~~rst
Reference
--------------

- setup.py: `Building and Distributing Packages with Setuptools`__
- MANIFEST.in: `Creating a Source Distribution`__
- Simplified BSD License: `2-clause license ("Simplified BSD License" or "FreeBSD License")`__

__ https://pythonhosted.org/setuptools/setuptools.html
__ https://docs.python.org/2.7/distutils/sourcedist.html#source-dist
__ https://en.wikipedia.org/wiki/BSD_licenses#2-clause_license_.28.22Simplified_BSD_License.22_or_.22FreeBSD_License.22.29
~~~

~~~html
<h1>Reference</h1>
<ul class="simple">
<li>setup.py: <a class="reference external" href="https://pythonhosted.org/setuptools/setuptools.html">Building and Distributing Packages with Setuptools</a></li>
<li>MANIFEST.in: <a class="reference external" href="https://docs.python.org/2.7/distutils/sourcedist.html#source-dist">Creating a Source Distribution</a></li>
<li>Simplified BSD License: <a class="reference external" href="https://en.wikipedia.org/wiki/BSD_licenses#2-clause_license_.28.22Simplified_BSD_License.22_or_.22FreeBSD_License.22.29">2-clause license (&quot;Simplified BSD License&quot; or &quot;FreeBSD License&quot;)</a></li>
</ul>
~~~


## Autodoc

- [Include documentation from docstrings](http://sphinx-doc.org/ext/autodoc.html)

### デコレーター関数

- [Python Sphinx autodoc and decorated members](https://stackoverflow.com/questions/3687046/python-sphinx-autodoc-and-decorated-members)
- `automodule` だとdocstringがドキュメントされないので、個別に `autofunction` する
