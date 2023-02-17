import boto3
AWS_REGION = "us-east-1"
resource = boto3.resource("s3", region_name=AWS_REGION)
bucket_name = "Boto3PythonPractice"
print(" s3 created")