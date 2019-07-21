import boto3

def InstanceData(instance):
    logString = ""
    logString += str(instance['InstanceId']) + '\t'
    logString += str(instance['InstanceType']) + '\t'
    logString += str(instance['PublicDnsName']) + '\t'

    interfaceCount = len(instance['NetworkInterfaces'])

    for num, nic in enumerate(instance['NetworkInterfaces'], 1):
        logString += nic['Association']['PublicIp']
        if num < interfaceCount:
            logString += ", "

    return logString

ec2 = boto3.client('ec2')

apiResponse = ec2.describe_instances()

for reservation in apiResponse['Reservations']:
    for instance in reservation['Instances']:
        print(InstanceData(instance))