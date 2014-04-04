C#: ConcatKDF 

[JWA Appendix C](https://tools.ietf.org/html/draft-ietf-jose-json-web-algorithms-23#appendix-C)のパラメータで確認

ユーティリティ:

        // byte配列のマージ
        public static IEnumerable<byte> Combine(params byte[][] arrays)
        {
            foreach (byte[] a in arrays)
                foreach (byte b in a)
                    yield return b;
        }

        // 配列スライス
        public static byte[] Slice( byte[] org, 
                            int start, int end = int.MaxValue)
        {
            if (end < 0)
            {
                end = org.Length + end;
            }
            start = Math.Max(0, start);
            end = Math.Max(start, end);

            return org.Skip(start).Take(end - start).ToArray();

        }

派生関数実体:

        // NIST キー派生関数
        public byte[] ConncatKDF_SHA256(
            byte[]  agreement,
            uint    key_octets,
            byte[]  other_info
            )
        {
            byte[] dkey = new byte[0];
            for (uint counter = 1; dkey.Length < key_octets;counter++ )
                {
                    //using System.Security.Cryptography; 
                    var digest = (new SHA256Managed()).ComputeHash(
                          Combine(counter.ToOctetString(),
                                agreement,
                                other_info).ToArray<byte>()
                        );
                    dkey = Combine(dkey, digest).ToArray<byte>();
                }

            return Slice(dkey, 0, (int)key_octets);
        }

テスト:

        [TestMethod]
        public void EcDeriveKey()
        {
            // JWA Appendix C 
            var agreement = new byte[]{
                158, 86, 217, 29, 129, 113, 53, 211, 
                114, 131, 66, 131, 191, 132,
                38, 156, 251, 49, 110, 163, 218, 128, 
                106, 72, 246, 218, 167, 121,
                140, 254, 144, 196
            };

            byte[] oi = new byte[]{
               0, 0, 0, 7, 
               65, 49, 50, 56,71, 67, 77, 
               0, 0, 0, 5, 
               65, 108, 105,99, 101, 
               0, 0, 0, 3, 
               66, 111, 98, 
               0, 0, 0, 128
           };
            uint key_octs = 16;

            byte[] derived_key = new byte[]{
                86, 170, 141, 234, 248, 35, 
                109, 32, 92, 34, 40, 205, 113, 167, 16,26
            };

            // Calculate Derived Key
            var result = ConncatKDF_SHA256(agreement, key_octs, oi);

            Assert.IsTrue(derived_key.SequenceEqual(result));

        }	