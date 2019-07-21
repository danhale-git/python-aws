import boto3

def PrintInstanceInformation(instance):
    print(instance['InstanceId'])
    print(instance['InstanceType'])
    print(instance['PublicDnsName'])
    for nic in instance['NetworkInterfaces']:
        print(nic['Association']['PublicIp'])

ec2 = boto3.client('ec2')

apiResponse = ec2.describe_instances()

for reservation in apiResponse['Reservations']:
    for instance in reservation['Instances']:
        PrintInstanceInformation(instance)