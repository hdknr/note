python:keyringによるパスワード管理

https://bitbucket.org/kang/python-keyring-lib/

# Mac #

インストール:

    $ pip install keyring

    Downloading/unpacking keyring
      Downloading keyring-3.5.zip (88Kb): 88Kb downloaded
      Running setup.py egg_info for package keyring
        
        warning: no previously-included files found matching '.hg/last-message.txt'
    Installing collected packages: keyring
      Running setup.py install for keyring
        
        warning: no previously-included files found matching '.hg/last-message.txt'
        Installing keyring script to /Users/hide/ve/tact/bin
    Successfully installed keyring
    Cleaning up...
    
使ってみる:
    
    >>> import keyring
    >>> dir(keyring)
    ['__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__', 
     'absolute_import', 'backend', 'backends', 'core', 'credentials', 'delete_password', 
     'errors', 'get_keyring', 'get_pass_get_password', 'get_password', 'getpassbackend', 
     'logger', 'logging', 'py27compat', 'set_keyring', 'set_password', 'util']
    
Macで使えるバックエンド:

    >>> keyring.backend.get_all_keyring()
    [<keyring.backends.OS_X.Keyring object at 0x10b1a9150>, 
     <keyring.backends.file.EncryptedKeyring object at 0x10b1a47d0>, 
     <keyring.backends.file.PlaintextKeyring object at 0x10b1a9590>]
    
デフォルトでOSXのキーチェーン:

    >>> keyring.get_keyring()
    <keyring.backends.OS_X.Keyring object at 0x10b1a9150>
    
    >>> keyring.set_password('service','user','password')
    >>> keyring.get_password('service','user')
    u'password'

## キーチェーンアクセス ##

アプリケーション -> ユーティリティ -> キーチェーンアクセスを開いてログイン項目として「service」を確認できる。

## security #

OSXのバックエンドは security コマンドのラッパーです。


    $ which security
    /usr/bin/security
    
    $ security find-generic-password -a user -s service -g
    keychain: "/Users/hide/Library/Keychains/login.keychain"
    class: "genp"
    attributes:
        0x00000007 <blob>="service"
        0x00000008 <blob>=<NULL>
        "acct"<blob>="user"
        "cdat"<timedate>=0x32303134303330333138303733385A00  "20140303180738Z\000"
        "crtr"<uint32>=<NULL>
        "cusi"<sint32>=<NULL>
        "desc"<blob>=<NULL>
        "gena"<blob>=<NULL>
        "icmt"<blob>=<NULL>
        "invi"<sint32>=<NULL>
        "mdat"<timedate>=0x32303134303330333138303733385A00  "20140303180738Z\000"
        "nega"<sint32>=<NULL>
        "prot"<blob>=<NULL>
        "scrp"<sint32>=<NULL>
        "svce"<blob>="service"
        "type"<uint32>=<NULL>
    password: "password"


# Debian #


