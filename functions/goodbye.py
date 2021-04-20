import common
from aws_lambda_powertools import Logger

logger = Logger()

@logger.inject_lambda_context
def main(event, context):
    logger.info("Writing out Goodbye")
    logger.info({"Test": "Hello"})
    return common.common_return("Goodbye-sdiuaghdfiaew7rtqewrv")
