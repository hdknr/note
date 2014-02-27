Python: クラスインスタンス用のシリアライザを用意する:

    # jose.py

    class BaseObjectSerializer(json.JSONEncoder):
    
        def default(self, obj):
            if isinstance(obj, Enum):
                return obj.value

            #:...... その他のオブジェクト判定

            if isinstance(obj, object):
                #: フィールドをdict化し、
                #: アンダースコアで始まるフィールドを無視する
                return dict([(k, v) for k, v in obj.__dict__.items()
                             if not k.startswith('_')])
    
            return super(BaseObjectSerializer, self).default(obj)

    
to_json() メソッドでエンコーダクラスを指定して json.dumps する:
    
    # jose.py 

    class BaseObject(object):
        _serializer = BaseObjectSerializer    
    
        def to_json(self, *args, **kwargs):
            kwargs['cls'] = self._serializer    #: Custom Serializer
            return json.dumps(self, *args, **kwargs)
    

足し算の結果のみをシリアライズし、途中のホルダーはシリアライズしない。:
    
    from jose import BaseObject
    
    
    class Message(BaseObject):
    
        def __init__(self, *args, **kwargs):
            super(Message, self).__init__(*args, **kwargs)
            self.total = 0 
            self._x =0
            self._y =0
    
        def sum(self, x, y): 
            self._x = x 
            self._y = y 
            self.total = self._x + self._y
    
    
    m = Message()
    m.sum(3, 4)
    assert m.total == 7
    assert m.to_json() == '{"total": 7}'
    assert m._x == 3
    
    m2 = Message()
    assert m2._x == 0

