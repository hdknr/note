# 接続

- [FivetranのDestinationにSSHトンネルを介さないとアクセスできないMySQLを追加してみた](https://dev.classmethod.jp/articles/fivetran-ssh-tunnel/)
- [Amazon Aurora MySQL Setup Guide: Connection](https://fivetran.com/docs/databases/mysql/aurora-setup-guide)


AWS接続:

1. TCP直接(TLSは必要)
2. SSH接続(TLSは必要)  (SSHトンネル)
3. [AWS PrivateLink](https://aws.amazon.com/jp/privatelink/?privatelink-blogs.sort-by=item.additionalFields.createdDate&privatelink-blogs.sort-order=desc)

