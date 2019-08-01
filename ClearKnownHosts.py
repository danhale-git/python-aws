import boto3
import paramiko

activeInstances = []
activeHostEntries = []

GetActiveInstances()
GetActiveHostEntries()

for host in activeHostEntries:
    print(host)

for instance in activeInstances:
    print(instance)

def GetActiveInstances():
    ec2 = boto3.client('ec2')
    apiResponse = ec2.describe_instances()

    for reservation in apiResponse['Reservations']:
        for instance in reservation['Instances']:
            activeInstances.append(instance['PublicDnsName'])

def GetActiveHostEntries():
    known_hosts = paramiko.hostkeys.HostKeys()
    known_hosts.load('~/.ssh/known_hosts')

    for instance in activeInstances:
        entry = known_hosts.lookup(instance)
        if entry != None:
            activeHostEntries.append(entry)
        else:
            activeInstances.remove(instance)


    