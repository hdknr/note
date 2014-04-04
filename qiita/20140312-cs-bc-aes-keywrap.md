C#: BouncyCastleのAES Key Wrap (RFC3394)

AESでKEK(Key Encryption Key:16,24,32オクテット)でCEK(Content Encryption Key)をラップ:

```csharp
       public static byte[] Wrap(byte[] kek, byte[] plaint)
        {
            // using Org.BouncyCastle.Crypto.Engines;
            var en = new AesWrapEngine();

            //  Org.BouncyCastle.Crypto.Parameters;
            en.Init(true, new KeyParameter(kek));

            return en.Wrap(plaint, 0, plaint.Length);
        }
```

同じくラップをほどく:


```csharp

        public static byte[] Unwrap(byte[] kek, byte[] ciphert)
        {
            var en = new AesWrapEngine();
            en.Init(false, new KeyParameter(kek));
            return en.Unwrap(ciphert, 0, ciphert.Length);
        }
```

テスト:

```csharp

        [TestMethod]
        public void AesWrap()
        {
            // https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-23#appendix-A.3.3
            
            var cek = new byte[]{
                4, 211, 31, 197, 84, 157, 252, 254,
                11, 100, 157, 250, 63, 170, 106, 206,
                107, 124, 212, 45, 111, 107, 9, 219,
                200, 177, 0, 240, 143, 156, 44, 207};

            var cek_ci = new byte[]{
                232, 160, 123, 211, 183, 76, 245,
                132, 200, 128, 123, 75, 190, 216,
                22, 67, 201, 138, 193, 186, 9, 91,
                122, 31, 246, 90, 28, 139, 57, 3,
                76, 124, 193, 11, 98, 37, 173, 61, 104, 57};

            var kek_b64url = "GawgguFyGrWKav7AX4VKUg";

            var kek = Jose.Utils.FromBase64Url(kek_b64url);
            Assert.IsTrue( kek.Length == 16 || kek.Length == 24 || kek.Length == 32);

            var wrapped = Aes.Wrap(kek, cek);
            Assert.IsTrue(cek_ci.SequenceEqual(wrapped));

            var unwrapped = Aes.Unwrap(kek, wrapped);
            Assert.IsTrue(cek.SequenceEqual(unwrapped));

        }
```
