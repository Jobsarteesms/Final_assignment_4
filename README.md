# Final_assignment_4
Data Migration and Transformation Tool for Amazon RDS Data Warehouses
# SEC Data Pipeline

This project provides a pipeline for downloading a ZIP file from a URL, extracting JSON files, uploading them to Amazon S3, and loading the data into Amazon RDS (NoSQL). The pipeline is implemented using Python.

## Project Structure

```bash
.
├── download_zip.py      # Downloads the ZIP file from the provided URL
├── extract_json.py      # Extracts JSON files from the ZIP file
├── upload_to_s3.py      # Uploads the extracted JSON files to Amazon S3
├── load_to_rds.py       # Loads the JSON data from S3 into Amazon RDS
└── README.md            # Project documentation

#Requirements
To run this project, you'll need the following Python libraries:

requests
boto3
pandas
sqlalchemy
pymysql
zipfile (Standard Library)

1. You can install the required libraries using pip:pip install requests boto3 pandas sqlalchemy pymysql

# Output

1. This script downloads a ZIP file from a specified URL:python download_zip.py

2. Extract the JSON files from the downloaded ZIP file : python extract_json.py

3. Uploads the extracted JSON files to a specified S3 bucket : python upload_to_s3.py

4. Loads the JSON data from S3 into an Amazon RDS (NoSQL) table : python load_to_rds.py

#Configuration
Amazon S3: Ensure that your AWS credentials are configured properly, either by using environment variables or by configuring them in ~/.aws/credentials.
Amazon RDS: Update the load_to_rds.py script with your RDS endpoint, database name, table name, and AWS credentials.
