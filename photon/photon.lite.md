# Lite

## Liteデータモデル

### Peers

- 接続中のプレイヤーのこと
- LitePeerクラス

#### 新規作成

- LiteApplication.CreatePeer


### RoomReference

- LitePeerにひも付けられたステート
- プレイヤーは**同時に１つのroomにしか**入ることができません
- Joinで設定される

### Room

- Room == "対戦"
- 固有のネーム
- プレイヤーリスト(Join, Leave, Disconnect)
- プレイヤー間のイベント通信


### Actor

- Room中のプレーヤー
- ActorNumber


## Operation & Event

### Operation

#### 入室退室

- Join :ネームを指定してroomに入る操作。Roomが存在しなければその時に作成されます。プレイヤーが別のroomに居た場合、Join操作で自動的にそのroomも同時に退室します。そこでのActorNumberも返されます。

- Leave: roomを退室する操作。（但し、接続は維持されます）。

#### イベント

- RaiseEvent: room内にいる他のpeerにイベントを送るようroomに指示します。イベントにはEventCodeがあり、そのコードはクライアントからのデータを運ぶことができます。Liteではイベントは保存されません。

- 位置を教えるクライアント

~~~
// プレイヤ(peer)のポジションを教えます
internal void SendEvMove(LitePeer peer)
{
    if (peer == null)
    {
        return;
    }
 
    Hashtable evInfo = new Hashtable();
 
    evInfo.Add((byte)STATUS_PLAYER_POS_X, (byte)this.posX);
    evInfo.Add((byte)STATUS_PLAYER_POS_Y, (byte)this.posY);
        
    peer.OpRaiseEvent(
    	EV_MOVE, 				// イベントコード(byte)
    	evInfo, 				// イベントデータ(Hashtable)
    	isSendReliable, 		// 信頼性通信?(bool)
    	(byte)0, 				// チャネルID(byte)
    	Game.RaiseEncrypted	// 暗号化?(bool)
    );
}
~~~

- 受け取ったクライアント側

~~~
//in Game.cs:
public void EventAction(byte eventCode, Hashtable photonEvent)
{
    int actorNr = 0;
    if (photonEvent.ContainsKey((byte)LiteEventKey.ActorNr))
    {
        actorNr = (int) photonEvent[(byte) LiteEventKey.ActorNr];
    }
 
    // get the player that raised this event
    Player p;
    this.Players.TryGetValue(actorNr, out p);
 
    switch (eventCode)
    {
        case Player.EV_MOVE:
            p.SetPosition((Hashtable)photonEvent[(byte)LiteEventKey.Data]);
            break;
        //[...]
    }
}
 
//in Player.cs:
internal void SetPosition(Hashtable evData)
{
    this.posX = (byte)evData[(byte)STATUS_PLAYER_POS_X];
    this.posY = (byte)evData[(byte)STATUS_PLAYER_POS_Y];
}
~~~

#### 属性

- プレイヤーが設定し、また、取得できるハッシュテーブル
- 常に actor または room に関連付けられています
- Join は room が新しい場合にだけ値を設定します。(あとでルームの属性を変えられると困るから)

- GetProperties: Liteでは、roomやプレイヤーにプロパティを付けることができます。この操作でプロパティをフェッチします。
- SetProperties: 一つのroomまたは一人のプレイヤーに無作為なキー／値のペアを付ける操作。Liteはデータを使わないので、クライアントは無作為なデータを一緒に送ることができます。設定より規約のパラダイムです。


### Event

- Join: （操作で）roomに入室すると、その中に居るプレイヤーのリストがアップデートされます。これはイベントとして（新しいプレイヤーを含み）プレイヤー全員に送信されます。
- Leave: プレイヤーがroomを退室する時も、他のプレイヤー全員にアップデート情報が送信されます。
- Properties update: プロパティが変更された時、その変更をブロードキャストするオプションがあります。これはクライアントそれぞれに最新の情報を確実に伝えるイベントです。


