import os
import boto3
import urllib3


def lambda_handler(event, context):
    url = os.environ['URL']
    bucket = os.environ['BUCKET_NAME']
    key = os.environ['S3_KEY']

    s3 = boto3.client('s3')
    http = urllib3.PoolManager()

    try:
        response = http.request('GET', url, preload_content=False)
        if 400 <= response.status < 600:
            print(f'Error {response.status} while accessing log file at {url}')
            return {'statusCode': response.status, 'body': f'Error {response.status} while accessing log file'}

        s3.upload_fileobj(http.request('GET', url, preload_content=False), bucket, key)
        print(f'Log file {url} uploaded to {bucket}/{key}')
        return {'statusCode': 200, 'body': 'Log file uploaded successfully'}
    except Exception as e:
        print(f'Error uploading log file: {e}')
        return {'statusCode': 500, 'body': 'Error uploading log file'}


lambda_handler(None, None)
