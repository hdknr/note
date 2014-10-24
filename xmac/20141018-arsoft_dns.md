ARSoft.Tools.Net: Xamarin.Mac/iOSで動かしてみる


# Socket is already connected


~~~csharp
		public void AssertGoogle(DnsMessage msg)
		{
			Assert.IsNotNull (msg);
			Assert.IsTrue (msg.AnswerRecords.Count > 0);
			Assert.AreEqual( 
				173,
				(msg.AnswerRecords[0] as ARecord).Address.GetAddressBytes()[0]
			);
		}
~~~

~~~ csharp

		[Test]
		public void TestResolve ()
		{
			AssertGoogle (
				DnsClient.Default.Resolve (
					"google.com", RecordType.A)
			);
		}
~~~
		
結果が返らない。ブレークポイント入れるとSocket is already connectedで例外起きている。

ので、DnsClientBase.csを修正:

~~~ csharp

private byte[] QueryByUdp(DnsClientEndpointInfo endpointInfo, byte[] messageData, int messageLength, out IPAddress responderAddress)
{
  ....
                    if( udpClient.Connected )
                        udpClient.Send(messageData);
                    else 
                        udpClient.SendTo(messageData, messageLength, SocketFlags.None, serverEndpoint);


~~~

# BeginResolve でも同じ

~~~ csharp

		[Test]
		public void TestResolveAsync()
		{
			DnsClient.Default.BeginResolve (
				"google.com", 
				ar => {
					AssertGoogle (
						DnsClient.Default.EndSendMessage (ar)
					);
				}, null);
		}
~~~

で結果がかえらないので、同様に修正:

~~~ csharp

        private void UdpBeginSend<TMessage>(DnsClientAsyncState<TMessage> state)
            where TMessage : DnsMessageBase, new()
        {
                 ....
                IAsyncResult asyncResult;
                if( state.UdpClient.Connected == true){
                    asyncResult = state.UdpClient.BeginSend(
                        state.QueryData, 0, state.QueryLength, 
                        SocketFlags.None,  UdpSendCompleted<TMessage>, state);
                }else {
                    asyncResult = state.UdpClient.BeginSendTo(
                        state.QueryData, 0, state.QueryLength, 
                        SocketFlags.None, state.UdpEndpoint, UdpSendCompleted<TMessage>, state);
                }
~~~


#  NSサーバー指定してAレコードのクエリ

~~~ csharp

		public List<System.Net.IPAddress>	ResolveAddress(
			DnsClient dns, string name, int timeout=50000 )
		{
			var msg = dns.Resolve (name);

			var addrs = msg.AnswerRecords
				.Where (a => a.RecordType == RecordType.A)
				.Select (a => ((ARecord)a).Address).ToList ();

			foreach(CNameRecord rec 
				in msg.AnswerRecords.Where( a => a.RecordType == RecordType.CName))
			{
				addrs = addrs.Concat(ResolveAddress(dns, rec.CanonicalName )).ToList();
			}

			return addrs.Distinct ().ToList ();
		}
~~~

~~~ csharp

		[Test]
		public void TestResolveByGoogle()
		{
			var google = new System.Net.IPAddress (new byte[4]{ 8, 8, 8, 8 });

			var addrs = ResolveAddress (
				            new DnsClient (google, 3000), 
				            "www.microsoft.com");

        }
~~~

                     
