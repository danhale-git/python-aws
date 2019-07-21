import boto3
import pprint

ec2 = boto3.client('ec2')

instances = ec2.describe_instances()

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'])
        print(instance['InstanceType'])
        print(instance['PublicDnsName'])
        for nic in instance['NetworkInterfaces']:
            print(nic['Association']['PublicIp'])