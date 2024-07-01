# sam init

```txt
% sam init

You can preselect a particular runtime or package type when using the `sam init` experience.
Call `sam init --help` to learn more.

Which template source would you like to use?
        1 - AWS Quick Start Templates
        2 - Custom Template Location
Choice: 1

Choose an AWS Quick Start application template
        1 - Hello World Example
        2 - Data processing
        3 - Hello World Example with Powertools for AWS Lambda
        4 - Multi-step workflow
        5 - Scheduled task
        6 - Standalone function
        7 - Serverless API
        8 - Infrastructure event management
        9 - Lambda Response Streaming
        10 - Serverless Connector Hello World Example
        11 - Multi-step workflow with Connectors
        12 - GraphQLApi Hello World Example
        13 - Full Stack
        14 - Lambda EFS example
        15 - DynamoDB Example
        16 - Machine Learning
Template: 1

Use the most popular runtime and package type? (Python and zip) [y/N]: n

Which runtime would you like to use?
        1 - aot.dotnet7 (provided.al2)
        2 - dotnet8
        3 - dotnet6
        4 - go (provided.al2)
        5 - go (provided.al2023)
        6 - graalvm.java11 (provided.al2)
        7 - graalvm.java17 (provided.al2)
        8 - java21
        9 - java17
        10 - java11
        11 - java8.al2
        12 - nodejs20.x
        13 - nodejs18.x
        14 - nodejs16.x
        15 - python3.9
        16 - python3.8
        17 - python3.12
        18 - python3.11
        19 - python3.10
        20 - ruby3.3
        21 - ruby3.2
        22 - rust (provided.al2)
        23 - rust (provided.al2023)
Runtime: 17

What package type would you like to use?
        1 - Zip
        2 - Image
Package type: 2

Based on your selections, the only dependency manager available is pip.
We will proceed copying the template using pip.

Would you like to enable X-Ray tracing on the function(s) in your application?  [y/N]: n

Would you like to enable monitoring using CloudWatch Application Insights?
For more info, please view https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html [y/N]: n

Would you like to set Structured Logging in JSON format on your Lambda functions?  [y/N]: y
Structured Logging in JSON format might incur an additional cost. View https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html#monitoring-cloudwatchlogs-pricing for more details

Project name [sam-app]: aicti

Cloning from https://github.com/aws/aws-sam-cli-app-templates (process may take a moment)

    -----------------------
    Generating application:
    -----------------------
    Name: aicti
    Base Image: amazon/python3.12-base
    Architectures: x86_64
    Dependency Manager: pip
    Output Directory: .
    Configuration file: aicti/samconfig.toml

    Next steps can be found in the README file at aicti/README.md


Commands you can use next
=========================
[*] Create pipeline: cd aicti && sam pipeline init --bootstrap
[*] Validate SAM template: cd aicti && sam validate
[*] Test Function in the Cloud: cd aicti && sam sync --stack-name {stack-name} --watch

Error: An error occurred while generating this project aicti: Error: "aicti" directory already exists
(aicti) hdknr@macmini-spindd aicti-genai % sam init

You can preselect a particular runtime or package type when using the `sam init` experience.
Call `sam init --help` to learn more.

Which template source would you like to use?
        1 - AWS Quick Start Templates
        2 - Custom Template Location
Choice: 1

Choose an AWS Quick Start application template
        1 - Hello World Example
        2 - Data processing
        3 - Hello World Example with Powertools for AWS Lambda
        4 - Multi-step workflow
        5 - Scheduled task
        6 - Standalone function
        7 - Serverless API
        8 - Infrastructure event management
        9 - Lambda Response Streaming
        10 - Serverless Connector Hello World Example
        11 - Multi-step workflow with Connectors
        12 - GraphQLApi Hello World Example
        13 - Full Stack
        14 - Lambda EFS example
        15 - DynamoDB Example
        16 - Machine Learning
Template: 1

Use the most popular runtime and package type? (Python and zip) [y/N]: n

Which runtime would you like to use?
        1 - aot.dotnet7 (provided.al2)
        2 - dotnet8
        3 - dotnet6
        4 - go (provided.al2)
        5 - go (provided.al2023)
        6 - graalvm.java11 (provided.al2)
        7 - graalvm.java17 (provided.al2)
        8 - java21
        9 - java17
        10 - java11
        11 - java8.al2
        12 - nodejs20.x
        13 - nodejs18.x
        14 - nodejs16.x
        15 - python3.9
        16 - python3.8
        17 - python3.12
        18 - python3.11
        19 - python3.10
        20 - ruby3.3
        21 - ruby3.2
        22 - rust (provided.al2)
        23 - rust (provided.al2023)
Runtime: 17

What package type would you like to use?
        1 - Zip
        2 - Image
Package type: 2

Based on your selections, the only dependency manager available is pip.
We will proceed copying the template using pip.

Would you like to enable X-Ray tracing on the function(s) in your application?  [y/N]: n

Would you like to enable monitoring using CloudWatch Application Insights?
For more info, please view https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html [y/N]: n

Would you like to set Structured Logging in JSON format on your Lambda functions?  [y/N]: y
Structured Logging in JSON format might incur an additional cost. View https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html#monitoring-cloudwatchlogs-pricing for more details

Project name [sam-app]: aictiapi

    -----------------------
    Generating application:
    -----------------------
    Name: aictiapi
    Base Image: amazon/python3.12-base
    Architectures: x86_64
    Dependency Manager: pip
    Output Directory: .
    Configuration file: aictiapi/samconfig.toml

    Next steps can be found in the README file at aictiapi/README.md


Commands you can use next
=========================
[*] Create pipeline: cd aictiapi && sam pipeline init --bootstrap
[*] Validate SAM template: cd aictiapi && sam validate
[*] Test Function in the Cloud: cd aictiapi && sam sync --stack-name {stack-name} --watch

```

ディレクトリ構成:

```bash
aictiapi
├── README.md
├── __init__.py
├── events
│   └── event.json
├── hello_world
│   ├── Dockerfile
│   ├── __init__.py
│   ├── app.py
│   └── requirements.txt
├── samconfig.toml
├── template.yaml
└── tests
    ├── __init__.py
    └── unit
        ├── __init__.py
        └── test_handler.py

5 directories, 12 files
```

## Dockerfile

```docker
FROM public.ecr.aws/lambda/python:3.12

COPY app.py requirements.txt ./

RUN python3.12 -m pip install -r requirements.txt -t .

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
```
