# JSON データの受け渡し

## 定義

~~~html
<script type="application/json" id="pagedata">
{
    "category": "dog",
    "name": "andy"
}
</script>
~~~

## スクリプトから利用

~~~html
<script>
const json_data = JSON.parse(document.getElementById("pagedata").textContent);
console.log(json_data);
</script>
~~~


## 記事

- [HTML に JSON データを埋め込んで JavaScript から利用する - Qiita](https://qiita.com/hoto17296/items/197bdf91f97a33a69dfc)
