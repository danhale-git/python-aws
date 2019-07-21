import boto3
import json

ec2 = boto3.client('ec2')

instances = ec2.describe_instances()

print(type(instances))
