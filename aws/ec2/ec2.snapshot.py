#!/usr/bin/env python
import os
import click
import boto3

import json

client = boto3.client("ec2")
resource = boto3.resource("ec2")


def setup_boto3():
    keys = {"profile_name": "AWS_PROFILE", "region_name": "AWS_REGION"}
    params = dict((k, os.environ[v]) for k, v in keys.items() if v in os.environ)
    boto3.setup_default_session(**params)


@click.group()
@click.pass_context
def ec2(ctx):
    setup_boto3()


@ec2.command()
@click.pass_context
def remove_all(ctx):
    """不要なスナップショットの削除"""

    def _get_snapshotid(image):
        return image["BlockDeviceMappings"][0]["Ebs"]["SnapshotId"]

    response = client.describe_images(Owners=["self"])
    snapsho_ids = list(map(_get_snapshotid, response["Images"]))

    def _remove_snapshot(snapshot):
        SnapshotId = snapshot["SnapshotId"]
        if SnapshotId not in snapsho_ids:
            client.delete_snapshot(SnapshotId=SnapshotId)

    cond = {
        "Name": "description",
        "Values": [
            "Created by CreateImage*",
        ],
    }
    response = client.describe_snapshots(OwnerIds=["self"], Filters=[cond])
    list(map(_remove_snapshot, response["Snapshots"]))


if __name__ == "__main__":
    ec2()