同じくpipでインストール。 ウィンドウシステムとか動いていないサーバーなので、ファイルベース:

    >>> keyring.backend.get_all_keyring()
    [<keyring.backends.file.EncryptedKeyring object at 0x28f4a50>, 
     <keyring.backends.file.PlaintextKeyring object at 0x28ebc50>]

    
    >>> current = _
    >>> dir(current[0])
    ['__abstractmethods__', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_abc_cache', '_abc_negative_cache', '_abc_negative_cache_version', '_abc_registry', '_check_file', '_classes', '_create_cipher', '_ensure_file_path', '_get_new_password', '_init_file', '_lock', '_migrate', '_unlock', 'block_size', 'decrypt', 'delete_password', 'encrypt', 'file_path', 'filename', 'get_password', 'keyring_key', 'priority', 'pw_prefix', 'set_password', 'viable']
    
    
    >>> current[0].filename
    'crypted_pass.cfg'
    >>> current[0].file_path
    '/home/hdknr/.local/share/python_keyring/crypted_pass.cfg'
    
    >>> current[1].filename
    'keyring_pass.cfg'
    >>> current[1].file_path
    '/home/hdknr/.local/share/python_keyring/keyring_pass.cfg'


作ってみる。キーストアのパスワードをrootとする:

    >>> keyring.set_password('ubuntu','user','password')
    Please enter password for encrypted keyring: root
    >>> keyring.get_password('ubuntu','user')
    u'password'
    
    >>> keyring.set_password('ubuntu','user1','password1')


## ini ファイル形式のストア ##

ホーム以下にある:

    $ more /home/hdknr/.local/share/python_keyring/crypted_pass.cfg 
    [keyring_2Dsetting]
    password_20reference = eyJwYXNzd29yZF9lbmNyeXB0ZWQiOiAiUVpqd2I1a2tKem5oMU1tdVpNL3VFTjE3QURFVU9mazg3
    	Zm9vXG4iLCAic2FsdCI6ICJ5cTFES3BkeTl1QWtZN1VWSVhkR0JkczR6RUpzQ0UraFFHMjVWa1hL
    	MWZFPVxuIiwgIklWIjogIm5uWGFlK0t3L0ErQUg1T2I2eGJiWFE9PVxuIn0=
    
    [ubuntu]
    user = eyJwYXNzd29yZF9lbmNyeXB0ZWQiOiAiK3ViUmdaRVYrRURVYTdVPVxuIiwgInNhbHQiOiAidEJt
    	OGpaUzhkTnFIYkIzZHlrOU5TZGwvTnFFOGZ6TkttWEZsZVhwYkRkRT1cbiIsICJJViI6ICJxWXFQ
    	YkY2TmV5YytFZmtZOVV0b0RRPT1cbiJ9
    user1 = eyJwYXNzd29yZF9lbmNyeXB0ZWQiOiAiL2E1Qzl2RlFQR3Y1YU5GSVxuIiwgInNhbHQiOiAidjZV
    	a3BIeHR3OGU3RnM5NDRoTTQwc1llL0hjdisrb3F0dktRSHdIeGw0az1cbiIsICJJViI6ICI0aENO
    	QWZsTDdUeVBxVW1PSlBIU3FnPT1cbiJ9	
			

user1を削除	
	
    $ vi /home/hdknr/.local/share/python_keyring/crypted_pass.cfg
    
    >>> import keyring
    >>> keyring.get_password('ubuntu','user')
    Please enter password for encrypted keyring: 
    u'password'
    >>> keyring.get_password('ubuntu','user1')
    >>> 

"root"というパスワードはまずいので、評価おわったら消す。

## Json Base64したもの ##

[keyring_2Dsetting]セクション

    >>> key_data = '''eyJwYXNzd29yZF9lbmNyeXB0ZWQiOiAiazloc1R1bmt3UERnRGo0TFY3UWljcVQybGxoSTRJS3Ns
    ...     Z1BVXG4iLCAic2FsdCI6ICJrcUZYUWhTMkR1ZEZGMjFkK3BpRmVJbll5dVkzY3V4MWlyam5OT3Zt
    ...     azBFPVxuIiwgIklWIjogIkQ0YUhEQ1VJbVhTUnFLZmN4MXRicmc9PVxuIn0='''.replace(' ','').replace('\n','')
    
    >>> import base64
    >>> import json
    >>> key_param = json.loads(base64.decodestring(key_data))
    >>> key_param
    {u'salt': u'kqFXQhS2DudFF21d+piFeInYyuY3cux1irjnNOvmk0E=\n', 
     u'password_encrypted': u'k9hsTunkwPDgDj4LV7QicqT2llhI4IKslgPU\n', 
     u'IV': u'D4aHDCUImXSRqKfcx1tbrg==\n'}
    
    >>> lambda d: dict([ (base64.decodestring(k.encode()), base64.decodestring(v.encode())) for k,v in d.items()])
    <function <lambda> at 0x7f4aba18dd70>
    >>> cv = _
    >>> key_param = cv(key_param)
    >>> key_param
    {'password_encrypted': '\x93\xd8lN\xe9\xe4\xc0\xf0\xe0\x0e>\x0bW\xb4"r\xa4\xf6\x96XH\xe0\x82\xac\x96\x03\xd4', 
     'salt': '\x92\xa1WB\x14\xb6\x0e\xe7E\x17m]\xfa\x98\x85x\x89\xd8\xca\xe67r\xecu\x8a\xb8\xe74\xeb\xe6\x93A', 
      'IV': '\x0f\x86\x87\x0c%\x08\x99t\x91\xa8\xa7\xdc\xc7[[\xae'}

## pycrypto & AES CBF ##

[pycrypto](https://www.dlitz.net/software/pycrypto/)があれば使います。
blockサイズ32で [CFBブロック暗号化](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation)。
saltを使って[キーを派生させます](https://www.dlitz.net/software/pycrypto/api/2.6/Crypto.Protocol.KDF-module.html)

    >>> from Crypto.Protocol.KDF import PBKDF2
    >>> from Crypto.Cipher import AES
    >>> pw_key = PBKDF2('root', key_param['salt'], 32)
    >>> cipher_key = AES.new(pw_key[:32], AES.MODE_CFB, key_param['IV'])
    >>> keyring_password = cipher_key.decrypt(key_param['password_encrypted']).decode('utf8')
    >>> keyring_password
    u'pw:password reference value'
    
    プレフィックス除く
    >>> p = keyring_password[3:]
    >>> p
    u'password reference value'

同じくユーザーデータ

    >>> user_data ='''eyJwYXNzd29yZF9lbmNyeXB0ZWQiOiAiY1VNVERaT1F4YWh4SElvPVxuIiwgInNhbHQiOiAicTg3
    ...     L0hDcmVOYTk1blBydFlvZVl4czB6aEVlSzVxMWdFTnUvdGtKRUhtYz1cbiIsICJJViI6ICI1TU5G
    ...     RjBZbnZzdyt2elFabWNTNmF3PT1cbiJ9'''.replace(' ','').replace('\n','')
    
    >>> user_param = cv( json.loads( base64.decodestring(user_data) ) )
    >>> user_param
    {'password_encrypted': 'qC\x13\r\x93\x90\xc5\xa8q\x1c\x8a', 'salt': '\xab\xce\xff\x1c*\xde5\xafy\x9c\xfa\xedb\x87\x98\xc6\xcd3\x84G\x8a\xe6\xad`\x10\xdb\xbf\xb6BD\x1eg', 'IV': "\xe4\xc3E\x17F'\xbe\xcc>\xbf4\x19\x99\xc4\xbak"}
    
    
    >>> pw_user = PBKDF2('root', user_param['salt'], 32)
    >>> cipher_user = AES.new(pw_user[:32], AES.MODE_CFB, user_param['IV'])
    >>> cipher_user.decrypt(user_param['password_encrypted']).decode('utf8')[3:]
    u'password'
