## ビューの処理に割り込んで引数を追加する

- デコレータを定義

~~~python
from functools import wraps                                                         
                                                                                    
                                                                                    
def traced(methods=['POST']):                                                       
    ''' view trace         	                                                         
                                                                                    
        @traced()                                                                   
        def view_list(request, *args, **kwargs):                                    
            return HttpResponse()                                                   
    '''                                                                             
                                                                                    
    def _traced(view_func):                                                         
        ''' view_func: decorated function in django view '''                        
                                                                                    
        def _decorator(request, *args, **kwargs):                                   
            if request.method in methods:                                           
                trace = "create trace instance, and git to view function"           
                kwargs['trace'] = trace                                             
            response = view_func(request, *args, **kwargs)                          
            return response                                                         
        return wraps(view_func)(_decorator)                                         
                                                                                    
    return _traced      
~~~    