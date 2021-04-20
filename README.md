# Simple Python app using AWS SAM

## Prerequisite

- Sam-cli
- Docker (not strictly necessary, but we will use it)

## To deploy the app

    $ sam build --use-container
    $ sam deploy

Whenever changes are made, you will typically have to execute **both** the build and deploy commands.

## Invoking the function

To invoke the function, you may curl the endpoint specified in the output of the `sam deploy` command. 

Alternatively, you may use the console to invoke it manually.

## Viewing logs

The example code uses `aws-lambda-powertools` to provide better logging functionality. We use the `requirements.txt` file to include this package into the deployment.

Once deployed, we can view the logs via the AWS Console on cloudwatch **or** run the following sam-cli command:

    $ sam logs -n GoodbyeWorldFunction --region ap-southeast-1 --stack-name sam-app

To "tail" the logs, simply add the --tail command

    $ sam logs -n GoodbyeWorldFunction --region ap-southeast-1 --stack-name sam-app --tail
  
An example of how to log out code from the function:

```python

from aws_lambda_powertools import Logger

logger = Logger()

@logger.inject_lambda_context
def main(event, context):
    logger.info("Writing out Goodbye")
    logger.error({"Code": "101"})
    return 

```

## Add packages

To add packages, add them to the `requirements.txt`. However, there are size limits to the packages we can include here.

## Api Keys

The example includes custom CloudFormation scripts to deploy an API Key and associate it with your API. You can obtain the API Key via the AWS Console after deploying, or running the following aws command.

    $ aws apigateway get-api-keys --name-query sam-app-apikey --region ap-southeast-1 --include-value

*Note: the template deploys the API Key with the same \<stackname\>-apikey*

Once you obtain the value for the apikey, you can curl the endpoint like so, where <XXXX> is the value of the apikey:

    $ curl https://glhhwuvkac.execute-api.ap-southeast-1.amazonaws.com/Prod/goodbye/ -H "x-api-key:\<XXXX\>"

The command above is a regular curl command, but includes the apikey in the `x-api-key` HTTP Header.

To enable api key authorization on a function, include the following Yaml in the function:

```yaml
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: <Path>
            Method: <method>
            Auth:
              ApiKeyRequired: true
```