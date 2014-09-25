Touch ID: プライベートキーをTouch IDプロテクトする

アプリのマスターキーをJwkSetで管理したい


# SecKind.GenericPassword で保存する

- どうも SecKind.Key だと うまく行かない

~~~csharp

		const SecKind KIND =  SecKind.GenericPassword;
		public static readonly string SERVICE_NAME = "Auth.Touch";
~~~

#  マスターキーが存在したら削除する
- KeyChain Itemのクエリレコード

~~~ csharp

		static readonly SecRecord KEYCHAIN_QUERY = new SecRecord (KIND) { 	
			Service = SERVICE_NAME,
			UseOperationPrompt = "Authenticate yourself.",
		};
~~~

- 指定したKeyChain Itemを削除する

~~~ csharp

		public override void Delete ()
		{
			Evaluate (SecKeyChain.Remove (KEYCHAIN_QUERY));
		}
~~~

- Success以外だと例外を出す

~~~ csharp

		public static void Evaluate(SecStatusCode  code){
			if (code != SecStatusCode.Success) {
				throw new KeyChainException (code);
			}		
		}
~~~			



# JOSE JwkSetをシリアライズして入れてみる

- JwkSet をシリアライズして、 SecRecordの Genericにぶち込む
- コメントにあるようにTouch IDで守りたいのであれば、SecAccessControll を設定する
- AccessControlを指定しないと、Touch IDのプロンプトでません

~~~ csharp

		public static SecRecord ToKeyChainItem (
			Jose.JwkSet jwkset, 
			SecAccessControl grant)
		{
			// if AccessControl is not specified,
			// this security record is not protected by TouchID 
			
			return new SecRecord (KIND) {
				Service = SERVICE_NAME,
				Generic =  NSData.FromString(jwkset.ToJson()),
				UseNoAuthenticationUI = true,
				AccessControl=grant,
			};			
		}
~~~		

- Touch ID 用のAccess Controlは以下で渡す事にします

~~~csharp

		static readonly SecAccessControl GRANT = new SecAccessControl (
			                                         SecAccessible.WhenPasscodeSetThisDeviceOnly,
			                                         SecAccessControlCreateFlags.UserPresence);

~~~

- 作成。Deleteの例外はItemNotFoundの場合、無視する。

~~~ csharp

		public override Jose.JwkSet Create ()
		{
			try{
				this.Delete ();
			}catch(KeyChainException ex) {
				if (ex.Code != SecStatusCode.ItemNotFound)
					throw ex;
			}
			return this.Add (CreateJwkSet());
		}
~~~		

- Add

~~~csharp

		public Jose.JwkSet Add(Jose.JwkSet jwkset)
		{
			var kci = ToKeyChainItem(jwkset, GRANT);
			Evaluate (SecKeyChain.Add (kci));

			return jwkset;
		}
~~~


- JwkSetはEC521で

~~~ csharp

		public static Jose.JwkSet CreateJwkSet()
		{
			var jwk = Jose.Jwa.KeyDef.EC.GenerateKey (Jose.Jwa.Ec.CurveEnum.P_521);
			jwk.kid = DateTime.Now.ToString ();	// for TEST

			return new Jose.JwkSet () {
				keys = new System.Collections.Generic.List<Jose.Jwk>{ jwk }
			};
		}
~~~

# 参照する

- Deleteを同じKeyChain Itemをレコードして探す
- みつかったらJwkSetに復元する
 
~~~ csharp

		public override Jose.JwkSet Load ()
		{
			SecStatusCode code;                

			SecRecord resultData = SecKeyChain.QueryAsRecord (
				KEYCHAIN_QUERY, out code);
			Evaluate(code);
			return ToJwkSet(resultData.Generic);
		}
~~~		


# 動かす

- 起動

![image](https://lh4.googleusercontent.com/-yBCyn24OBwE/VCOyrAZ82vI/AAAAAAAAA3Q/74FitGcZok0/w309-h548-no/1.%2BStart.png)

- 空で削除すると例外


![image](https://lh5.googleusercontent.com/-sZrQ42Lguuk/VCOyrNhRZnI/AAAAAAAAA24/efuTZHt_16E/w309-h548-no/2.%2BDelete%2BFails.png)

- 新規作成　 & 保存


![image](https://lh6.googleusercontent.com/-82QGS3IILrY/VCOyrUuFETI/AAAAAAAAA3A/dKtS0LeP9kU/w309-h548-no/3.%2BKey%2BGenerated%2Band%2BStored.png)

- Browse すると Touch ID 認証

![image](https://lh6.googleusercontent.com/-dD8q5ESBXbs/VCOyr9QT-kI/AAAAAAAAA3M/-hf-ThMl7nU/w309-h548-no/4.%2BTouch%2BID%2Bprotects%2Ban%2Baccess.png)

- 認証が通ると表示

![image](https://lh4.googleusercontent.com/-qhbpNrZy6Jk/VCOysBTcGGI/AAAAAAAAA3U/i0rzbRdJUY4/w309-h548-no/5.%2BShow%2BJwkSet%2Bif%2Bverified.png)

- ちなみに“Enter Passcord”でパスコード認証も通ります

![image](https://lh6.googleusercontent.com/-MJMgKsP-5SM/VCOysrYExBI/AAAAAAAAA3Y/ZAz5CA9Sxac/w309-h548-no/6.%2BPassword%2Balso%2Bworks.png)
	
	
# SecKind.Keyだとうまく行かない

- Touch ID を使わないと以下のコードで SecKind.Keyで保存できるが、 Touch IDプロテクトすると Param エラー

~~~ csharp


			SecStatusCode code = SecKeyChain.Add ( new SecRecord ( SecKind.Key ) {
				Service = _service_name,
				Label = _service_name,
				Account = _account_name,
				Generic = NSData.FromString ( jwkset.ToJson(), NSStringEncoding.UTF8 ),
				Accessible = accessible,
				Synchronizable = sync
			} );
~~~			

- どのParamでエラーなのかがよくわからん
