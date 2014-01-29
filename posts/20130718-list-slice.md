Date: 2013-07-18  
Title: C#: Pythonのlistのスライス的なもの
Type: post  
Excerpt:   


拡張メソッド :

    public static class Extends
    {
        public static byte[] Slice(this byte[] org,int start,  int end = int.MaxValue )
        {
            if (end < 0)
            {
                end = org.Length + end;
            }
            start = Math.Max(0, start);
            end = Math.Max(start, end);

            return org.Skip(start).Take(end - start).ToArray();

        }
    }

テスト:

            var org = new byte[]{0,1,2,3,4,5,6,7,8,9};


            Assert.IsTrue(org.Slice(3, 6).SequenceEqual(new byte[] { 3, 4, 5 }));
            Assert.IsTrue(org.Slice(3, -1).SequenceEqual(new byte[] { 3, 4, 5,6,7,8 }));
            Assert.IsTrue(org.Slice(3, 3).SequenceEqual(new byte[]{}));
            Assert.IsTrue(org.Slice(0, 1).SequenceEqual(new byte[] {0 }));
            Assert.IsTrue(org.Slice(4, 2).SequenceEqual(new byte[] { }));
            Assert.IsTrue(org.Slice(8).SequenceEqual(new byte[]{8,9} ));
            // ちょっとPythonとは変えてる
            Assert.IsTrue(org.Slice(-1, 2).SequenceEqual(org.Slice(0, 2)));
    