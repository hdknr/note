
[Element UI paginationの現在ページを強制的に変更させたい](https://qiita.com/hoshiaya/items/76cb4d0b00a502cb41e1)

current-page.sync:

~~~html
<el-pagination
  ref="pagination"
  layout="prev, pager, next"
  :total="50"
  :current-page.sync="currentPage">
</el-pagination>
~~~