Date: 2013-11-16  13:00
Title:  HTMLを整形する 
Type: post  
Excerpt:   


BeautifulSoupを使ったPythonバージョン:

    # -*- coding: utf-8 -*-
    import sys
    from BeautifulSoup import BeautifulSoup as Soup
    
    def main(script,filename = None):
        if filename:
            with open(filename) as html:
                print Soup(html.read() ).prettify()
        
    if __name__ == "__main__":
        main(*sys.argv)

fs,html を使ったNode.js:

    var fs = require('fs');
    var html = require("html");
    var arguments = process.argv.splice(2);
    fs.readFile(arguments[0], 'utf8', function (err,data) {
      if (err) {
        return console.log(err);
      }
      console.log( html.prettyPrint(data, {indent_size: 2}) );
    });

