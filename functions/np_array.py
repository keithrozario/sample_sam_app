import numpy as np
import json 

def main(event, context):
    a = np.array([[1,2,3],[4,5,6]]) 
    print (a.shape)

    return  {
        "statusCode": 200,
        "body": json.dumps({
            "message": str(a.shape),
        }),
    }
