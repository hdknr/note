Python: Jose ECDHの共有シークレットのアグリーメント

キーの派生をしていいないので、「Key Agreement」にはなっていなですが、Diffie-Hellmanまでは確認:

    def test_dhZ(self):
        from ecc.Key import Key 

        # Party V(recepient) declares a satic key pair
        curve_bits = 521 
        v_stc = Key.generate(curve_bits)

        # and advertise to Party U(Sender)
        v_pub = Key.decode(v_stc.encode())

        # Party U provides a ephemeral key
        u_epk = Key.generate(v_pub._pub[0])

        # Getting NIST Curve
        from ecc.curves import get_curve
        from ecc.elliptic import mulp

        _curve = lambda bits:  dict(
            zip(('bits', 'p', 'N', 'a', 'b', 'G'),
                get_curve(bits)))
        # Compute ECDH
        _dhZ = lambda crv, pub, pri: mulp(
            crv['a'], crv['b'], crv['p'], pub, pri)[0]

        # Party U compute
        u_crv = _curve(u_epk._priv[0])
        shared_secret_u = _dhZ(u_crv, v_pub._pub[1], u_epk._priv[1])

        # Party V recive Epemeral Public Key
        v_epk = Key.decode(u_epk.encode())
        # Party V compute
        shared_secret_v = _dhZ(u_crv, v_epk._pub[1], v_stc._priv[1])

        # Secrete Agreeed!
        self.assertEqual(shared_secret_u, shared_secret_v)