import requests

def download_zip(url, output_path):
    response = requests.get(url)
    with open(output_path, 'wb') as file:
        file.write(response.content)

if __name__ == "__main__":
    url = "https://www.sec.gov/edgar/sec-api-documentation"
    output_path = "data.zip"
    download_zip(url, output_path)