import os

from boto3 import client


model_object_name = 'model.onnx'
s3_endpoint_url = os.environ.get('AWS_S3_ENDPOINT')
s3_access_key = os.environ.get('AWS_ACCESS_KEY_ID')
s3_secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
s3_bucket_name = os.environ.get('AWS_S3_BUCKET')


def initialize_s3_client(s3_endpoint_url, s3_access_key, s3_secret_key):
    print('initializing S3 client')
    s3_client = client(
        's3', aws_access_key_id=s3_access_key,
        aws_secret_access_key=s3_secret_key,
        endpoint_url=s3_endpoint_url,
    )
    return s3_client


def upload_model(s3_client, object_name):
    print(f'uploading model to {object_name}')
    try:
        s3_client.upload_file('model.onnx', s3_bucket_name, object_name)
    except:
        print(f'S3 upload to bucket {s3_bucket_name} at {s3_endpoint_url} failed!')
        raise


if __name__ == '__main__':
    s3_client = initialize_s3_client(
        s3_endpoint_url=s3_endpoint_url,
        s3_access_key=s3_access_key,
        s3_secret_key=s3_secret_key
    )
    upload_model(s3_client, model_object_name)
