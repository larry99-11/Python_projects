import boto3
import time

##############################################
#
# Author: EL Owusu
#
# creating Aoura serverless RDS database cluster
# 
#################################################

# boto3 client for RDS (we don't have a RDS resource)
rds = boto3.client('rds')

# user defined variables:
username = 'test'
password = '2W3d5123'
db_subnet_group = 'dev-enviroment'
db_cluster_id = 'rds-test-cluster'

# create db cluser  # => check to see if the database already exists
try:
    rds.describe_db_clusters(DBClusterIdentifier=db_cluster_id) # this means that we found the db
    print(f"The DB cluster named: '{db_cluster_id}' already exists, skipping creation.")

#if the db is not found create one down below
except rds.exceptions.DBClusterNotFoundFault:
    response = rds.create_db_cluster(
        Engine ='aurora-mysql',
        EngineVersion ='5.7.mysql_aurora.2.08.3',
        DBClusterIdentifier=db_cluster_id,
        MasterUsername=username,
        MasterUserPassword=password,
        DatabaseName='rds_test_db',
        DBSubnetGroupName=db_subnet_group,
        EngineMode='serverless',
        EnableHttpEndpoint=True, # we can access the RDS console
        ScalingConfiguration={
            'MinCapacity': 1, # Minmum ACU
            'MaxCapacity': 8, #Maximum ACU
            'AutoPause': True,
            'SecondsUntilAutoPause': 300 # pause after 5 minutes of inactivity
        }
    )
    print(f"The DB cluster named '{db_cluster_id}' has been created.")

    #wait for the db cluser to be avalible
    while True:
        response =  rds.describe_db_clusters(DBClusterIdentifier=db_cluster_id)
        status = response['DBClusters']['0']['Status']
        print(f"The status of the cluster is: {status}")

        if status == 'avalible':
            break

        print("waiting for the DB cluster to avalible...")
        time.sleep(40)

# modify the db cluster, update the scaling config for the cluster
response = rds.modify_db_cluster(
        DBClusterIdentifier=db_cluster_id,
        ScalingConfiguration={
            'MinCapacity': 1, # Minmum ACU
            'MaxCapacity': 16, #Maximum ACU
            'AutoPause': True,
            'SecondsUntilAutoPause': 600 # pause after 5 minutes of inactivity
        }
    )
print(f"The DB cluster named '{db_cluster_id}' has been updated.")


#delete the cluser
response = rds.delete_db_cluster(
        DBClusterIdentifier=db_cluster_id,
        SkipFinalSnapshot=True
    )
print(f"The DB cluster named '{db_cluster_id}' has been deleted.")
