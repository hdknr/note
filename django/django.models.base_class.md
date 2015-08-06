Python: 動的に多重継承させる(`__base__`)をいじる

- 後でなにやってるかわからなくなるからやめたほうがいい
- １年寝かせた自分のクソコードを追ってたら最初意味不明でした

## Djangoのモデルを動的に多重継承させる
- ヘルパークラスのメソッドを注入する

~~~py
from django.utils.importlib import import_module                                 

class BaseModel(models.Model):                                                      
                                                                                    
    def __init__(self, *args, **kwargs):                                            
        super(BaseModel, self).__init__(*args, **kwargs) 
        
        # コンストラクタ実行後、基底クラスをいじる                           
        self.patch_helper(self.helper())                                            
                                                                                    
    _helper = None  		                                                             
    @classmethod                                                                    
    def helper(cls):
    	'''ヘルパークラスを探して返す '''                                                                
        if cls._helper is None:
        	# modelsの下でにhelpersモジュールを探す                                                     
            mod = import_module(
            	cls.__module__.replace('models','helpers'))  
			# helpersモジュールの中から、クラス名と同じ名前のクラスを探す
			# なかったら object               
            cls._helper = getattr(mod, cls.__name__, object)                        
        return cls._helper                                                          
                                                                                    
    @classmethod                                                                    
    def patch_helper(cls, helper):    
    	''' 指定されたヘルパークラスが __bases__になかったら追加する '''                                              
        if helper and helper not in  cls.__bases__:                                 
            cls.__bases__ = cls.__bases__ + (helper,)   
~~~                            