Date: 2014-02-19  
Title:  Python: Enumは多重継承できない 
Type: post  
Excerpt:   


用途的に当たり前のような:


    from enum import Enum
    
    
    class AlgSign(Enum):
        SIGN1 = 'SIGN1'
        SIGN2 = 'SIGN2'
    
    
    class AlgEnc(Enum):
        SIGN1 = 'SIGN1'
        SIGN2 = 'SIGN2'
    
    
    class Alg(AlgSign, AlgEnc):
        pass
    

TypeErrorです:


    Traceback (most recent call last):
      File "tests.py", line 17, in <module>
        class Alg(AlgSign, AlgEnc):
      File "/v16/local/lib/python2.7/site-packages/enum/__init__.py", line 154, in __new__
        member_type, first_enum = metacls._get_mixins_(bases)
      File "/v16/local/lib/python2.7/site-packages/enum/__init__.py", line 469, in _get_mixins_
        raise TypeError("Cannot extend enumerations")
    TypeError: Cannot extend enumerations


以下も同様にだめです:


    class AlgSign(Enum):
        SIGN1 = 'SIGN1'
        SIGN2 = 'SIGN2'
    
    
    class Process(object):
        pass
    
    
    class ExAlgSign(AlgSign, Process):
        pass    
