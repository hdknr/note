Date: 2014-01-07 17:00
Title:  PHP: php-simple-html-dom-parser
Type: post  
Excerpt:   


UnittestでHTML確認したくて。Pythonの[BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) + [soupselect](https://github.com/simonw/soupselect) みたいで使える気がする。


[php-simple-html-dom-parser](https://github.com/sunra/php-simple-html-dom-parser) 指定:
    
    $ vi composer.json
    
        "require": {
            "php": ">=5.4.0",
            "rmccue/requests": ">=1.0",
            "sunra/php-simple-html-dom-parser": "v1.5.0"
        },  
    
Composer更新:

    $ php composer.phar update
    Loading composer repositories with package information
    Updating dependencies (including require-dev)
      - Removing symfony/yaml (v2.4.0)
      - Installing symfony/yaml (v2.4.1)
        Downloading: 100%         
    
      - Installing rmccue/requests (v1.6.0)
        Loading from cache
    
    Writing lock file
    Generating autoload files
    

テストコード:
    
    $ vi test/Connect/DiscoveryTest.php 
    
    <?php
    
    use Sunra\PhpSimple\HtmlDomParser;
    
    class DiscoveryTest extends PHPUnit_Framework_TestCase
    {
        
        public function testRequests(){
            $res = Requests::get('http://twitter.com/', array('Accept' => 'text/html'));
            $dom = HtmlDomParser::str_get_html( $res->body );
            $elm = $dom->find("span.visuallyhidden",0);
            $this->assertEquals($elm->innertext,"Twitter");
        }   
        //....
    }

うまく行く:
    
    $ vendor/phpunit/phpunit/phpunit.php 
    PHPUnit 3.7.28 by Sebastian Bergmann.
    
    Configuration read from /home/hdknr/php/phpconnect/phpunit.xml
    
    ..
    
    Time: 1.05 seconds, Memory: 7.00Mb
    
    OK (2 tests, 2 assertions)
