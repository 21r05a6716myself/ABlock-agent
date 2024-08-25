import boto3
#code setup up a connection to amazon s3 using the boto3 library
import os

s3 = boto3.client('s3')

def backup_files(directory, bucket_name):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            s3.upload_file(file_path, bucket_name, filename)
            print(f"{filename} backed up successfully.")

backup_files('/important_data', 'your-s3-bucket-name')
