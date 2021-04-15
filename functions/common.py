import json
def common_return(message: str):

    return_dict= {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
        }),
    }

    return return_dict