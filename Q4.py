import json

#Lambda Function which accepts name i.e event['name'] passed in the request of the API (POST)
#In the response body, it prints the name sent
def lambda_handler(event, context):
    name = event['Name']
    return {
        'Name' : name,
        }
