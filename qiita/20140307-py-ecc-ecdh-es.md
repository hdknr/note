Python: Jwa/Jwe ECDH-ESの検証

ECDHで共有するシークレットをConcatKDFで派生させて作ったキーを共有キーとするのがECDH-ES。
このキーをつかって[192|384|512]ビットのランダム生成させた共有キーをラップして渡すのが、
ECDH-ES+AnnnWKのようです。

JWAの [Appendix.C](https://tools.ietf.org/html/draft-ietf-jose-json-web-algorithms-23#appendix-C) のEDCHキー派生の検証.

    def test_ecdh(self):
        '''
        https://tools.ietf.org/html/draft-ietf-jose-json-web-algorithms-23#appendix-C
        '''

# キーマテリアル #

 

        v_stc_material = {
            "kty": "EC",
            "crv": "P-256",
            "x": "gI0GAILBdu7T53akrFmMyGcsF3n5dO7MmwNBHKW5SV0",
            "y": "SLW_xSffzlPWrHEVI30DHM_4egVwt3NQqeUD7nMFpps",
            "d": "0_NxaRPUMQoAJt50Gz8YiTr8gRTwyEaCumd-MToTmIo"
        }

        u_epk_material = {
            "kty": "EC",
            "crv": "P-256",
            "x": "weNJy2HscCSM6AEDTDg04biOvhFhyyWvOHQfeF_PxMQ",
            "y": "e8lnCO-AlStT-NJVX-crhB7QRYhiix03illJOVAOyck",
            "d": "VEmDZpDXXK8p8N0Cndsxs924q6nS1RXFASRl6BfUqdw"
        }

        # キーマテリアルのフォーマット変換
        import re
        from jose.utils import base64
        _to_pub = lambda km: (
            int(re.search(r"P-(\d+)$", "P-256").group(1)),
            (base64.long_from_b64(km['x']),
             base64.long_from_b64(km['y']))
        )
        _to_pri = lambda km: (
            int(re.search(r"P-(\d+)$", "P-256").group(1)),
            base64.long_from_b64(km['d'])
        )

        # Party V(受け取り側)の永続キーと、PartyU(送信側)の一時キーの作成
        from ecc.Key import Key
        v_stc = Key(
            public_key=_to_pub(v_stc_material),
            private_key=_to_pri(v_stc_material)
        )
        # 公開鍵として PartyUに渡す
        v_pub = Key.decode(v_stc.encode())

        u_epk = Key(
            public_key=_to_pub(u_epk_material),
            private_key=_to_pri(u_epk_material)
        )

# NIST の楕円曲線パラメータ #


        # NISTが定めたカーブパラメータ: Getting NIST Curve
        from ecc.curves import get_curve
        from ecc.elliptic import mulp

        _curve = lambda bits:  dict(
            zip(('bits', 'p', 'N', 'a', 'b', 'G'),
                get_curve(bits)))

        u_crv = _curve(u_epk._priv[0])

# ECDH : ２つの鍵の互いの公開鍵、秘密鍵でDiffie-Hellmanしてシークレットを共有#

生成した一時秘密鍵と送り先の公開されている永続公開鍵で:


        # ECDH : 
        _dhZ = lambda crv, pub, pri: mulp(
            crv['a'], crv['b'], crv['p'], pub, pri)[0]

        # 送り側のシークレット計算
        shared_secret_u = _dhZ(u_crv, v_pub._pub[1], u_epk._priv[1])

        from Crypto.Util.number import long_to_bytes
        from math import ceil

        # ブロックサイズでバイト列化
        block_size = int(ceil(u_epk._priv[0] / 8.0))
        
        Zu = long_to_bytes(shared_secret_u, block_size)

        Z_jwa = [158, 86, 217, 29, 129, 113, 53,
                 211, 114, 131, 66, 131, 191, 132,
                 38, 156, 251, 49, 110, 163, 218,
                 128, 106, 72, 246, 218, 167, 121,
                 140, 254, 144, 196]

        # スペックと確認: OK
        self.assertEqual([ord(i) for i in Zu], Z_jwa)

## パーティ情報 ##

        # パーティ情報の生成:saltみたいなもの
        # Other Information used in Concat KDF
        # AlgorithmID || PartyUInfo || PartyVInfo || SuppPubInfo
        from struct import pack
        _otherInfo = lambda alg, pu, pv, klen: ''.join([
            pack("!I", len(alg)),
            alg,
            pack("!I", len(pu)),
            pu,
            pack("!I", len(pv)),
            pv,
            pack("!I", klen),
        ])

        oi_u = _otherInfo(
            "A128GCM",
            "Alice",
            "Bob",
            16 * 8,     # A128GCM
        )

        oi_jwa = [
            0, 0, 0, 7,
            65, 49, 50, 56, 71, 67, 77,
            0, 0, 0, 5,
            65, 108, 105, 99, 101,
            0, 0, 0, 3,
            66, 111, 98,
            0, 0, 0, 128]

        # スペックと確認: OK
        self.assertEqual([ord(i) for i in oi_u], oi_jwa)

## Concat KDF: 共有キーを派生 ##

        # Concat KDF : NIST SP-800-56a 5.8.1
        # この関数にパーティ情報と、シークレットを渡してキーを派生します
        from Crypto.Hash import SHA256

        def _ConcatKDF(Z, dkLen, otherInfo,
                       digest_method=SHA256):
            _src = lambda counter_bytes: "".join([
                counter_bytes, Z, otherInfo])

            from math import ceil
            from struct import pack

            dkm = b''   # Derived Key Material
            counter = 0
            klen = int(ceil(dkLen / 8.0))
            while len(dkm) < klen:
                counter += 1
                counter_b = pack("!I", counter)
                dkm += digest_method.new(_src(counter_b)).digest()

            return dkm[:klen]

        _derived_key_u = _ConcatKDF(Zu, 16 * 8, oi_u)


# 受け取り側も同じように派生させる #

もらった一時公開鍵と自分の永続秘密鍵で:


        # Party V : 一時公開鍵をもらいます
        v_epk = Key.decode(u_epk.encode())
        Zv = long_to_bytes(
            _dhZ(u_crv, v_epk._pub[1], v_stc._priv[1]),
            block_size)

        _derived_key_v = _ConcatKDF(Zv, 16 * 8, oi_u)

        self.assertEqual(_derived_key_u, _derived_key_v)

        kd_jwa = [
            86, 170, 141, 234, 248, 35, 109, 32,
            92, 34, 40, 205, 113, 167, 16, 26]

        # スペックと確認: OK
        self.assertEqual([ord(i) for i in _derived_key_u], kd_jwa)
        self.assertEqual("VqqN6vgjbSBcIijNcacQGg",
                         base64.base64url_encode(_derived_key_u))
