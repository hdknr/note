## Photon Server

- [Photon Serverイントロ](http://doc.exitgames.com/ja/onpremise/current/getting-started/photon-server-intro)

### SDK

- Lite: シンプルでパワフルなルームベースのゲームロジック、
- Lite Lobby: ロビー機能とルームロジック、
- Policy: Unity3d, FlashとSilverlight用のPolicy server
- LoadBalancing: サーバに渡りロードバランスされたスケーリングを実現 - これがPhoton Cloudにパワーを与えています。

![](http://doc.exitgames.com/Docs/img/photon-server-architecture.png)

レイヤー

- Photon Core (C/C++)
- Business Logic (C#)

プロトコル

- 信頼性のあるUDP (eNETに基づく)でClient-2-Server構造に特化しています
- Binary TCP
- Web Sockets
- HTTP

