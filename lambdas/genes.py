import json


def get(event, context):
    body = {
        "message": "GET request for a gene expression received",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def post(event, context):
    body = {
        "message": (
            f"POST request for a gene expression has been received!",
            f"We have written to the database!"
        ),
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
