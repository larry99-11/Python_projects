import boto3
import json
import logging
from datetime import datetime

##################################################
# Author: EL Owusu
#
# lamda function which creates a ec2 daily snapshot at regular intervals
# 
#################################################


# we want to setup some logs here 
log = logging.getLogger()
log.setLevel(logging.INFO)


def lambda_handler(event, context):
    #do some stuff here
    ec2 = boto3.client('ec2')
    # the format will be: year/month/day of the current day
    current_date =  datetime.now().strftime("%Y-%m-%d")


    #the snapshot logic
    try:
        response = ec2.create_snapshot(

            VolumeId='vol-0f775b76c6c494921',
            Description ='My EC2 snapshot',
            TagSpecifications=[
                {
                    'ResourceType': 'snapshot',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': f"My EC2 snapshot {current_date}"
                         }
                        ]
                }
            ]
        )
        #this will dump our response variable into the logger.
        log.info(f"sucessfully created snapshot: {json.dumps(response, default=str)} ")

    except Exception as e:
        log.error(f"Error creating snapshot: {str(e)}")



    return {
        'statusCode': 200,
        'body': json.dumps('Testing lambda func')
    }