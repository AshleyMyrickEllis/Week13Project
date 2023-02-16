import Boto3Python
aws_resource=Boto3Python
bucket=aws_resource.bucket("botopythonpractice")
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'|'us-gov-east-1'
    },
    
)

print(response)

