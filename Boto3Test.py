import boto3

def PrintInstanceInformation(instance):
    logString = ""
    logString += str(instance['InstanceId']) + '\t'
    logString += str(instance['InstanceType']) + '\t'
    logString += str(instance['PublicDnsName']) + '\t'

    interfaceCount = len(instance['NetworkInterfaces'])

    for num, nic in enumerate(instance['NetworkInterfaces']):
        logString += nic['Association']['PublicIp']
        if num < interfaceCount:
            logString += ", "

ec2 = boto3.client('ec2')

apiResponse = ec2.describe_instances()

for reservation in apiResponse['Reservations']:
    for instance in reservation['Instances']:
        PrintInstanceInformation(instance)