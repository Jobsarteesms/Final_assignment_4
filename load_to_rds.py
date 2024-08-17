import boto3
import pandas as pd
import json
from sqlalchemy import create_engine

def load_data_to_rds(bucket_name, rds_endpoint, db_name, table_name, aws_access_key_id, aws_secret_access_key):
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    s3_objects = s3.list_objects_v2(Bucket=bucket_name).get('Contents', [])

    engine = create_engine(f'mysql+pymysql://{aws_access_key_id}:{aws_secret_access_key}@{rds_endpoint}/{db_name}')

    for obj in s3_objects:
        if obj['Key'].endswith('.json'):
            s3_file_path = obj['Key']
            obj = s3.get_object(Bucket=bucket_name, Key=s3_file_path)
            data = json.loads(obj['Body'].read().decode('utf-8'))

            df = pd.json_normalize(data)
            df.to_sql(table_name, engine, if_exists='append', index=False)

if __name__ == "__main__":
    bucket_name = "star-s3-bucket"
    rds_endpoint = "star-rds-endpoint"
    db_name = "star-database"
    table_name = "star-table"
    aws_access_key_id = "*************"
    aws_secret_access_key = "**********"
    
    load_data_to_rds(bucket_name, rds_endpoint, db_name, table_name, aws_access_key_id, aws_secret_access_key)