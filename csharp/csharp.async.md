	## Task.Run


~~~csharp

public virtual void Load(){

		Task.Run (async () => {
				var file = await FileSystem.Current.LocalStorage.GetFileAsync (_cache);
				var json = await file.ReadAllTextAsync ();
				this._data = JObject.Parse (json);
		});
}
~~~


あるいは

~~~csharp

public virtual void Load(){

		Task.Run (() => {
				this._data = Load<User>("user1").Result;
		});
}

public async Task<T> Load(string key) {
	return
		await  DataBase.Load<T>(key);
}
~~~

## Task.Facory.StartNew

~~~csharp

public virtual void Load(){
    Task.Factory.StartNew (async () => {
      try {
        var file = await FileSystem.Current.LocalStorage.GetFileAsync (_cache);
        var json = await file.ReadAllTextAsync ();
        this._data = JObject.Parse (json);
      } catch {
      }
    }).Wait ();
}
~~~


## Job Queue

- http://d.hatena.ne.jp/rti7743/20100612/1276375504
