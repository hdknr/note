C#:AES GCMでコンテンツ暗号


GCMで計算されるタグサイズは 128ビット:

```csharp

        /// <summary>
        /// JWA 4.7 tag bits = 128;
        /// </summary>
        public  const int GCM_TAG_LEN = 16;
```

GCMで暗号化してCipherTextとAuth Tag を返す。IVの他に、Additional Authenticated Dataで、Cipherのパラメータを作る:

```csharp

        public static Tuple<byte[], byte[]> AesGcmEncrypt(byte[] cek, byte[] iv, 
                                                          byte[] plaint, byte[] aad )
        {
            var gcm = new GcmBlockCipher(new AesFastEngine());

            var param = new  AeadParameters(
                    new KeyParameter(cek), 8 * GCM_TAG_LEN, iv, aad);

            gcm.Init(true, param);

            byte[] ciphert = new byte[gcm.GetOutputSize(plaint.Length)];

            int len = gcm.ProcessBytes(plaint, 0, plaint.Length, ciphert, 0);
            len += gcm.DoFinal(ciphert, len);

            var tag = gcm.GetMac();

            // trim trailing auth tag
            return Tuple.Create(ciphert.Slice(0,plaint.Length), tag);

        }
```

CipherText を Auth Tagを与えて、Plaintextに復号する。Auth Tagのチェックは復号時に同時に行われ、タグが合わないと例外。GCM Ciphierへは CipherText + Auth Tagを渡すのがポイント:

```csharp
        
        public static byte[] AesGcmDecrypt(byte[] cek, byte[] iv, 
                                           byte[] ciphert, byte[] aad, byte[] tag)
        {
            var gcm = new GcmBlockCipher(new AesFastEngine());

            var param = new AeadParameters(
                    new KeyParameter(cek), 8 * GCM_TAG_LEN, iv, aad);

            gcm.Init(false, param);

            // decrypt(ciphert + tag ) check
            var marged =  Jose.Utils.Combine(ciphert, tag).ToArray<byte>();
            byte[] plaint = new byte[gcm.GetOutputSize(marged.Length)];

            int len = gcm.ProcessBytes(marged, 0, marged.Length, plaint, 0);
            len += gcm.DoFinal(plaint, len);

            return plaint;
        }
```

[Jwe Appnendix A.1](https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption-23#appendix-A.1)のコンテンツ暗号の部分で確認:

```csharp

        [TestMethod]
        public void GmcTest()
        {
            // A.1
            var plaint = new byte[]
            {
                84, 104, 101, 32, 116, 114, 117, 101, 32, 115, 105, 103, 110, 32,
            111, 102, 32, 105, 110, 116, 101, 108, 108, 105, 103, 101, 110, 99,
            101, 32, 105, 115, 32, 110, 111, 116, 32, 107, 110, 111, 119, 108,
            101, 100, 103, 101, 32, 98, 117, 116, 32, 105, 109, 97, 103, 105,
            110, 97, 116, 105, 111, 110, 46
            };
            // A.1.2  CEK
            var cek = new byte[]{
            177, 161, 244, 128, 84, 143, 225, 115, 63, 180, 3, 255, 107, 154,
            212, 246, 138, 7, 110, 91, 112, 46, 34, 105, 47, 130, 203, 46, 122,
            234, 64, 252
            };

            // A.1.4 IV
            var iv = new byte[] { 227, 197, 117, 252, 2, 219, 233, 68, 180, 225, 77, 219 };

            // A.1.5 AAD
            var aad = new byte[]{
            101, 121, 74, 104, 98, 71, 99, 105,
            79, 105, 74, 83, 85, 48, 69,
            116, 84, 48, 70, 70, 85, 67, 73,
            115, 73, 109, 86, 117, 89, 121, 73,
            54, 73, 107, 69, 121, 78, 84, 90,
            72, 81, 48, 48, 105, 102, 81};

            // A.1.6 CipherText

            var  ciphert = new byte[]{
            229, 236, 166, 241, 53, 191, 115,
            196, 174, 43, 73, 109, 39, 122,
            233, 96, 140, 206, 120, 52, 51, 237,
            48, 11, 190, 219, 186, 80, 111,
            104, 50, 142, 47, 167, 59, 61, 181,
            127, 196, 21, 40, 82, 242, 32,
            123, 143, 168, 226, 73, 216, 176,
            144, 138, 247, 106, 60, 16, 205,
            160, 109, 64, 63, 192};

            // Tag
            var tag = new byte[]{ 
            92, 80, 104, 49, 133, 25, 161,
            215, 173, 101, 219, 211, 136, 91,
            210, 145
            };


            var ct = AesGcmEncrypt(cek, iv, plaint, aad);
            Assert.AreEqual(ct.Item2.Length, GCM_TAG_LEN);
            Assert.IsTrue(tag.SequenceEqual(ct.Item2));

            Assert.IsTrue(ciphert.SequenceEqual(ct.Item1));

            var pt = AesGcmDecrypt(cek,iv, ct.Item1, aad, ct.Item2);
            Assert.IsTrue(plaint.SequenceEqual(pt));

            Console.WriteLine(System.Text.Encoding.UTF8.GetString(pt));

            
        }
    }
```