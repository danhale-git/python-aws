import boto3
import pprint

def PrintField(dictObject, fieldName):
    print(fieldName+": "+dictObject[fieldName])

ec2 = boto3.client('ec2')

instances = ec2.describe_instances()['Reservations'][0]['Instances']

for instance in instances:
    PrintField(instance, 'InstanceId')
    PrintField(instance, 'InstanceType')
    for nic in instance['NetworkInterfaces']:
        PrintField(nic, 'PublicIp')