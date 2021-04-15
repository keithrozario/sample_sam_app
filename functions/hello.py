import json

def main(event, context):

    return_dict= {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello World!~34219048123y4b23",
        }),
    }

    return return_dict
