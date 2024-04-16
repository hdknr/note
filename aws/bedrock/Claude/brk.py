"""
AWS_PROFILE=yourprofile  AWS_REGION=us-west-2 python brk.py desc-image ~/Downloads/gallery-img-01.jpg
"""

import click
import boto3
import base64
import json
import os

client = boto3.client("bedrock-runtime", region_name=os.environ["AWS_REGION"])

MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"
ANSHROPIC = "bedrock-2023-05-31"


def create_image_query(path, prompt=None):
    prompt = prompt or "What is in this image?"

    with open(path, "rb") as image_file:
        image_bytes = image_file.read()
        encoded_image = base64.b64encode(image_bytes).decode("utf-8")

    params = {
        "anthropic_version": ANSHROPIC,
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": encoded_image,
                        },
                    },
                    {"type": "text", "text": prompt},
                ],
            }
        ],
    }
    return params


@click.group()
@click.pass_context
def bedrock(ctx):
    pass


@bedrock.command()
@click.argument("path")
@click.pass_context
def desc_image(ctx, path):

    query = create_image_query(path)
    body = json.dumps(query)
    response = client.invoke_model(modelId=MODEL_ID, body=body)
    response_body = json.loads(response.get("body").read())
    print(json.dumps(response_body, indent=2))


if __name__ == "__main__":
    bedrock()
