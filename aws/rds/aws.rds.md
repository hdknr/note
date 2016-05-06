# RDSインスタンス作成(ansible)

- ansible RDS作成タスク

~~~yaml
---
# http://docs.ansible.com/ansible/rds_module.html
- name: Create a RDS instance
  rds: >
      command=create
      instance_name={{ db_name }}
      username={{ db_user }}
      password={{ db_password }}
      db_name={{ db_name }}
      aws_access_key="{{ lookup('env','AWS_ACCESS_KEY_ID') }}"
      aws_secret_key="{{ lookup('env','AWS_SECRET_ACCESS_KEY') }}"
      zone="{{ aws_zone }}"
      region="{{ aws_region }}"
      vpc_security_groups="{{ rds_vpc_security_groups }}"
      db_engine=postgres
      instance_type="{{ rds_instance }}"
      size="{{ rds_size }}"
      wait=yes
      wait_timeout=600
  register: rds_info
  tags: rds
~~~

- ansible playbook
- VPCセキュリティグループができていること

~~~yaml
---
- hosts: localhost
  vars:
    db_name: tactgresdb
    db_user: tactgresuser
    db_password: tactgrespwd
    aws_zone: ap-northeast-1c
    aws_region: ap-northeast-1
    rds_vpc_security_groups: sg-14808171
    rds_instance: db.t1.micro        
    rds_size: 20
  roles:
    - role: ec2_rds
~~~

- めんどくさいので同じセキュリティグループ(sg-14808171)内のサーバーからアクセスできるようにしておく

~~~bash
$ aws ec2 describe-security-groups --group-names development | jq ".SecurityGroups[].IpPermissions[1]"

{
  "PrefixListIds": [],
  "FromPort": 5432,
  "IpRanges": [],
  "ToPort": 5432,
  "IpProtocol": "tcp",
  "UserIdGroupPairs": [
    {
      "UserId": "757103751050",
      "GroupId": "sg-14808171"
    }
  ]
}
~~~

# ubuntu

~~~bash
$ sudo apt-get install postgresql-client
~~~

~~~bash
$ psql -h tactgresdb.cius0pombyrd.ap-northeast-1.rds.amazonaws.com tactgresdb tactgresuser
Password for user tactgresuser:
psql (9.3.10, server 9.4.5)
WARNING: psql major version 9.3, server major version 9.4.
         Some psql features might not work.
SSL connection (cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256)
Type "help" for help.

tactgresdb=> \q
~~~


# マルチAZ

- [Multi-AZの役割](http://macotasu.hatenablog.jp/entry/2015/07/09/231312)
- [AWSのMultiAZについて調べたので残しておく](http://natural-hokke.hateblo.jp/entry/2014/10/24/133205)

![](http://cdn-ak.f.st-hatena.com/images/fotolife/M/Maco_Tasu/20150709/20150709223107.png)

- フェールオーバー時にもエンドポイントが変わらない(再接続で済む)
- AZ間の通信には（同一リージョンであっても）1G/$0.01かかる点には注意しなければならない。
- 2インスタンス使うため料金は倍掛かる。


# awscli

## DBインスタンス(describe-db-instances)

- [describe-db-instances](http://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html)

~~~bash
$ aws rds describe-db-instances --profile ictact |  ¥
jq ".DBInstances[]|[.DBInstanceIdentifier, .DBName, .MasterUsername,  .AvailabilityZone, .AllocatedStorage, .VpcSecurityGroups[].VpcSecurityGroupId, .DBParameterGroups[].DBParameterGroupName ]" -c   
~~~

~~~
["stagingdb","appdb","appuser","ap-northeast-1c",5,"sg-19808171","default.postgres9.3"]
["livedb","appdb","appuser","ap-northeast-1c",50,"sg-19808171","default.postgres9.3"]
~~~
