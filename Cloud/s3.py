import boto3

##############################################
#
# Author: EL Owusu
#
# listing s3 buckets avalible in AWS
# 
#################################################

# Here we are going to make a s3 reosuce and assign it to a variable
s3 = boto3.resource('s3')

# we are interating through all the buckets in our s3 variable and print the bucket name
for bucket in s3.buckets.all():
    print(bucket.name)


