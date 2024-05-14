#!/usr/bin/env python
"""
env $(cat .env|xargs) kb_lc.py query 山田太郎の年齢を教えてください
"""
import os
import boto3
import click
from langchain.chains import RetrievalQA
from langchain_community.chat_models import BedrockChat
from langchain_community.retrievers import AmazonKnowledgeBasesRetriever


def create_client(region_name=None):
    region_name = region_name or os.environ["AWS_REGION"]
    bedrock_client = boto3.client("bedrock-runtime", region_name=region_name)
    return bedrock_client


def create_llm(bedrock_client=None, model_version_id=None, region_name=None):
    bedrock_client = bedrock_client or create_client(region_name=region_name)
    model_version_id = model_version_id or os.environ["LLM_MODEL_ID"]
    bedrock_llm = BedrockChat(
        model_id=model_version_id,
        client=bedrock_client,
        model_kwargs={"temperature": 0},
    )
    return bedrock_llm


def create_retriever(knowledge_base_id=None):
    knowledge_base_id = knowledge_base_id or os.environ["BEDROCK_KB_ID"]
    retriever = AmazonKnowledgeBasesRetriever(
        knowledge_base_id=knowledge_base_id,
        retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 4}},
    )
    return retriever


@click.group()
@click.pass_context
def bedrock(ctx):
    ctx.ensure_object(dict)
    ctx.obj["AWS_REGION"] = os.environ["AWS_REGION"]
    ctx.obj["BEDROCK_KB_ID"] = os.environ["BEDROCK_KB_ID"]  #
    ctx.obj["LLM_MODEL_ID"] = os.environ[
        "LLM_MODEL_ID"
    ]  # "anthropic.claude-3-sonnet-20240229-v1:0"


@bedrock.command()
@click.argument("question")  # 山田太郎って何歳?
@click.pass_context
def query(ctx, question):
    """問い合わせ"""

    llm = create_llm(
        model_version_id=ctx.obj["LLM_MODEL_ID"], region_name=ctx.obj["AWS_REGION"]
    )
    retriever = create_retriever(knowledge_base_id=ctx.obj["BEDROCK_KB_ID"])

    qa = RetrievalQA.from_chain_type(
        llm=llm, retriever=retriever, return_source_documents=True
    )

    response = qa(question)

    query = response.get("query", None)
    result = response.get("result", None)
    source = "\n".join(
        map(lambda d: d.page_content, response.get("source_documents", []))
    )

    print(query)
    print(result)
    print(source)


if __name__ == "__main__":
    bedrock()
