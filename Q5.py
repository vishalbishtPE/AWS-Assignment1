
import boto3
import json

#This lambda function copy the file, entry.txt in the bucket from vishal-bucket-1 i.e. source bucket.
#And puts in vishal-bucket-2 i.e. destination bucket as newentry.txt file.

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    copy_source = {
      'Bucket': 'vishal-bisht-bucket-1',
      'Key': 'entry.txt'
        }
    bucket = s3.Bucket('vishal-bisht-bucket-2')
    bucket.copy(copy_source, 'newentry.txt')
 
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


