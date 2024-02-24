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

# check if the instance already exists (via creating a list)

instances = ec2.instances.all()
instance_exist = False

for instance in instances:
    for tag in instance.tags:
        if tag['Key'] == 'Name' and tag['Value'] == instance_name:
            instance_exist = True
            instance_id = instance.id
            print(f"An instance named '{instance_name}' with id '{instance_id}' already exists.")
            break
    
    if instance_exist:
        break


#ami: ami-052efd3df9dad4825

if not instance_exist:

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
    instance_id = new_instance[0].id
    print(f"An instance named '{instance_name}' with id '{instance_id}' created.")



#stop an instance via the stop() method
ec2.Instance(instance_id).stop()
print(f"An instance named '{instance_name}' with id '{instance_id}' has been stoped.")

#start an instance
ec2.Instance(instance_id).start()
print(f"An instance named '{instance_name}' with id '{instance_id}' has been started.")

    #terminate an instance
ec2.Instance(instance_id).terminate()
print(f"An instance named '{instance_name}' with id '{instance_id}' has been terminated.")
