Python: RFC3394 AES Key Wrapを実装してみた

[RFC 3394 AES Key Wrap](http://tools.ietf.org/html/rfc3394.html)の実装してみた


pycryptoから拝借:

```py

    from Crypto.Cipher import AES
    from Crypto.Util.strxor import strxor
```

64ビットのxorとかで使う:

```py

    from struct import pack
```

テキストを8オクテットブロックで処理するので分割

```py

    slice = lambda s, n: [s[i:i + n] for i in range(0, len(s), n)]
```

RFC3394 2.2.3.1 に定義されている初期値:

```py

    AES_IV = b'\xA6\xA6\xA6\xA6\xA6\xA6\xA6\xA6'
```

RFC3394 2.2.1 で定義されているラップ処理:

```py
    def aes_key_wrap(K, P):
        """
        aes key wrap : :rfc:`3394` 2.2.1
    
            :param str K: key encrytpion key
            :param str P: plaintext
        """
    
        assert len(K) * 8 in [128, 192, 256]  # key bits
        assert len(P) % 8 == 0     # 64 bit blok
    
        n = len(P) / 8      # 64 bit blocks
        A = AES_IV          # Set A = IV
        R = [b'\0\0\0\0\0\0\0\0'
             ] + slice(P, 8)     # copy of slice every 8 octets
                            # For i = 1 to n ; R[i] = P[i]
    
        _AES = AES.AESCipher(K)
        for j in range(0, 6):               # For j=0 to 5
            for i in range(1, n + 1):       # For i=1 to n
                B = _AES.encrypt(A + R[i])  # B = AES(K, A | R[i])
                R[i] = B[8:]                # R[i] = LSB(64, B)
    
                t = pack("!q", (n * j) + i)
                A = strxor(B[:8], t)
                # A = MSB(64, B) ^ t where t = (n*j)+i
    
        R[0] = A            # Set C[0] = A
        return "".join(R)   # For i = 1 to n C[i] = R[i]
```

RFC3394 2.2.2 で定義されているアンラップ処理:


```py
    def aes_key_unwrap(K, C):
        """
        aes key unwrap : :rfc:`3394` 2.2.2
    
            :param str K: key encrytpion key
            :param str C: ciphertext
        """
    
        assert len(K) * 8 in [128, 192, 256]  # key bits
        assert len(C) % 8 == 0     # 64 bit blok
    
        n = len(C) / 8 - 1         # 64bit blocks - 1 loops
        R = slice(C, 8)
        A = R[0]                   # Set A = C[0] (=R[0])
        R[0] = [b'\0\0\0\0\0\0\0\0']
                                   # init R[0]
                                   # For i = 1 to n ; R[i] = C[i]
    
        _AES = AES.AESCipher(K)
        for j in range(5, -1, -1):           # For j = 5 to 0
            for i in range(n, 0, -1):        # For i = n to 1
                t = pack("!q", (n * j) + i)  # t = n * j + i
                src = strxor(A, t) + R[i]             # A ^ t
                B = _AES.decrypt(src)
                # B = AES-1(K, (A ^ t) | R[i]) where t = n*j+i
    
                A = B[:8]                    # A = MSB(64, B)
                R[i] = B[8:]                 # R[i] = LSB(64, B)
    
        if A == AES_IV:
            return "".join(R[1:])   # For i = 1 to n; P[i] = R[i]
        else:
            raise Exception("unwrap failed: Invalid IV")

```

テスト [Jwe Appendix A.3](https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-23#appendix-A.3.3) のCEKのラップの確認:

```py
    def test_key_wrap(self):
        # values from Jwe Appendix A.3
        cek_oct = [
            4, 211, 31, 197, 84, 157, 252, 254,
            11, 100, 157, 250, 63, 170, 106, 206,
            107, 124, 212, 45, 111, 107, 9, 219,
            200, 177, 0, 240, 143, 156, 44, 207]
        cek_ci_oct = [
            232, 160, 123, 211, 183, 76, 245,
            132, 200, 128, 123, 75, 190, 216,
            22, 67, 201, 138, 193, 186, 9, 91,
            122, 31, 246, 90, 28, 139, 57, 3,
            76, 124, 193, 11, 98, 37, 173, 61, 104, 57]

        cek = ''.join(chr(i) for i in cek_oct)
        cek_ci = ''.join(chr(i) for i in cek_ci_oct)

        jwk_dict = {
            "kty": "oct",
            "k": "GawgguFyGrWKav7AX4VKUg"
        }
        kek = base64.base64url_decode(jwk_dict['k'])
        from jose.jwa.aes import aes_key_wrap, aes_key_unwrap

        rk = aes_key_wrap(kek, cek)
        self.assertEqual(rk, cek_ci)

        urk = aes_key_unwrap(kek, cek_ci)
        self.assertEqual(urk, cek)

```