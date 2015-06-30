## 文字列フォーマット

- [String.Format in javascript?](https://stackoverflow.com/questions/2534803/string-format-in-javascript)
- [Equivalent of String.format in JQuery](https://stackoverflow.com/questions/1038746/equivalent-of-string-format-in-jquery)


~~~js

function format(str, obj) {
    return str.replace(
    	/\{\s*([^}\s]+)\s*\}/g, 
    	function(m, p1, offset, string) {
	        return obj[p1]
    	}
    );
}
~~~