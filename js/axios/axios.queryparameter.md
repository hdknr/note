## 配列を送信する(URLSearchParams)

- `{staus: [2, 3]}` を送信すると、 `staus[]=[2, 3]`  を送ってしまう
- `status=2&status=3` と送りたい


[URLSearchParams](https://developer.mozilla.org/ja/docs/Web/API/URLSearchParams) オブジェクトに変換する:

~~~js
to_query_object(obj){
    let query = new URLSearchParams();
    Object.keys(obj).map((i)=>{
      const val = obj[i];
      if (val instanceof Array) {
        val.map((j) => { query.append(i, j); });
      } else {
        query.append(i, obj[i]);
      }
    })
    return query;
}
~~~

~~~js
const qo = to_query_object(params);
axios.get(url, {params: qo}).then((res) => {
    ...
});
~~~

### 記事

- [URLSearchParamsによる簡単URL操作
](https://qiita.com/yoichiro6642/items/ea0508651ba20f4bfe14)
