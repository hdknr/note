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