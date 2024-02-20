import boto3

##############################################
#
# Author: EL Owusu
#
# creating EC2 in AWS 
# 
#################################################

# when creating a new EC2 instance we have to pass in some parameters
ec2 = boto3.resource('ec2')

instance_name = 'test_ec2'

instance_id = None #this is a null value i.e it's either True or False

#ami: ami-052efd3df9dad4825

# using the create instances method (function) to pass in these parameters down below
new_instance = ec2.create_instances(
    ImageId='ami-052efd3df9dad4825', #reqiured param
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='boto3',# use the aws cli to create a key pair
    TagSpecifications= [
        {
            'ResourceType':'instance',
            'Tags': [{
                 'Key': 'Name',
                'Value': instance_name
            },
            ]
        },
    ]
)


#stop an instance 

#start an instance

#terminate an instance