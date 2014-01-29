Date: 2013-07-18  07:00
Title:   C#: 整数のOctet String 表現
Type: post  
Excerpt: 


拡張メソッド(Extension Methods)を定義:

    public static class Extends
    {
        public static byte[] ToOctetString(this ulong value)
        {
            var ret = BitConverter.GetBytes(value);
            if (BitConverter.IsLittleEndian)
                Array.Reverse(ret);

            return ret;

        }
    }

テスト:

            foreach (var i in new int[] { 1,2,3,4,5,6,7,8})
            {
                ulong v = (ulong)Math.Pow(256, i) - 1;
                Console.WriteLine("{0}=>{1}",
                    v,BitConverter.ToString( v.ToOctetString()) );
            }


結果:

    255=>00-00-00-00-00-00-00-FF
    65535=>00-00-00-00-00-00-FF-FF
    16777215=>00-00-00-00-00-FF-FF-FF
    4294967295=>00-00-00-00-FF-FF-FF-FF
    1099511627775=>00-00-00-FF-FF-FF-FF-FF
    281474976710655=>00-00-FF-FF-FF-FF-FF-FF
    72057594037927935=>00-FF-FF-FF-FF-FF-FF-FF
    18446744073709551615=>FF-FF-FF-FF-FF-FF-FF-FF
    
     

