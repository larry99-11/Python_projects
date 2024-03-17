import boto3

##################################
# AWS resource handeler
####################################

ec2_client = boto3.client('ec2')

def stop_ec2():

    response = ec2_client.describe_instances(
        Filters=[{'Name': 'instance-state-name',
         'Values': ['running']}]
         )

    instances = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_info = {
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'PublicIpAddress': instance.get('PublicIpAddress', 'N/A'),
                'PrivateIpAddress': instance.get('PrivateIpAddress', 'N/A'),
                'State': instance['State']['Name']
            }
            instances.append(instance_info)

    for instance in instances:
        print("Listing current running instances:")
        print("")

        print(instance)
        print("")

    # Print the list of instances
    for index, instance in enumerate(instances, start=1):
        print(f"{index}: {instance}")

    # Ask user to select instances to stop
    instances_to_stop = input("Enter the numbers (separated by comma) of instances to stop: ")

    # Convert input string to a list of indices
    indices_to_stop = [int(index) for index in instances_to_stop.split(",")]

    # Stop selected instances
    for index in indices_to_stop:
        instance_id = instances[index - 1]['InstanceId']
        print(f"Stopping instance with ID {instance_id}...")
        ec2_client.stop_instances(InstanceIds=[instance_id])
        print(f"Instance with ID {instance_id} stopped successfully.")

def start_ec2():

    # Retrieve information about stopped instances

    response = ec2_client.describe_instances(
        Filters=[{'Name': 'instance-state-name',
         'Values': ['stopped']}]
         )

    instances_ts = []

    # Extract instance information
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_info = {
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'State': instance['State']['Name']
            }
            instances_ts.append(instance_info)

    # Print the list of instances
    for index, instance in enumerate(instances_ts, start=1):
        print(f"{index}: {instance}")

    # Ask user to select instances to start
    instances_to_start = input("Enter the numbers (separated by comma) of instances to start: ")

    # Convert input string to a list of indices
    indices_to_start = [int(index) for index in instances_to_start.split(",")]

    # Start selected instances
    for index in indices_to_start:
        instance_id = instances_ts[index - 1]['InstanceId']
        print(f"Starting instance with ID {instance_id}...")
        ec2_client.start_instances(InstanceIds=[instance_id])
        print(f"Instance with ID {instance_id} started successfully.")



# do we want to start ec2 instances
user_input = input("would you like to start all stopped instances?(y/n): ")

if user_input == 'y':
    start_ec2()

elif user_input == 'n':
    stop_ec2()

# do we want to stop the ec2 insances






    #user_input = input("would you like to stop all running instances?")

#if user_input == 'y':




#give a list of current EC2 servers running


# stop the EC2 servers
#ec2.Instnce(instance_id).stop()


# start an instance

# Initialize the EC2 client

# Retrieve information about running instances

# Extract instance information


# Print the list of instances


