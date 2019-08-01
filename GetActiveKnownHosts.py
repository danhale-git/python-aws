import sys
import boto3
import paramiko
from botocore.exceptions import ClientError
import json#DEBUG

#TODO
# handle multiple keys per host
# consider raising exceptions as opposed to exit(1). Which is more robust?
# implement argparse for known_hosts path
# hash new known_hosts contents using paramiko?
# is there something lighter than ec2.describe_instances that can be used to get ec2 public dns hosts?
# print actual known_hosts file entries 

known_hostsPath = '/home/dhale/.ssh/known_hosts'

activeInstances = []
activeKeyEntries = []

def GetActiveInstances():
    try:
        ec2 = boto3.client('ec2') # Should this be in the try: block? Can it throw a ClientError?
        apiResponse = ec2.describe_instances()
    except ClientError as error:
        print('Error: '+error.response['Error']['Code'])
        exit(1)

    for reservation in apiResponse['Reservations']:
        for instance in reservation['Instances']:
            activeInstances.append(instance['PublicDnsName'])

def GetActiveKeyEntries():
    known_hosts = paramiko.hostkeys.HostKeys()
    known_hosts.load(known_hostsPath)

    for instance in activeInstances:
        entry = known_hosts.lookup(instance)
        if entry != None:
            activeKeyEntries.append(list(entry.values())[0])
        else:
            activeInstances.remove(instance)

def PrintActiveInstanceLines():
    if len(activeKeyEntries) != len(activeInstances):
        print('Error: ActiveInstances and ActiveHostEntry arrays are not equal length.')
        exit(1)

    for value in activeKeyEntries:#DEBUG
        print(type(value))

    #for index, host in enumerate(activeKeyEntries):
    #    entry = paramiko.hostkeys.HostKeyEntry(hostnames=host, key=activeKeyEntries[index])
    #    print(entry.to_line())

GetActiveInstances()
GetActiveKeyEntries()
PrintActiveInstanceLines()

for host in activeKeyEntries:
    print(host)

for instance in activeInstances:
    print(instance)




    