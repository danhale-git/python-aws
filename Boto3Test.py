import boto3
import pprint

ec2 = boto3.client('ec2')

instances = ec2.describe_instances()['Reservations'][0]['Instances']

for instance in instances:
    print(instance['InstanceId'])
    print(instance['InstanceType'])
    print(instance['PublicDnsName'])
    print(instance['PublicIp'])