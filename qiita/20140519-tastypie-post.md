Tastypie: POST でデータを返す


'application/x-www-form-urlencoded'でResourceにPOSTすると、dispathから、post_detail が呼ばれます。

```py

    def post_detail(self, request, **kwargs):
        return http.HttpNotImplemented()

```


ので、これを実装します。 dispatchは最終的にHttpResponseをかえすのですが、

```py

    def dispatch(self, request_type, request, **kwargs):

        #.....

        response = method(request, **kwargs)        # method = post_detail
        #....
        if not isinstance(response, HttpResponse):
            return http.HttpNoContent()

        return response

```

なので、post_detail からHttpResponseを返さないと、 HttpNoContent(204) を返してしまいます。
locationを渡して、 getしてもらうのが基本的な考え方です。

しかしPOSTですぐ返したいので、それにはget_detail()でやっているようにbundleを作ってcreate_response()を呼んでやればいいようです。


```py

    class TokenResource(Resource):
    
        class Meta:
            allowed_methods = ['post',]
            resource_name = 'token'
            object_class = TokenRes
            authentication = ClientFormAuth()
            serializer = ObjectSerializer(formats=['json'])
    
        def post_detail(self, request, **kwargs):
        
            obj = TokenRes(access_token="__here_is_a_new_token_")
            
            bundle = self.build_bundle(obj=obj, request=request)
            bundle = self.full_dehydrate(bundle)
            bundle = self.alter_detail_data_to_serialize(request, bundle)
            return self.create_response(request, bundle)
        
```
        
always_return_data = True はResource#post_detail では全く関係ないです。
        
