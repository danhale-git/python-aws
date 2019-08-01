import boto3
import paramiko

#TODO
# implement argparse for known_hosts path
# hash new known_hosts contents using paramiko?
# is there something lighter than ec2.describe_instances that can be used to get ec2 public dns hosts?
# print actual known_hosts file entries 
# handle boto3 client errors

known_hostsPath = '/home/dhale/.ssh/known_hosts'

activeInstances = []
activeHostEntries = []

def GetActiveInstances():
    ec2 = boto3.client('ec2')
    apiResponse = ec2.describe_instances()

    for reservation in apiResponse['Reservations']:
        for instance in reservation['Instances']:
            activeInstances.append(instance['PublicDnsName'])

def GetActiveHostEntries():
    known_hosts = paramiko.hostkeys.HostKeys()
    known_hosts.load(known_hostsPath)

    for instance in activeInstances:
        entry = known_hosts.lookup(instance)
        if entry != None:
            activeHostEntries.append(entry)
        else:
            activeInstances.remove(instance)

GetActiveInstances()
GetActiveHostEntries()

for host in activeHostEntries:
    print(host)

for instance in activeInstances:
    print(instance)




    