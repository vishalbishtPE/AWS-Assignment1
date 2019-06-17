from __future__ import print_function # Python 2/3 compatibility
import boto3

#Defining dynamodb and its region
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

#Table Schema
#Table name is Books_Vishal11. Its Partition key is year(type-Number)
#And its sort key is title(type-String)

table = dynamodb.create_table(
    TableName='Books_Vishal11',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)



#Inserting items in DynamoDB

table1 = dynamodb.Table('Books_Vishal10')


#Inserting item1 
table1.put_item(
   Item={
        'year':2015,
        'title':'ABC',
        'rating':19
    }
)

#Inserting item 2
table1.put_item(
   Item={
        'year':2016,
        'title':'PQR',
        'rating':17
    }
)


#Inserting item3
table1.put_item(
   Item={
        'year':207,
        'title':'XYZ',
        'rating':14
    }
)



print("PutItem succeeded:")

                                                                                                                            42,0-1        Bot


                                                
