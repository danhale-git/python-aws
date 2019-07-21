import boto3
import pprint

ec2 = boto3.client('ec2')

instances = ec2.describe_instances()['Reservations'][0]['Instances']

pprint.pprint(instances)