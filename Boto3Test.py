import boto3
import json

ec2 = boto3.client('ec2')

instances = ec2.describe_instances()

PrettyPrint(instances)

def PrettyPrint(data):
    print(json.dumps(data, indent=4, sort_keys=True))