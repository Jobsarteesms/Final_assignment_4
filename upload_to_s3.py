import boto3
import os

def upload_to_s3(directory, bucket_name):
    s3 = boto3.client('s3')
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            s3.upload_file(file_path, bucket_name, filename)

if __name__ == "__main__":
    directory = "extracted_data"
    bucket_name = "star-s3-bucket-name"
    upload_to_s3(directory, bucket_name)