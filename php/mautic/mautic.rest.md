# REST API

## 認証

- OAuth2 
- Basic認証  (`設定` > `API Settings` > `Enable API basic auth` == `Yes`)

API設定を変えたらMauticのキャッシュをクリアすること:

~~~bash 
$ rm -rf app/cache/*
~~~

## エンドポイントベース

- `/api`


## コンタクト(リード)


用途　　　　　| REST                                 | Document
-----------| -------------------------------------|----------------------------------------------
詳細        | `GET /api/contacts/{id}`             | https://developer.mautic.org/#get-contact
一覧　　　　　| `GET /api/contacts`                 |  https://developer.mautic.org/#list-contacts 
追加        | `POST /api/contacts/new`             | https://developer.mautic.org/#create-contact
修正　　　　　| `PATCH /api/contacts/{id}/edit`      | https://developer.mautic.org/#edit-contact
修正/追加　　| `PUT /api/contacts/{id}/edit`         | https://developer.mautic.org/#edit-contact
削除        | `DELETE /api/contacts/{id}/delete`    | https://developer.mautic.org/#delete-contact

## セグメント(リードリスト)

セグメント:

用途　　　　　| REST                                 | Document
-----------| -------------------------------------|----------------------------------------------
詳細        | `GET /api/segments/{id}`             | https://developer.mautic.org/#get-segment
一覧　　　　　| `GET /api/segments`                 |  https://developer.mautic.org/#list-contact-segments
追加        | `POST /api/segments/new`             | https://developer.mautic.org/#create-segment
修正　　　　　| `PATCH /api/segments/{id}/edit`      | https://developer.mautic.org/#edit-segment
修正/追加　　| `PUT /api/segments/{id}/edit`         | https://developer.mautic.org/#edit-segment
削除        | `DELETE /api/segments/{id}/delete`    | https://developer.mautic.org/#delete-segment

セグメントコンタクト:

用途   | REST                                           | Document
------| -----------------------------------------------|----------------------------------------------------------------
追加   | `POST /api/segments/{id}/contact/{cid}/add`    | https://developer.mautic.org/#add-contact-to-a-segment
削除   | `POST /api/segments/{id}/contact/{cid}/remove` | https://developer.mautic.org/#remove-contact-from-a-segment


## メール

用途             | REST                                                    | Document
----------------| --------------------------------------------------------|----------------------------------------------------------------
セグメントへ送信   | `POST /api/emails/{id}/send`                            | https://developer.mautic.org/#send-email-to-segment
コンタクトへ送信   | `POST /api/emails/{id}/contact/{cid]/send`              | https://developer.mautic.org/#send-email-to-contact