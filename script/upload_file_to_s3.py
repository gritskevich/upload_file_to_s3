import os
import boto3
import urllib3


def upload_file_to_s3(url, bucket, key):
    s3 = boto3.client('s3')
    http = urllib3.PoolManager()

    try:
        response = http.request('GET', url, preload_content=False)
        if 400 <= response.status < 600:
            print(f'Error {response.status} while accessing log file at {url}')
            return False

        s3.upload_fileobj(http.request('GET', url, preload_content=False), bucket, key)
        print(f'Log file {url} uploaded to {bucket}/{key}')
        return True
    except Exception as e:
        print(f'Error uploading log file: {e}')
        return False


if __name__ == '__main__':
    url = os.environ['URL']
    bucket = os.environ['BUCKET_NAME']
    key = os.environ['S3_KEY']
    upload_file_to_s3(url, bucket, key)
