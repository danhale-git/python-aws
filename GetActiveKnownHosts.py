import sys
import boto3
import paramiko
from botocore.exceptions import ClientError

#TODO
# handle multiple keys per host
# consider raising exceptions as opposed to exit(1). Which is more robust?
# implement argparse for known_hosts path
# return hashed version of output using paramiko?
# is there something lighter than ec2.describe_instances that can be used to get ec2 public dns hosts?
# SubDictValue() seems sloppy, is there a better way than .values())[0]?
# Why does the hostnames parameter in HostKeyEntry expect a list, am I missing something?

known_hostsPath = '/home/dhale/.ssh/known_hosts'

activeInstances = []
activeKeyEntries = []

def GetActiveInstances():
    try:
        ec2 = boto3.client('ec2')
        apiResponse = ec2.describe_instances()
    except ClientError as error:
        print('Error: '+error.response['Error']['Code'])
        exit(1)

    for reservation in apiResponse['Reservations']:
        for instance in reservation['Instances']:
            activeInstances.append(instance['PublicDnsName'])

def SubDictValue(subDict):
    return list(subDict.values())[0]

def GetActiveKeyEntries():
    known_hosts = paramiko.hostkeys.HostKeys()
    known_hosts.load(known_hostsPath)

    for instance in activeInstances:
        entry = known_hosts.lookup(instance)
        if entry != None:
            activeKeyEntries.append(SubDictValue(entry))
        else:
            activeInstances.remove(instance)

def PrintActiveInstanceLines():
    if len(activeKeyEntries) != len(activeInstances):
        print('Error: ActiveInstances and ActiveHostEntry arrays are not equal length.')
        exit(1)

    for index, key in enumerate(activeKeyEntries):
        entry = paramiko.hostkeys.HostKeyEntry(hostnames=[activeInstances[index]], key=key)
        print(entry.to_line().rstrip())

GetActiveInstances()
GetActiveKeyEntries()
PrintActiveInstanceLines()




    