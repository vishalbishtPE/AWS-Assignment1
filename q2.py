import boto3

client = boto3.client('s3')
versions = client.list()

#The entry.txt file is in the S3 bucket and newentry.txt is the file that it gets downloaded as.
#The versionId provided is the second last version of the file in, entry.txt
client.download_file('entry', 'newentry.txt', 'f1',ExtraArgs={'VersionId':'ZMHTToZSP4xpj43q.SDcZGHCnpKvTXW6Nn'})
