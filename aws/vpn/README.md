# VPN: Site-to-Site VPN

- VPC <--- (IPSec) --->  オンプレミスネットワーク

## [カテゴリ](https://docs.aws.amazon.com/ja_jp/vpn/latest/s2svpn/vpn-categories.html)

- `AWS VPN 接続`:   新しく作成されるVPN として `AWS Classic VPN 接続` は作成できない
- [接続の識別](https://docs.aws.amazon.com/ja_jp/vpn/latest/s2svpn/identify-vpn.html)

## 概念

| **項目**      | **意味** |
| ------------ | -------- |
| VPN 接続      |  オンプレミス機器と VPC 間の安全な接続。 |
| VPN トンネル   | お客様のネットワークと AWS の間でデータを送受信できる暗号化されたリンク。  各 VPN 接続には、高可用性のために同時に使用できる 2 つの VPN トンネルが含まれています。 |
| カスタマーゲートウェイ    | カスタマーゲートウェイデバイスに関する情報を AWS に提供する AWS リソース。 |
| カスタマーゲートウェイデバイス | Site-to-Site VPN 接続のユーザー側にある物理的なデバイスまたはソフトウェアアプリケーション。 |


## コンポーネント

- 仮想プライベートゲートウェイ
- 転送ゲートウェイ
- カスタマーゲートウェイデバイス
- カスタマーゲートウェイ
