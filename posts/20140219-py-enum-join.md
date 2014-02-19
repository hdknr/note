Date: 2014-02-19 5:00
Title: python:２つのEnumを合体させたりする  
Type: post  
Excerpt:   



[多重継承とか拡張とかできないので](http://scriptogr.am/hdknr/post/python-enum):


    Signers = dict(
        RS256='RS256',
        RS512='RS512',
    )
    
    Encryptors = dict(
        A128KW='A128KW',
        A192KW='A192KW',
    )
    
    
    class AlgorithmBase(Enum):
        @property
        def is_signer(self):
            return Signers.get(self.value, None) is not None
    
        @property
        def is_encryptor(self):
            return Encryptors.get(self.value, None) is not None
    
        def __eq__(self, other):
            if isinstance(other, AlgorithmBase):
                return self.value == other.value
            return NotImplemented
    
        def __ne__(self, other):
            result = self.__eq__(other)
            if result is NotImplemented:
                return result
            return not result
    
    SignerEnum = type('SignersEnum', (AlgorithmBase, ), Signers)
    EncryptorEnum = type('EncryptorsEnum', (AlgorithmBase, ), Encryptors)

    #: AlgorithmEnum = SignerEnum + EncryptorEnum
    AlgorithmEnum = type('AlgorithmEnum', (AlgorithmBase, ),
                         dict(Signers, **Encryptors))
    
    #: テスト

    a1 = AlgorithmEnum('RS256')
    a2 = AlgorithmEnum('A128KW')
    
    assert a1.is_signer and a2.is_encryptor
    assert a1 == AlgorithmEnum.RS256 and a1 == SignerEnum.RS256
    assert a2 == AlgorithmEnum.A128KW and a2 == EncryptorEnum.A128KW
