import boto3

ec2 = boto.resource('ec2')

print(ec2.describe_instances())
