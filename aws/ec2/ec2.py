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


def restart(instance_id, obj=None, force=False):
    """
    state:
    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/state.html
    """
    instance = obj or resource.Instance(instance_id)

    state = instance.state
    if not force:
        if state["Code"] == 16:  # running
            return
        if state["Code"] == 48:  # terminated
            # AMIから起動
            return

    if not state["Code"] == 80:  # stopped
        # tood start
        stop(instance_id, obj=obj, force=force)
        instance.wait_until_stopped()

    start(instance_id, obj=instance)


@ec2.command()
@click.argument("instance_id", nargs=-1)
@click.option("--force", "-f", is_flag=True)
@click.pass_context
def restart_instances(ctx, instance_id, force):
    res = client.describe_instances(InstanceIds=list(instance_id))
    instances = chain.from_iterable(map(lambda i: i["Instances"], res["Reservations"]))
    list(map(lambda i: restart(i["InstanceId"], force=force), instances))


if __name__ == "__main__":
    ec2()
