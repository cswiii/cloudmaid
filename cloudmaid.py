#!/usr/bin/python
import sys
import optparse
import boto
import boto.ec2

description = "Initiates EC2 instance. Will do more later"
usage = "Usage: %prog --keyname <pubkey>"

p = optparse.OptionParser(usage=usage, description=description)
p.add_option('-k', '--keyname', type=str, dest='keyname', help='Your EC2 keyname')
options, arguments = p.parse_args()
if not options.keyname:
  print "\nPlease provide a valid key name (i.e., your pubkey) with '-k'."
  sys.exit(-1)

conn = boto.ec2.connect_to_region('us-east-1')

# For debugging
regions = boto.ec2.regions()
print regions
groups = conn.get_all_security_groups()
print groups

# Create/run instance
instance_data = conn.run_instances('ami-7d0c6314', key_name=options.keyname, instance_type='t1.micro')
instance = str(instance_data).split(':')[1]
print instance

# Show us all instances
reservations = conn.get_all_reservations()
print reservations

#conn.terminate_instances(my_instance)

