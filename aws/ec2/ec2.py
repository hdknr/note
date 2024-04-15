import click
import boto3
from itertools import chain


client = boto3.client("ec2")
resource = boto3.resource("ec2")


@click.group()
@click.pass_context
def ec2(ctx):
    pass


def stop(instance_id, obj=None, force=False):
    """
    stop:
    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/stop.html
    """
    instance = obj or resource.Instance(instance_id)
    instance.stop(Force=force)
    pass


def start(instance_id, obj=None):
    """
    start:
    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/start.html
    """
    instance = obj or resource.Instance(instance_id)
    instance.start()


def restart(instance_id, obj=None, force=False, dry_run=False):
    """
    state:
    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/state.html
    """
    instance = obj or resource.Instance(instance_id)

    state = instance.state

    if not force:
        if state["Code"] == 16:  # running
            print(f"{instance_id} is running: do nothing")
            return
        if state["Code"] == 48:  # terminated
            # AMIから起動
            print(f"{instance_id} is terminated: you must create instance from AMI)")
            return

    if not state["Code"] == 80:  # stopped
        print(f"{instance_id} is not stop: stop this before starting")
        if not dry_run:
            stop(instance_id, obj=obj, force=force)
            instance.wait_until_stopped()

    print(f"{instance_id} stopped: start this")
    if not dry_run:
        start(instance_id, obj=instance)


def restart_instances(instances, force, dry_run):
    """再起動"""
    instances = chain.from_iterable(
        map(lambda i: i["Instances"], instances["Reservations"])
    )
    list(
        map(lambda i: restart(i["InstanceId"], force=force, dry_run=dry_run), instances)
    )


def filter_from_tags(tags):
    tagtuples = map(lambda i: i.split("="), tags)
    return list(map(lambda i: {"Name": f"tag:{i[0]}", "Values": [i[1]]}, tagtuples))


@ec2.command()
@click.argument("instance_id", nargs=-1)
@click.option("--force", "-f", is_flag=True)
@click.option("--dry_run", "-d", is_flag=True)
@click.pass_context
def restart_instance_ids(ctx, instance_id, force, dry_run):
    """
    再起動
    """
    # describe_instances
    # - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instances.html
    res = client.describe_instances(InstanceIds=list(instance_id))
    restart_instances(res, force, dry_run)


@ec2.command()
@click.argument("tags", nargs=-1)
@click.option("--force", "-f", is_flag=True)
@click.option("--dry_run", "-d", is_flag=True)
@click.pass_context
def restart_instances_tags(ctx, tags, force, dry_run):
    # describe_instances
    # - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instances.html
    res = client.describe_instances(Filters=filter_from_tags(tags))
    restart_instances(res, force, True)


if __name__ == "__main__":
    ec2()
