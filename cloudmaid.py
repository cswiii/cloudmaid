#!/usr/bin/python
import boto
import boto.ec2
import paramiko

# For debugging
regions = boto.ec2.regions()
print regions

connection = boto.ec2.connect_to_region('us-east-1')
groups = connection.get_all_security_groups()
print groups
#image = connection.get_all_images()

connection.run_instances('ami-7d0c6314')

