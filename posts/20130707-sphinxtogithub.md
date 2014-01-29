Date: 2013-07-07 20:00
Title: sphinx-to-github : Virtualenvの環境によってはエラー
Type: post  
Excerpt:   

同じMacに作ったVirtualenvでうまく行く環境と例外起きる環境がある。

make htmlすると例外:

    # Sphinx version: 1.2b1
    # Python version: 2.7.2
    # Docutils version: 0.10 release
    # Jinja2 version: 2.7
    Traceback (most recent call last):
      File "/Users/hide/ve/docs/src/sphinx/sphinx/cmdline.py", line 247, in main
        app.build(force_all, filenames)
      File "/Users/hide/ve/docs/src/sphinx/sphinx/application.py", line 220, in build
        self.emit('build-finished', None)
      File "/Users/hide/ve/docs/src/sphinx/sphinx/application.py", line 353, in emit
        results.append(callback(self, *args))
      File "/Users/hide/ve/docs/src/sphinxtogithub/sphinxtogithub/sphinxtogithub.py", line 313, in sphinx_extension
        layout.process()
      File "/Users/hide/ve/docs/src/sphinxtogithub/sphinxtogithub/sphinxtogithub.py", line 172, in process
        handler.process()
      File "/Users/hide/ve/docs/src/sphinxtogithub/sphinxtogithub/sphinxtogithub.py", line 53, in process
        text = replacer.process( text )
      File "/Users/hide/ve/docs/src/sphinxtogithub/sphinxtogithub/sphinxtogithub.py", line 37, in process
        return text.replace( self.from_, self.to )
    UnicodeDecodeError: 'ascii' codec can't decode byte 0xc2 in position 1709: ordinal not in range(128)


とりあえず動くように[FileHandler.process](https://github.com/michaeljones/sphinx-to-github/blob/master/sphinxtogithub/sphinxtogithub.py#L48)を修正:


    class FileHandler(object):
        "Applies a series of replacements the contents of a file inplace"
    
        def process(self):
    
            text = self.opener(self.name).read()
            text = text.decode('utf8')      #: Dirtyfix
    
            for replacer in self.replacers:
                text = replacer.process( text )
    
            text = text.encode('utf8')      #: Dirtyfix
            self.opener(self.name, "w").write(text)

Pythonがよくわかってない。。。。