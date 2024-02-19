import boto3

##############################################
#
# Author: EL Owusu
#
# creating s3 buckets in AWS and preforming CRUD operations
# 
#################################################

# intialize a boto3 resource for s3 then name the bucket
s3 = boto3.resource('s3')
bucket_name = 'programmed-bucket'

# check if bucket_name exsits if it doesn't create create a new one
all_buckets = [bucket.name for bucket in s3.buckets.all()]

if bucket_name not in all_buckets:
    print(f"==> {bucket_name} does not exist. Creating now...")

    s3.create_bucket(Bucket=bucket_name)

    print(f"==>'{bucket_name}' Has been created!")

else:
    print(f"==>'{bucket_name}' exists already.")


# create example_file1 and example_file2
file1= 'example_file1'
file2= 'example_file2'

# Upload  example_file1 to the new bucket
s3.Bucket(bucket_name).upload_file(Filename=file1, Key=file1)

# read and print the file from the bucket
obj = s3.Object(bucket_name, file1)
body = obj.get()['Body'].read() 
print(body)

# update the example_file1 with the content from example_file2
s3.Object(bucket_name, file1).put(Body=open(file2, 'rb'))

obj = s3.Object(bucket_name, file1)
body = obj.get()['Body'].read() 
print(body)


# delete the file from the bucket 
print(f"deleting {file1} from {bucket_name}!")
s3.Object(bucket_name, file1).delete()

# delete the bucket 
bucket = s3.Bucket(bucket_name)
bucket.delete()
