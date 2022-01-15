# SASL (Simple Authentication and Security Layer)


- [RFC2222: Simple Authentication and Security Layer (SASL)](https://datatracker.ietf.org/doc/html/rfc2222)
- [RFC4422: Simple Authentication and Security Layer (SASL)](https://datatracker.ietf.org/doc/html/rfc4422)
- は認証 (Authentication) のやり取りと認証情報の保護 (Security) に関する仕組みをあらかじめアプリケーションが使いやすいようにプラグインとして用意しているフレームワーク

セキュリティ機能:

1. 通信相手が正しいこと (認証: Authentication)
2. 通信が改竄されていないこと (完全性: Integrity)
3. 通信が盗聴されていないこと (機密性: Confidentiality)


利用可能メカニズム(IANA管理):

- ANNONYMOUS
- GSS-API (=KERBEROS_V5 のこと)
- NTLM
- OAUTH
- OTP
- SAML20
- SECURID

## GSS-API(Generic Security Standard Application Programming Interface)

- アプリケーションの認証方法について、通信プロトコルからの独立性・汎用性を高めるためのフレームワーク
- SPNEGO: Windows Active Directory  でのGSS-API

SASL と GSS-API の違い:

- SASL: 通信プロトコルに依存(SASL はメカニズムを選択するだけ)
- GSS-API: 通信プロトコルに依存しない (各自実装が必要)

## 実装

- [Cyrus SASL](cyrus/README.md) (メジャー)
- [GNU SASL](https://www.gnu.org/software/gsasl/)
- [Dovecot SASL](https://doc.dovecot.org/admin_manual/sasl/)  /  [wiki](https://wiki.dovecot.org/Sasl)

## リンク

- [Wikipedia:Simple Authentication and Security Layer](https://ja.wikipedia.org/wiki/Simple_Authentication_and_Security_Layer)