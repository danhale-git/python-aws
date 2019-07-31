import paramiko

hostname = "ec2-35-178-232-127.eu-west-2.compute.amazonaws.com"

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.WarningPolicy)
client.connect(hostname, username='ubuntu')

stdin, stdout, stderr = client.exec_command('ls -lh ~/.ssh')
print(stdout.read().decode('ascii'))