import boto3

ec2 = boto3.resource('ec2')

print(ec2.describe_instances())
