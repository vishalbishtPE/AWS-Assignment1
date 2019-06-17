import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

#Table name is Books_Vishal10
table1 = dynamodb.Table('Books_Vishal10')



# Querying the DynamoDB by year and title
response = table1.get_item(
    Key={
        'year':2015,
        'title':'ABC'
    }
)
item = response['Item']
print(item)
