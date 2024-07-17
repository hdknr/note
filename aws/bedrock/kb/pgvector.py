#!/usr/bin/env python
import json
import os

import boto3
import click


def setup_boto3():
    keys = {"profile_name": "AWS_PROFILE", "region_name": "AWS_REGION"}
    params = dict((k, os.environ[v]) for k, v in keys.items() if v in os.environ)
    boto3.setup_default_session(**params)


def get_sm_clinet():
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html
    return boto3.client("secretsmanager")


def get_rds_ds_client():
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html
    return boto3.client("rds-data")


def get_rds_clint():
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html
    return boto3.client("rds")


def get_secret_arn(name):
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager/client/list_secrets.html
    client = get_sm_clinet()
    values = client.list_secrets(Filters=[dict(Key="name", Values=[name])])[
        "SecretList"
    ]
    if len(values) == 1:
        return values[0]["ARN"]
    return


def get_secret_value(id, is_json=True):
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager/client/get_secret_value.html
    if not id.startswith("arn"):
        id = get_secret_arn(id)

    if not id:
        return

    client = get_sm_clinet()
    value = client.get_secret_value(SecretId=id)["SecretString"]
    if is_json and value:
        return json.loads(value)
    return value


def get_rds_cluster_arn(identfire):
    client = get_rds_clint()
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds/client/describe_db_clusters.html
    values = client.describe_db_clusters(
        DBClusterIdentifier=os.environ["KB_DATABASE_CLUSTER"]
    )["DBClusters"]
    if len(values) == 1:
        return values[0]["DBClusterArn"]


def execute_statement(clusterArn, secretArn, sql, database):
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data/client/execute_statement.html

    if not clusterArn.startswith("arn"):
        clusterArn = get_rds_cluster_arn(clusterArn)
        if not clusterArn:
            return {"failed": "no clusterArn"}

    if not secretArn.startswith("arn"):
        secretArn = get_secret_arn(secretArn)
        if not secretArn:
            return {"failed": "no secretArn"}

    client = get_rds_ds_client()
    return client.execute_statement(
        resourceArn=clusterArn, secretArn=secretArn, sql=sql, database=database
    )


def execute_sql(sql):
    return execute_statement(
        os.environ["KB_DATABASE_CLUSTER"],
        os.environ["KB_DATABASE_SECRET_MASTERUSER"],
        sql,
        os.environ["KB_DATABASE_NAME"],
    )


@click.group()
@click.pass_context
def group(ctx):
    setup_boto3()
    pass


@group.command()
@click.pass_context
def setup_vector(ctx):
    """vector(pgVextro) の設定"""
    sql = """CREATE EXTENSION IF NOT EXISTS vector;"""

    res = execute_sql(sql)
    print(json.dumps(res, indent=2))


@group.command()
@click.pass_context
def create_schema(ctx):
    """スキーマ作成"""
    sql = """CREATE SCHEMA {schema};""".format(schema=os.environ["KB_DATABASE_SCHEMA"])

    res = execute_sql(sql)
    print(json.dumps(res, indent=2))


@group.command()
@click.pass_context
def create_table(ctx):
    """テーブル作成"""
    sql = """
    CREATE TABLE {schema}.{table}(
        id uuid PRIMARY KEY,
        embedding vector(1536),
        categories varchar(256),
        document varchar(256),
        chunks text,
        metadata json);
    """.format(
        schema=os.environ["KB_DATABASE_SCHEMA"],
        table=os.environ["KB_DATABASE_TABLE"],
    )

    res = execute_sql(sql)
    print(json.dumps(res, indent=2))


@group.command()
@click.pass_context
def create_role(ctx):
    """ロール(アクセスユーザー)作成"""
    value = get_secret_value(os.environ["KB_DATABASE_SECRET_USER"])

    sql = """CREATE ROLE {username} WITH PASSWORD '{password}' LOGIN;""".format(**value)
    res = execute_sql(sql)
    print(json.dumps(res, indent=2))


@group.command()
@click.pass_context
def list_role(ctx):
    """ロール(アクセスユーザー)一覧"""
    sql = """ SELECT pg_user.usename FROM pg_user;"""
    res = execute_sql(sql)
    print(json.dumps(res, indent=2))


@group.command()
@click.pass_context
def grant_schema(ctx):
    """スキーマに許可"""
    value = get_secret_value(os.environ["KB_DATABASE_SECRET_USER"])
    sql = """GRANT ALL ON SCHEMA {schema} to {username};""".format(
        schema=os.environ["KB_DATABASE_SCHEMA"], **value
    )
    res = execute_sql(sql)
    print(json.dumps(res, indent=2))


@group.command()
@click.pass_context
def grant_table(ctx):
    """テーブルに許可"""
    value = get_secret_value(os.environ["KB_DATABASE_SECRET_USER"])
    sql = """GRANT ALL ON TABLE {schema}.{table} to {username};""".format(
        schema=os.environ["KB_DATABASE_SCHEMA"],
        table=os.environ["KB_DATABASE_TABLE"],
        **value,
    )
    res = execute_sql(sql)
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    group()
