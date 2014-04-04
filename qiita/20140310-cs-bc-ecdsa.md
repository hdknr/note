C# : BouncyCastle で ECDSAで署名/検証

NistのCurve(X9ECParameters)に対する拡張メソッドを定義:

    /// <summary>
    /// Extends Org.BouncyCastle.Asn1.X9.X9ECParametersExtends
    /// </summary>
    public static class X9ECParametersExtends
    {
        // Curveのドメインパラメター
        public static ECDomainParameters GetDomainParams(this X9ECParameters ec)
        {
          return new ECDomainParameters( ec.Curve, ec.G, ec.N, ec.H);
        }

        // 非対称キーを作成
        public static AsymmetricCipherKeyPair GenerateKeyPair(this X9ECParameters ec)
        {
            IAsymmetricCipherKeyPairGenerator g = GeneratorUtilities.GetKeyPairGenerator("ECDSA");
            g.Init(new ECKeyGenerationParameters(ec.GetDomainParams(), new SecureRandom()));
            return  g.GenerateKeyPair();
        }

        // BigIntegerの x, y を Pointに変換
        public static ECPoint ToPoint(this X9ECParameters ec, BigInteger x, BigInteger y)
        {
            FpCurve c = (FpCurve)ec.Curve;
            return new FpPoint(c,
                    new FpFieldElement(c.Q, x),
                    new FpFieldElement(c.Q, y));
        }
        
        // キーマテリアルからパブリックキーを復元
        public static ECPublicKeyParameters CreatePublicKey(this X9ECParameters ec, BigInteger x, BigInteger y)
        {
            return new ECPublicKeyParameters(ec.ToPoint(x, y), ec.GetDomainParams());
        }
        // キーマテリアルからプライベートキーを復元
        public static ECPrivateKeyParameters CreatePrivateKey(this X9ECParameters ec, BigInteger d)
        {
            return new ECPrivateKeyParameters(d, ec.GetDomainParams());
        }

        // Signerを生成 ( Jwaでサポートしているやつだけ)
        public static ISigner GetSigner( this X9ECParameters ec )
        {
            int bits = (ec.Curve.FieldSize == 521) ? 512 : ec.Curve.FieldSize;
            return  SignerUtilities.GetSigner(string.Format("SHA-{0}withECDSA",bits));
        }
        
        // 署名を作る
        public static byte[] Sign(this X9ECParameters ec, ECPrivateKeyParameters key, byte[] src)
        {
            return  ec.GetSigner().Sign(key, src);
        }
        
        // 署名を検証する
        public static bool Verify(this X9ECParameters ec, ECPublicKeyParameters key, byte[] src, byte[] signature)
        {
            return ec.GetSigner().Verify(key, src, signature);
        }
         
    }

ISignerにも同じく拡張メソッドを定義

    /// <summary>
    /// Extends Org.BouncyCastle.Crypto.ISigner
    /// </summary>
    public static class SignerExtends
    {
        public static byte[] Sign(this ISigner signer, ECPrivateKeyParameters key, byte[] src)
        {
            signer.Init(true, key);
            signer.BlockUpdate(src, 0, src.Length);
            return  signer.GenerateSignature();
        }

        public static bool Verify(this ISigner signer, ECPublicKeyParameters  key, byte[] src, byte[] signature)
        {
            signer.Init(false, key);
            signer.BlockUpdate(src, 0, src.Length);
            return signer.VerifySignature(signature);
        }
    }

テスト:


        [TestMethod]
        public void EcTestKey()
        {
			// NIST P-521
            string curveName = "P-521";
            var nistCurve = NistNamedCurves.GetByName(curveName);

			// TEXT
            var msg = "Hello, it's me.";
            var msg_bytes = System.Text.Encoding.UTF8.GetBytes(msg);


            // Sender Provide Ephemeral Key Pair
            AsymmetricCipherKeyPair keypair = nistCurve.GenerateKeyPair();
            var pri =( ECPrivateKeyParameters) keypair.Private;
            var signature = nistCurve.Sign(pri, msg_bytes);

            // Transfer Curve,  Point, Message Source and Signature to Recepient
            var pub = (ECPublicKeyParameters)keypair.Public;
            var x = pub.Q.X.ToBigInteger();
            var y = pub.Q.Y.ToBigInteger();

            // Restore Curve and Public Key
            var v_curve = NistNamedCurves.GetByName(curveName);
            var v_pub = v_curve.CreatePublicKey(x, y);
                
            // Recipient Verify
            Assert.IsTrue( v_curve.Verify(v_pub, msg_bytes, signature ));

            // Restore Private Key and Try again
            var pri2 = nistCurve.CreatePrivateKey(pri.D);
            var sig2 = nistCurve.Sign(pri2, msg_bytes);
            Assert.IsTrue(nistCurve.Verify(v_pub, msg_bytes, sig2));           
        }