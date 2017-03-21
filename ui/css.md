# Webkitでチェックボックスが見えなくなる問題

~~~html
<style>
#id_enabled{ -webkit-appearance: checkbox; opacity: 1; } {# チェックボックスが見えなくなる問題 #}
</style>
~~~



# テキストを追加する

- [content プロパティ](http://www.tagindex.com/stylesheet/properties/content.html)

- 現在の言語が英語だったら日本語、 日本語だったら英語

~~~css
<style>
span.lang-flip-en:before{ content: "Japanse"; }
span.lang-flip-ja:before{ content: "English"; }
</style>
~~~

- 現在の言語を元に言語を切り替える(Django テンプレート)

~~~html
<a href="{% url 'accounts_lang' %}?redir={{ request.path }}">
    <span class="lang-flip-{{ LANGUAGE_CODE }}"></span>
</a>
~~~
