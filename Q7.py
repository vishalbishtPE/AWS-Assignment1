import boto3
import json

def main():
	iam=boto3.client('iam')
	ec2=boto3.client('ec2',region_name="us-east-1")
	
	#Defining the trust policy
	trust_policy={
  	"Version": "2012-10-17",
  	"Statement": [
    	{
      	"Sid": "createRole",
      	"Effect": "Allow",
      	"Principal": {
        	"Service": "ec2.amazonaws.com"
      	},
      	"Action": "sts:AssumeRole"
    	}
 	 ]
	}


	tags=[
    	{
        	'Key': '',
        	'Value': ''
    	}
	]

	try:
    		
    		#Task1- Creating a role
    		response = iam.create_role(
        		Path="/",
        		RoleName="vishal-role",
        		AssumeRolePolicyDocument=json.dumps(trust_policy),
        		Description="Creating the Role,
        		Tags=tags
    		)

    		print(response)
		#Task 2 - Creating a policy

        	policyDoc={"Version": "2012-10-17",
    		"Statement": [
       			{
       	    		"Effect": "Allow",
       	    		"Action": "s3:*",
       	    		"Resource": "*"
        		}
    			]
   	
        		}
        	policy= iam.create_policy( PolicyName="s3_Full_access2",PolicyDocument=json.dumps(policyDoc) )
       		attaching_policy=iam.attach_role_policy("vishal-role",PolicyArn=policy['Policy']['Arn'])
		
		#Task3 - Creating profile instance
		instance_profile= iam.create_instance_profile("vishal-profile", "/")
		
		#Task4- Attach role to instance
		response= iam.add_role_to_instance_profile(InstanceProfileName="vishal-profile", RoleName="vishal-role")
		associate=ec2.describe_iam_instance_profile_associations(Filters=[{'Name': 'instance-id','Values': [ec2_instance,]}])

		#Task 5- Associating instance profile with ec2
		AssociationId=associate['IamInstanceProfileAssociations'][0]['AssociationId']
		print(instance_profile)

		res =ec2.replace_iam_instance_profile_association(
    		IamInstanceProfile={
        		'Arn': instance_profile['InstanceProfile']['Arn'],# place your arn instance_profile here 
        		'Name': ProfileName
    		},
    		AssociationId=AssociationId
		)

	except Exception as e:
        print("Error")
        raise e
if __name__=='__main__':
main()
