# AWS Lambda

- [API Gateway](apigw/README.md)
- [SAM: Severless Application Model](sam/README.md)

## Python 3.7

```json
{
  "statusCode": 200,
  "body": {
    "syspath": [
      "/var/task",
      "/opt/python/lib/python3.7/site-packages",
      "/opt/python",
      "/var/runtime",
      "/var/lang/lib/python37.zip",
      "/var/lang/lib/python3.7",
      "/var/lang/lib/python3.7/lib-dynload",
      "/var/lang/lib/python3.7/site-packages",
      "/opt/python/lib/python3.7/site-packages"
    ],
    "pkg_resources": [
      "boto3 1.9.221 /var/runtime",
      "botocore 1.12.221 /var/runtime",
      "docutils 0.15.2 /var/runtime",
      "jmespath 0.9.4 /var/runtime",
      "pip 19.2.3 /var/lang/lib/python3.7/site-packages",
      "python-dateutil 2.8.0 /var/runtime",
      "s3transfer 0.2.1 /var/runtime",
      "setuptools 41.2.0 /var/lang/lib/python3.7/site-packages",
      "six 1.12.0 /var/runtime",
      "urllib3 1.25.3 /var/runtime"
    ]
  }
}
```

- https://pypi.org/project/jmespath/
- https://pypi.org/project/boto3/
- https://pypi.org/project/python-dateutil/
