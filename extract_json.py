import zipfile
import os

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

if __name__ == "__main__":
    zip_path = "data.zip"
    extract_to = "extracted_data"
    extract_zip(zip_path, extract_to)